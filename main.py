# eimaj.py
#   ai based scence switching for obs
# by: Noah Syrkis

# imports
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2
import threading
import mediapipe as mp
from obswebsocket import obsws, requests
import time
from pynput import keyboard, mouse
import rumps


# app
class App(rumps.App):

    def __init__(self):
        super(App, self).__init__('eimaj')
        self.menu = ['Start']
        self.input_detected = False
        self.control_loop = threading.Thread(target=self.control_loop)
    
    @rumps.clicked("Start")
    def start(self, _):
        # Start the control loop when 'Start' button is clicked
        self.ws = get_obs()
        self.hands = mp.solutions.hands.Hands()
        self.cam = cv2.VideoCapture(0)
        self.listeners = self.start_listeners()
        if not self.control_loop.is_alive():
            # start the thread if it is not running
            self.control_loop.start()

    def control_loop(self):
        while True:
            frame = self.capture()
            if self.has_hands(frame) and not self.input_detected:
                self.ws.call(requests.SetCurrentProgramScene(sceneName='webcam_scene'))
            if self.input_detected:
                self.ws.call(requests.SetCurrentProgramScene(sceneName='screen_scene'))
                self.input_detected = False
            time.sleep(1)

    def start_listeners(self):
        mouse_listener = mouse.Listener(on_move=self.on_input, on_click=self.on_input, on_scroll=self.on_input)
        mouse_listener.start()
        time.sleep(1)
        keyboard_listener = keyboard.Listener(on_press=self.on_input)
        keyboard_listener.start()
        return mouse_listener, keyboard_listener


    def on_input(self, *args):
        self.input_detected = True

    def capture(self):
        ret, frame = self.cam.read()
        while frame.sum() == 0:
            _, frame = self.cam.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame_rgb

    def has_hands(self, frame):
        results = self.hands.process(frame).multi_hand_landmarks
        return results is not None and len(results) >= 2

    def on_quit(self, _):
        self.ws.disconnect()
        self.cam.release()
        cv2.destroyAllWindows()
        rumps.quit_application()


def get_obs():
    # add code to test if obs is running
    ws = obsws('localhost', 4445, password='123456')
    ws.connect()
    return ws


# main
def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
