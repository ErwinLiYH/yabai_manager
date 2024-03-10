import rumps
import socket
import threading
import sys
from .utils import get_info, toggle_space_layout, IP, PORT,\
minimize_all_windows_in_space, deminimize_all_windows_in_space


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
                rumps.quit_application()
            else:
                print('unknown message, quit APP')
                rumps.quit_application()

    def update_title(self):
        info = get_info()
        self.title = info

    @rumps.clicked("Toggle space layout")
    def toggle_space_to_float(self, _):
        toggle_space_layout()

    @rumps.clicked("Deminimize all windos")
    def deminimize_all_windows(self, _):
        deminimize_all_windows_in_space()

    @rumps.clicked("Minimize all windows")
    def minimize_all_windows(self, _):
        minimize_all_windows_in_space()

if __name__ == '__main__':
    mgr = YabaiManager()
    mgr.run()