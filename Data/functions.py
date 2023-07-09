import sys, time
from pygame.mixer import Sound


def play_bgm():
    bgm = Sound('Data/audio/bgm.mp3')
    bgm.set_volume(0.2)
    bgm.play(loops=-1, maxtime=0, fade_ms=0)

def classic_click():
    click = Sound('Data/audio/classic_click.wav')
    click.play(loops=0, maxtime=0, fade_ms=0)

def defeat(score):
    defeat = Sound('Data/audio/defeat.wav')
    defeat.play(loops=0, maxtime=0, fade_ms=0)
    print(f"\rDEFEAT Score:{score}")
    time.sleep(3.5)
    sys.exit()

def victory():
    victory = Sound('Data/audio/victory.wav')
    victory.play(loops=0, maxtime=0, fade_ms=0)
    print("\rVICTORY")
    time.sleep(1.5)
    sys.exit()

def score_board(score):
    print('\r', score, end='', flush=True)

def timer():
    pass
