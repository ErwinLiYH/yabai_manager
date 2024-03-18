from . import utils
from .yabai_manager import YabaiManager
import argparse

def main():
    parser = argparse.ArgumentParser(description='Yabai manager CLI')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0', help='show version')
    parser.add_argument('--startGUI', action='store_true', default=False, help='start yabai manager GUI')
    parser.add_argument('--quitGUI', action='store_true', default=False, help='quit yabai manager GUI')
    parser.add_argument('--restartGUI', action='store_true', default=False, help='restart yabai manager GUI')

    sub_parser_windows = subparsers.add_parser('windows', help='deminimize all windows in space')
    sub_parser_windows.add_argument('--deminimize', '-dm', action='store_true', default=False, help='deminimize all windows in space')
    sub_parser_windows.add_argument('--minimize', '-mn', action='store_true', default=False, help='minimize all windows in space')
    sub_parser_windows.add_argument('--refocus', '-r', action='store_true', default=False, help='refocus the last focused window when deminimizing all windows in space')
    sub_parser_windows.add_argument('--except_focus', '-e', action='store_true', default=False, help='except the focused window when minimizing all windows in space')
    sub_parser_windows.add_argument('--full_screen', '-f', action='store_true', default=False, help='full screen all windows when deminimizing all windows in space')
    sub_parser_windows.add_argument('--left_focus', '-l', action='store_true', default=False, help='left focus the last focused window when minimizing all windows in space')
    
    sub_parser_space = subparsers.add_parser('space', help='toggle space layout')
    sub_parser_space.add_argument('--toggle', '-t', action='store_true', default=False, help='toggle space layout')
    sub_parser_space.add_argument('--float2max', '-mx', action='store_true', default=False, help='flotating windows to max when toggling space layout')

    args = parser.parse_args()

    # GUI commands
    if args.startGUI:
        mgr = YabaiManager()
        mgr.run()

    if args.quitGUI:
        utils.send_quit_single()

    if args.restartGUI:
        utils.send_quit_single()
        mgr = YabaiManager()
        mgr.run()

    # windows commands
    if args.command == 'windows':
        if args.deminimize:
            utils.deminimize_all_windows_in_space(args.refocus, args.full_screen)
        if args.minimize:
            utils.minimize_all_windows_in_space(args.except_focus, args.left_focus)

    # space commands
    if args.command == 'space':
        if args.toggle:
            utils.toggle_space_layout(args.float2max)

if __name__ == '__main__':
    main()
