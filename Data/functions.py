from pygame.mixer import Sound


def play_bgm():
    bgm = Sound('Data/audio/bgm.mp3')
    bgm.set_volume(0.2)
    bgm.play(loops=-1, maxtime=0, fade_ms=0)

def classic_click():
    click = Sound('Data/audio/classic_click.wav')
    click.play(loops=0, maxtime=0, fade_ms=0)

def defeat():
    defeat = Sound('Data/audio/defeat.wav')
    defeat.play(loops=0, maxtime=0, fade_ms=0)
