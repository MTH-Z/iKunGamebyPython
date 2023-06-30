import pygame.mixer


def play_bgm():
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.music.load('Data/audio/bgm.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(loops=-1, start=0.0)
