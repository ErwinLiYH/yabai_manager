import subprocess
import json

def query_windows_in_space():
    result = subprocess.run(['yabai', '-m', 'query', '--windows', '--space'], capture_output=True, text=True)
    return result.stdout

def query_focus_sapce():
    result = subprocess.run(['yabai', '-m', 'query', '--spaces', '--space'], capture_output=True, text=True)
    return result.stdout

def query_spaces():
    result = subprocess.run(['yabai', '-m', 'query', '--spaces'], capture_output=True, text=True)
    return result.stdout

def type_abreviation(type_string):
    if type_string == 'float':
        return 'F'
    elif type_string == 'bsp':
        return 'T'
    else:
        return 'U'

def get_info():
    json_str_result = query_spaces()
    spaces = json.loads(json_str_result)
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

    focus_space = json.loads(query_focus_sapce())
    space_type = type_abreviation(focus_space['type'])
    focus_space_index = focus_space['index']
    focus_display = focus_space['display']
    focus_space_index_in_display = display_space_dict[focus_display].index(focus_space_index)
    num_of_spaces_in_display = len(display_space_dict[focus_display])
    num_of_space_in_total = len(spaces)

    return f"|{focus_space_index_in_display+1}:{num_of_spaces_in_display}|{focus_space_index}:{num_of_space_in_total}|{space_type}|"

def full_screen_all_windows_in_space():
    window_ids = [i["id"] for i in json.loads(query_windows_in_space())]
    for i in window_ids:
        subprocess.run(['yabai', '-m', 'window', str(i), '--grid', '1:1:0:0:1:1'])