# OBS Scene Switcher with Dynamic Monitoring

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python application offers a new way to interact with your OBS setup, providing a more dynamic and natural user experience. Using advanced neural network algorithms, the app constantly analyzes your webcam feed to detect the presence of both hands. When two hands are visible, it automatically switches to the webcam view in OBS. Additionally, the app monitors for trackpad or keyboard inputs to switch back to screen recording when necessary.

## Requirements

- Python 3.11
- OBS Studio
- Web camera

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Run `pip install -r requirements.txt`.

## Usage

Run the application using the following command:

```bash
python main.py
```

## Features

- **Dynamic Scene Switching**: Say goodbye to manual scene switching. Make your presentations and broadcasts more interactive.
- **Neural Network Analysis**: Sophisticated algorithms ensure accurate hand detection for seamless scene transitions.
- **Input Monitoring**: Automatically revert to your screen recording when keyboard or trackpad activity is detected.

## Technologies

- Python 3.11
- Neural Networks
- OBS Studio API

## Contributing

If you find a bug or want to contribute to the development of this application, feel free to open an issue or submit a pull request. Currently only works on MacOS.

## License

MIT License
