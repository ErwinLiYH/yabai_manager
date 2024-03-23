import subprocess
import json
from functools import wraps
import time
from Kkit import timeout
from . import LOGGER

IP = 'localhost'
PORT = 22118
MINIMIZE_ANIME_TIME = 0.5


# Functions to send signal to the rumps app to update the title-------------------------------------

def send_update_single():
    LOGGER.debug(f"Begin command: echo 'u' | nc {IP} {PORT}")
    subprocess.run(f'echo "u" | nc {IP} {PORT}', shell=True)
    LOGGER.debug(f"End command: echo 'u' | nc {IP} {PORT}")

def send_quit_single():
    LOGGER.debug(f"Begin command: echo 'q' | nc {IP} {PORT}")
    subprocess.run(f'echo "q" | nc {IP} {PORT}', shell=True)
    LOGGER.debug(f"End command: echo 'q' | nc {IP} {PORT}")

# Functions to query yabai--------------------------------------------------------------------------

def query_windows_in_space():
    LOGGER.debug("Begin command: yabai -m query --windows --space")
    result = subprocess.run(['yabai', '-m', 'query', '--windows', '--space'], capture_output=True, text=True)
    LOGGER.debug("End command: yabai -m query --windows --space")
    return json.loads(result.stdout)

def query_focus_sapce():
    LOGGER.debug("Begin command: yabai -m query --spaces --space")
    result = subprocess.run(['yabai', '-m', 'query', '--spaces', '--space'], capture_output=True, text=True)
    LOGGER.debug("End command: yabai -m query --spaces --space")
    return json.loads(result.stdout)

def query_spaces():
    LOGGER.debug("Begin command: yabai -m query --spaces")
    result = subprocess.run(['yabai', '-m', 'query', '--spaces'], capture_output=True, text=True)
    LOGGER.debug("End command: yabai -m query --spaces")
    return json.loads(result.stdout)

def query_displays():
    LOGGER.debug("Begin command: yabai -m query --displays")
    result = timeout.run_command_with_timeout(['yabai', '-m', 'query', '--displays'], retry_times=5, capture_output=True, text=True)
    LOGGER.debug("End command: yabai -m query --displays")
    return json.loads(result.stdout)

def get_focused_window_id():
    LOGGER.debug("Begin command: yabai -m query --windows --window")
    result = subprocess.run(['yabai', '-m', 'query', '--windows', '--window'], capture_output=True, text=True)
    LOGGER.debug("End command: yabai -m query --windows --window")
    try:
        res_id = json.loads(result.stdout)['id']
    except:
        res_id = None
    return res_id

def get_display_number():
    return len(query_displays())

def get_info():
    number_of_display = get_display_number()

    spaces = query_spaces()
    display_space_dict = {}

    # create a dictionary to store each display's space index
    for space in spaces:
        if space['display'] not in display_space_dict:
            display_space_dict[space['display']] = [space['index']]
        else:
            display_space_dict[space['display']].append(space['index'])

    # sort each display's space index
    for display in display_space_dict:
        display_space_dict[display].sort()

    focus_space = query_focus_sapce()
    space_type = type_abreviation(focus_space['type'])
    focus_space_index = focus_space['index']
    focus_display = focus_space['display']
    focus_space_index_in_display = display_space_dict[focus_display].index(focus_space_index)
    num_of_spaces_in_display = len(display_space_dict[focus_display])
    num_of_space_in_total = len(spaces)

    if number_of_display > 1:
        return f"|{focus_space_index_in_display+1}:{num_of_spaces_in_display}|{focus_space_index}:{num_of_space_in_total}|{space_type}|"
    else:
        return f"|{focus_space_index_in_display+1}:{num_of_spaces_in_display}|{space_type}|"

# utils functions-----------------------------------------------------------------------------------

def for_all_windows_in_space(func):
    @wraps(func)
    def wrapper():
        windows = query_windows_in_space()
        for i in windows:
            func(i)
    return wrapper

def type_abreviation(type_string):
    if type_string == 'float':
        return 'F'
    elif type_string == 'bsp':
        return 'T'
    else:
        return 'U'

@for_all_windows_in_space
def fullscreen_layernormal_all_windows_in_space(i):
    """
    this function is used to full screen all windows in the current space after the space layout is changed to float
    all windows created in bsp layout have a sub_layer of below, so we need to change it to normal
    """

    LOGGER.debug(f"Begin command: yabai -m window {i['id']} --grid 1:1:0:0:1:1")
    subprocess.run(['yabai', '-m', 'window', str(i["id"]), '--grid', '1:1:0:0:1:1'])
    LOGGER.debug(f"End command: yabai -m window {i['id']} --grid 1:1:0:0:1:1")

    LOGGER.debug(f"Begin command: yabai -m window {i['id']} --layer normal")
    subprocess.run(['yabai', '-m', 'window', str(i["id"]), '--layer', 'normal'])
    LOGGER.debug(f"End command: yabai -m window {i['id']} --layer normal")

@for_all_windows_in_space
def layernormal_all_windows_in_space(i):
    LOGGER.debug(f"Begin command: yabai -m window {i['id']} --layer normal")
    subprocess.run(['yabai', '-m', 'window', str(i["id"]), '--layer', 'normal'])
    LOGGER.debug(f"End command: yabai -m window {i['id']} --layer normal")

# Functions to manage yabai-------------------------------------------------------------------------

def toggle_space_layout(float2max=True):
    space = query_focus_sapce()
    if space['type'] == 'float':
        LOGGER.debug("Begin command: yabai -m space --layout bsp")
        subprocess.run(['yabai', '-m', 'space', '--layout', 'bsp'])
        LOGGER.debug("End command: yabai -m space --layout bsp")
        send_update_single()
    else:
        LOGGER.debug("Begin command: yabai -m space --layout float")
        subprocess.run(['yabai', '-m', 'space', '--layout', 'float'])
        LOGGER.debug("End command: yabai -m space --layout float")
        if float2max:
            fullscreen_layernormal_all_windows_in_space()
        else:
            layernormal_all_windows_in_space()
        send_update_single()

def minimize_all_windows_in_space(except_focus=True, left_focus=True):
    @for_all_windows_in_space
    def __minimize_all_windows_in_space(i):
        if (i["has-focus"] == False) or (except_focus == False):
            LOGGER.debug(f"Begin command: yabai -m window --minimize {i['id']}")
            subprocess.run(['yabai', '-m', 'window', '--minimize', str(i["id"])])
            LOGGER.debug(f"End command: yabai -m window --minimize {i['id']}")
    __minimize_all_windows_in_space()
    if left_focus:
        subprocess.run(['yabai', '-m', 'window', '--grid', '1:3:0:0:2:1'])

def deminimize_all_windows_in_space(refocus=True, full_screen=True):
    @for_all_windows_in_space
    def __deminimize_all_windows_in_space(i):
        if i["is-minimized"] == True:
            LOGGER.debug(f"Begin command: yabai -m window --deminimize {i['id']}")
            subprocess.run(['yabai', '-m', 'window', '--deminimize', str(i["id"])])
            LOGGER.debug(f"End command: yabai -m window --deminimize {i['id']}")
    focused_id = get_focused_window_id()
    __deminimize_all_windows_in_space()
    if refocus:
        if focused_id:
            time.sleep(MINIMIZE_ANIME_TIME)
            LOGGER.debug(f"Begin command: yabai -m window --focus {focused_id}")
            subprocess.run(['yabai', '-m', 'window', '--focus', str(focused_id)])
            LOGGER.debug(f"End command: yabai -m window --focus {focused_id}")
            if full_screen:
                LOGGER.debug(f"Begin command: yabai -m window {focused_id} --grid 1:1:0:0:1:1")
                subprocess.run(['yabai', '-m', 'window', '--grid', '1:1:0:0:1:1'])
                LOGGER.debug(f"End command: yabai -m window {focused_id} --grid 1:1:0:0:1:1")
        else:
            return 1