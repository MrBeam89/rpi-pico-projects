# rpi-pico-projects
Random stuff with the Raspberry Pi Pico
## Python scripts
I recommend **Thonny** since it's the easiest to use (for me, at least). Check it out [here](https://thonny.org).

You can install MicroPython and CircuitPython directly from Thonny (see Setup Thonny).

### Setup Thonny
1. Plug your Raspberry Pi Pico while holding the BOOTSEL button to your computer and start Thonny.
2. Click on "Local Python 3 • Thonny's Python" and click "Install Micropython" or "Install CircuitPython".
3. Click on the dropdown menu beside "variant" and select whatever variant you need.
4. Click on the dropdown menu beside "version" and choose the latest version.
5. Click Install and wait until it's finished.
6. Now that MicroPython is installed, click again on "Local Python 3 • Thonny's Python"  and select "MicroPython (Raspberry Pi Pico)" or "CircuitPython (generic)".
7. Done!

### How to run Python scripts
* MicroPython : save your script as "main.py" in the root folder of the Raspberry Pi Pico
* CircuitPython : save your script as "code.py" in the root folder of the Raspberry Pi Pico

### Current projects
* PicoMorse (LED Version) *MicroPython* : outputs Morse code with the onboard LED on the Raspberry Pi Pico, place your text in a file named "text.txt" in the same directory as the script. Supports only alphanumeric characters!

And more coming sooner or later...
