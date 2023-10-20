import json, sys, time, tkinter
from pygame.mixer import Sound


def play_bgm():
    bgm = Sound('Data/audio/bgm.mp3')
    bgm.set_volume(0.5)
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

def victory(game_time, difficulty):
    victory = Sound('Data/audio/victory.wav')
    victory.play(loops=0, maxtime=0, fade_ms=0)
    difficulty = difficulty.title()
    game_time = round(game_time, 2)
    print(f"\rVICTORY Difficulty:{difficulty} Time:{game_time}s")
    with open('Data/scores.json', encoding = 'utf-8') as scores:
        s = json.load(scores)
    if s["best_score"]["classic"][difficulty] < game_time:
        s["best_score"]["classic"][difficulty] = game_time
        with open('Data/scores.json', mode='w', encoding = 'utf-8') as scores:
            json.dump(s, scores)
    best_score = s["best_score"]["classic"][difficulty]
    print(f"BestScore:{best_score}s ({difficulty})")
    time.sleep(1.5)
    sys.exit()

def clear_score_list():
    with open('Data/scores.json', encoding = 'utf-8') as scores:
        s = json.load(scores)
    s["best_score"]["classic"]["Easy"] = 0
    s["best_score"]["classic"]["Normal"] = 0
    s["best_score"]["classic"]["Hard"] = 0
    s["best_score"]["classic"]["Insane"] = 0
    with open('Data/scores.json', mode='w', encoding = 'utf-8') as scores:
        json.dump(s, scores)
    print('--The highest score has been reset--.')

def score_board(score, total_score):
    print('\r', f"{score}/{total_score}", end='', flush=True)

def timer():
    pass

def about():
    window = tkinter.Tk()
    window.title("About")
    window.geometry("350x200")
    lbl = tkinter.Label(window, text="Version: v1.0")
    lbl.pack(anchor="nw")
    lbl = tkinter.Label(window, text="@MZS_2023 Copyright")
    lbl.pack(anchor="nw")
