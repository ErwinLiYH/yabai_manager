#!/usr/bin/env /opt/homebrew/Caskroom/miniconda/base/bin/python

import subprocess
import rumps
import socket
import threading
import sys
from utils import get_info, full_screen_all_windows_in_space


IP = 'localhost'
PORT = 22118

# init rumps app to show the space info
class YabaiManager(rumps.App):
    def __init__(self):
        info = get_info()
        super(YabaiManager, self).__init__(name="yabai menager", title=info)
        threading.Thread(target=self.listen_to_yabai, daemon=True).start()

    def listen_to_yabai(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((IP, PORT))
        s.listen(2)

        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            data = conn.recv(1)
            message = data.decode('utf-8')
            print('Received', message)
            conn.close()
            if message == 'u':
                print('update title')
                self.update_title()
            elif message == 'q':
                print('quit APP')
                sys.exit(1)
            else:
                print('unknown message, quit APP')
                sys.exit(1)

    def update_title(self):
        info = get_info()
        self.title = info

    def send_update_single(self):
        subprocess.run(f'echo "u" | nc {IP} {PORT}', shell=True)

    @rumps.clicked("Toggle space to float")
    def toggle_space_to_float(self, _):
        subprocess.run(['yabai', '-m', 'space', '--layout', 'float'])
        full_screen_all_windows_in_space()
        self.send_update_single()

    @rumps.clicked("Toggle space to bsp")
    def toggle_space_to_bsp(self, _):
        subprocess.run(['yabai', '-m', 'space', '--layout', 'bsp'])
        self.send_update_single()

if __name__ == '__main__':
    mgr = YabaiManager()
    mgr.run()