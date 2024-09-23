import pygame
import pydub
import sys

# Initialize Pygame
pygame.init()

# Set window dimension
screen = pygame.display.set_mode((800, 600))

# Load instrument samples
instruments = [
    pydub.AudioSegment.from_file("sources/guitar.wav"),
    pydub.AudioSegment.from_file("sources/piano.wav"),
    pydub.AudioSegment.from_file("sources/drums.wav")
]
current_instrument_index = 0

# Function to play the instrument sounds
def play_instrument(frequency_multiplier):
    instrument = instruments[current_instrument_index]
    
    # Change the tone of the sound
    new_sound = instrument._spawn(instrument.raw_data, overrides={
        "frame_rate": int(instrument.frame_rate * frequency_multiplier)
    }).set_frame_rate(instrument.frame_rate)
    
    # Convert in a formtat compatible with Pygame
    new_sound.export("sources/temp.wav", format="wav")
    pygame.mixer.music.load("sources/temp.wav")
    pygame.mixer.music.play()

# Parameters
base_frequency = 1.0  # Frequency multiplier

# Playing loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Cycle over instruments at mouse click
            current_instrument_index = (current_instrument_index + 1) % len(instruments)

    # Get the mouse position
    mouse_x, _ = pygame.mouse.get_pos()
    
    # Find the new multiplier based on the frequency
    frequency_multiplier = 1 + (mouse_x / 800)  # Changeable from 1 to 2

    # Play the sound of the active instrument
    play_instrument(frequency_multiplier)

    # Wait a bit before playing the sound
    pygame.time.delay(100)
