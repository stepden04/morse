import winsound
import time

FREQ = 500
BEEP_SOUND = 150

def short_beep():
    winsound.Beep(FREQ, BEEP_SOUND)

def long_beep():
    winsound.Beep(FREQ,BEEP_SOUND*3)

def pause():
    time.sleep(BEEP_SOUND*7)

def signal(morse: str):
    # if LETTERS_MORSE == .:
    #   short_beep()

    # if MORSE_LETTERS == -:
    #   long_beep()

    for char in morse:
        ...


if __name__ == "__main__":
    signal(".... . .-.. .-.. ---  .-- --- .-. .-.. -..")
    # short_beep()
    # long_beep()