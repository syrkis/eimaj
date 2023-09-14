# Eimaj: AI-Based Scene Switching for OBS

## Overview

Eimaj is an AI-based scene switching application for OBS (Open Broadcast Software) that automatically switches between two scenes, based on hand presence and user input detection. It uses computer vision and machine learning techniques for effective and seamless transitions.

## Features

- Hand Detection: Eimaj uses the MediaPipe machine learning framework to detect the presence of hands in the webcam feed. If two hands are detected, Eimaj switches to a scene named 'webcam_scene' in OBS.
- Input Detection: Eimaj listens for mouse and keyboard inputs. If any such input is detected, Eimaj switches to a different scene named 'screen_scene' in OBS.
- Easy to Use: Eimaj presents a simple menu interface for starting the scene-switching service. Once started, Eimaj runs quietly in the background, monitoring the webcam feed and user inputs, and switches scenes in OBS accordingly.

## Requirements

You need the following software and libraries installed to run Eimaj:
- Python 3.7 or newer
- OpenCV
- MediaPipe
- obs-websocket-py
- pynput
- rumps
You can install most of these libraries using pip:
pip install opencv-python-headless mediapipe obs-websocket-py pynput rumps
Also, you need to have OBS Studio with the WebSocket plugin installed for Eimaj to control scene switching.

## Configuration

You need to configure OBS Websocket settings (server address and password) to match yours in the ﻿get_obs function.
Default configuration:
ws = obsws('localhost', 4445, password='123456')

## Usage

Start the application by running the ﻿main.py file:
python main.py
Once started, click on the 'Start' option in the Eimaj app menu on your system's menu bar. The app will now start monitoring for hand presence in the webcam feed and user inputs.
As per the currently active scene in OBS, Eimaj will switch between 'webcam_scene' (when two hands are detected and there's no user input) and 'screen_scene' (when there's a user input).
Note
- Please make sure that you have the corresponding scenes (i.e., 'webcam_scene' and 'screen_scene') set up in OBS.
- OBS Studio must be running for the scene-switching functionality to work.

## License

This project is licensed under the MIT License.