# PicoMorse (Sound version)
# By MrBeam89_
# Made only for Raspberry Pi Pico

from time import sleep
import array
import math
import board
import audiobusio
import audiocore

audio = audiobusio.I2SOut(board.GP10, board.GP11, board.GP9) # Specific to Pimoroni Audio Pack, but you can change this to connect whatever speaker you want

tone_volume = 0.2  # Increase this to increase the volume of the tone.
frequency = 200  # Set this to the Hz of the tone you want to generate.
length = 8000 // frequency
sine_wave = array.array("h", [0] * length)
for i in range(length):
    sine_wave[i] = int((math.sin(math.pi * 2 * i / length)) * tone_volume * (2 ** 15 - 1))
sine_wave_sample = audiocore.RawSample(sine_wave)

# International Morse code standard durations
unit = 0.2 # Change unit to slow down or speed up
dot_duration = unit
dash_duration = 3*unit
inter_element_gap = unit
letter_gap = 3*unit
word_gap = 7*unit

morse_code = {
    "a" : ["dot", "dash"],
    "b" : ["dash","dot","dot","dot"],
    "c" : ["dash","dot","dash","dot"],
    "d" : ["dash","dot","dot"],
    "e" : ["dot"],
    "f" : ["dot","dot","dash","dot"],
    "g" : ["dash","dash","dot"],
    "h" : ["dot","dot","dot","dot"],
    "i" : ["dot","dot"],
    "j" : ["dot","dash","dash","dash"],
    "k" : ["dash","dot","dash"],
    "l" : ["dot","dash","dot","dot"],
    "m" : ["dash","dash"],
    "n" : ["dash","dot"],
    "o" : ["dash","dash","dash"],
    "p" : ["dot","dash","dash","dot"],
    "q" : ["dash","dash","dot","dash"],
    "r" : ["dot","dash","dot"],
    "s" : ["dot","dot","dot"],
    "t" : ["dash"],
    "u" : ["dot","dot","dash"],
    "v" : ["dot","dot","dot","dash"],
    "w" : ["dot","dash","dash"],
    "x" : ["dash","dot","dot","dash"],
    "y" : ["dash","dot","dash","dash"],
    "z" : ["dash","dash","dot","dot"],
    "1" : ["dot","dash","dash","dash","dash"],
    "2" : ["dot","dot","dash","dash","dash"],
    "3" : ["dot","dot","dot","dash","dash"],
    "4" : ["dot","dot","dot","dot","dash"],
    "5" : ["dot","dot","dot","dot","dot"],
    "6" : ["dash","dot","dot","dot","dot"],
    "7" : ["dash","dash","dot","dot","dot"],
    "8" : ["dash","dash","dash","dot","dot"],
    "9" : ["dash","dash","dash","dash","dot"],
    "0" : ["dash","dash","dash","dash","dash"]
}

# Audio switch
def read(input):
    for element in morse_code[input]:
        if element == "dot":
            audio.play(sine_wave_sample, loop=True)
            sleep(dot_duration)
            audio.stop()
        elif element == "dash":
            audio.play(sine_wave_sample, loop=True)
            sleep(dash_duration)
            audio.stop()
        sleep(inter_element_gap)

# Read file content
file_path = "text.txt"
try:
    with open(file_path, "r") as file:
        file_contents = file.read().lower()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")
    
# Main loop
for char in file_contents:
    if char == " ": sleep(word_gap)
    else: read(char)
