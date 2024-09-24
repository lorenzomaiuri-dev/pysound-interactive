[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Interactive Musical Instruments

## Description

This project allows users to play sounds from various musical instruments interactively. Users can modify the pitch of the sound by moving the mouse and switch instruments by clicking.

## Features

- Playback of guitar, piano, and drum sounds.
- Pitch adjustment based on mouse position.
- Cyclical switching between different musical instruments with each mouse click.

## Requirements

- Python 3.x
- The following Python libraries:
  - `pygame`
  - `pydub`

## Installation

1. Clone this repository:

   ```bash
    git clone https://github.com/lorenzomaiuri-dev/pysound-interactive.git
    cd pysound-interactive
2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv

    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate  # On Windows
3. Install the dependencies

    ```bash
    pip install -r requirements.txt
4. Make sure you have ffmpeg or libav installed to handle audio files

    You can install them using your operating system's package manager

5. Add audio files:

    Ensure you have the following audio files in the 'sources' folder:

- guitar.wav
- piano.wav
- drums.wav

## Usage

1. Run the program:

    ```bash
    python main.py
2. Move the mouse to adjust the pitch of the sound

3. Click the mouse to switch instruments

## Docker Usage

This project can also be run using Docker. Follow the steps below:

### Prerequisites

- Ensure you have [Docker](https://www.docker.com/) installed on your machine.

### Building the Docker Image

1. Clone this repository:

   ```bash
    git clone https://github.com/lorenzomaiuri-dev/pysound-interactive.git
    cd pysound-interactive
2. Build the Docker image with the following command:

   ```bash
   docker build -t pysound-interactive .
3. Run the Docker container:

    ```bash
    xhost +local:root  # On linux allow access to X11 display for local root user

    docker run -it \
    --env="DISPLAY" \
    --env="PULSE_SERVER=unix:/run/user/$(id -u)/pulse/native" \
    --volume="/run/user/$(id -u)/pulse/native:/run/user/$(id -u)/pulse/native" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="$HOME/.config/pulse/cookie:/root/.config/pulse/cookie" \
    --device /dev/snd \
    --env="SDL_VIDEODRIVER=x11" \
    -p 8000:8000 \
    pysound-interactive  # on Linux
    
    docker run -it \
    --gpus all \
    --env DISPLAY=host.docker.internal:0 \
    -p 8000:8000 \
        docker run -it --rm pysound-interactive # on WSL

## Contributing

If you would like to contribute to this project, feel free to open an issue or submit a pull request

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](./LICENSE) file for more details

<!-- LINKS & IMAGES -->
[stars-shield]: https://img.shields.io/github/stars/lorenzomaiuri-dev/pysound-interactive?style=social
[stars-url]: https://github.com/lorenzomaiuri-dev/pysound-interactive/stargazers
[license-shield]: https://img.shields.io/badge/license-GPL--3.0-blue.svg
[license-url]: https://www.gnu.org/licenses/gpl-3.0.html
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white
[linkedin-url]: https://it.linkedin.com/in/lorenzo-maiuri-9a7472244
