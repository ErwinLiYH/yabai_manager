import rumps
import socket
import threading
import Kkit
from . import LOGGER
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
        s.listen(10)

        while True:
            LOGGER.info('Waiting for connection')
            conn, addr = s.accept()
            LOGGER.info('Connected by', addr)
            data = conn.recv(1)
            message = data.decode('utf-8')
            LOGGER.info('Received', message)
            conn.close()
            if message == 'u':
                self.update_title()
            elif message == 'q':
                rumps.quit_application()
            else:
                rumps.quit_application()

    @Kkit.retry(3, record=LOGGER)
    def update_title(self):
        info = get_info()
        self.title = info

    @rumps.clicked("Toggle space layout")
    def toggle_space_to_float(self, _):
        toggle_space_layout()

    @rumps.clicked("Deminimize all windows")
    def deminimize_all_windows(self, _):
        res = deminimize_all_windows_in_space()
        if res:
            rumps.notification("Deminimize all windows and refocus", "No originally focused window", "When deminimize all windows and refocus to original window, No originally focused window to refocus.")

    @rumps.clicked("Minimize unfocused windows")
    def minimize_all_windows(self, _):
        minimize_all_windows_in_space()

if __name__ == '__main__':
    mgr = YabaiManager()
    mgr.run()