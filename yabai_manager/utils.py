import subprocess
import json
from functools import wraps
import time

IP = 'localhost'
PORT = 22118
MINIMIZE_ANIME_TIME = 0.5

# Functions to send signal to the rumps app to update the title-------------------------------------

def send_update_single():
    subprocess.run(f'echo "u" | nc {IP} {PORT}', shell=True)

def send_quit_single():
    subprocess.run(f'echo "q" | nc {IP} {PORT}', shell=True)

# Functions to query yabai--------------------------------------------------------------------------

def query_windows_in_space():
    result = subprocess.run(['yabai', '-m', 'query', '--windows', '--space'], capture_output=True, text=True)
    return json.loads(result.stdout)

def query_focus_sapce():
    result = subprocess.run(['yabai', '-m', 'query', '--spaces', '--space'], capture_output=True, text=True)
    return json.loads(result.stdout)

def query_spaces():
    result = subprocess.run(['yabai', '-m', 'query', '--spaces'], capture_output=True, text=True)
    return json.loads(result.stdout)

def query_displays():
    result = subprocess.run(['yabai', '-m', 'query', '--displays'], capture_output=True, text=True)
    return json.loads(result.stdout)

def get_focused_window_id():
    result = subprocess.run(['yabai', '-m', 'query', '--windows', '--window'], capture_output=True, text=True)
    return json.loads(result.stdout)['id']

def for_all_windows_id_in_space(func):
    @wraps(func)
    def wrapper():
        windows = query_windows_in_space()
        for i in windows:
            func(i)
    return wrapper

def get_display_number():
    return len(query_displays())

def type_abreviation(type_string):
    if type_string == 'float':
        return 'F'
    elif type_string == 'bsp':
        return 'T'
    else:
        return 'U'

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

# this function is used to full screen all windows in the current space after the space layout is changed to float
# all windows created in bsp layout have a sub_layer of below, so we need to change it to normal
@for_all_windows_id_in_space
def fullscreen_layernormal_all_windows_in_space(i):
    subprocess.run(['yabai', '-m', 'window', str(i["id"]), '--grid', '1:1:0:0:1:1'])
    subprocess.run(['yabai', '-m', 'window', str(i["id"]), '--layer', 'normal'])

@for_all_windows_id_in_space
def layernormal_all_windows_in_space(i):
    subprocess.run(['yabai', '-m', 'window', str(i["id"]), '--layer', 'normal'])

def toggle_space_layout(float2max=True):
    space = query_focus_sapce()
    if space['type'] == 'float':
        subprocess.run(['yabai', '-m', 'space', '--layout', 'bsp'])
        send_update_single()
    else:
        subprocess.run(['yabai', '-m', 'space', '--layout', 'float'])
        if float2max:
            fullscreen_layernormal_all_windows_in_space()
        else:
            layernormal_all_windows_in_space()
        send_update_single()

def minimize_all_windows_in_space(except_focus=True):
    @for_all_windows_id_in_space
    def __minimize_all_windows_in_space(i):
        if (i["has-focus"] == False) or (except_focus == False):
            subprocess.run(['yabai', '-m', 'window', '--minimize', str(i["id"])])
    __minimize_all_windows_in_space()

def deminimize_all_windows_in_space(refocus=True):
    @for_all_windows_id_in_space
    def __deminimize_all_windows_in_space(i):
        if i["is-minimized"] == True:
            subprocess.run(['yabai', '-m', 'window', '--deminimize', str(i["id"])])
    focused_id = get_focused_window_id()
    __deminimize_all_windows_in_space()
    if refocus:
        time.sleep(MINIMIZE_ANIME_TIME)
        subprocess.run(['yabai', '-m', 'window', '--focus', str(focused_id)])