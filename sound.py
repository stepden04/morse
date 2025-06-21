import winsound
import time

FREQ = 440
BEEP_SOUND = 100

def short_beep():
    winsound.Beep(FREQ, BEEP_SOUND)

def long_beep():
    winsound.Beep(FREQ,BEEP_SOUND*3)

def short_pause():
    time.sleep(BEEP_SOUND/1000*3)

def pause():
    time.sleep(BEEP_SOUND*7/1000)

def signal(morse: str):
    # if LETTERS_MORSE == .:
    #   short_beep()

    # if MORSE_LETTERS == -:
    #   long_beep()

    for char in morse:
        if char == '.' :
            short_beep()

        if char == '-' :
            long_beep()

        if char == '@':
            pause()

        if char == ' ':
            short_pause()


if __name__ == "__main__":
    signal(".... . .-.. .-.. ---  .-- --- .-. .-.. -..")
    # short_beep()
    # long_beep()