import pygame
import pydub
import sys
import os

# Use PulseAudio to route sound to the host system
os.environ["SDL_AUDIODRIVER"] = "pulseaudio"

# Initialize Pygame and the mixer
pygame.init()

# Set up the audio buffer (optional, but helps in environments like Docker)
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

# Set the window dimensions
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sound Instrument Player")

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
    
    # Change the pitch of the sound
    new_sound = instrument._spawn(instrument.raw_data, overrides={
        "frame_rate": int(instrument.frame_rate * frequency_multiplier)
    }).set_frame_rate(instrument.frame_rate)
    
    # Export the modified sound to a format compatible with Pygame
    new_sound.export("sources/temp.wav", format="wav")
    
    # Load and play the audio file with Pygame
    pygame.mixer.music.load("sources/temp.wav")
    pygame.mixer.music.play()

# Initial parameters
base_frequency = 1.0  # Frequency multiplier

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Cycle through instruments on mouse click
            current_instrument_index = (current_instrument_index + 1) % len(instruments)

    # Get the mouse position
    mouse_x, _ = pygame.mouse.get_pos()
    
    # Calculate the frequency multiplier based on the mouse position
    frequency_multiplier = 1 + (mouse_x / 800)  # Adjustable from 1 to 2

    # Play the sound of the active instrument
    play_instrument(frequency_multiplier)

    # Add a brief pause before playing the next sound
    pygame.time.delay(200)  # Increased to 200ms for better loop management
