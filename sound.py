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

if __name__ == "__main__":
    short_beep()
    long_beep()