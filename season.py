import sys
import random
from game import Game, play_games, play_series

class Season:
    def __init__(self, E1, E2, E3, E4, E5, E6, E7, E8, W1, W2, W3, W4, W5, W6, W7, W8):
        self.E1 = E1
        self.E2 = E2
        self.E3 = E3
        self.E4 = E4
        self.E5 = E5
        self.E6 = E6
        self.E7 = E7
        self.E8 = E8
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3
        self.W4 = W4
        self.W5 = W5
        self.W6 = W6
        self.W7 = W7
        self.W8 = W8

def play_season(season, shift, win, index):
    #round 1
    east1A = Game(season.E1, season.E8)
    #E1A = play_games(east1A, 0, 0, 0, shift)
    E1A = play_series(east1A, 0, shift)
    east1B = Game(season.E2, season.E7)
    #E1B = play_games(east1B, 0, 0, 0, shift)
    E1B = play_series(east1B, 0, shift)
    east1C = Game(season.E3, season.E6)
    #E1C = play_games(east1C, 0, 0, 0, shift)
    E1C = play_series(east1C, 0, shift)
    east1D = Game(season.E4, season.E5)
    #E1D = play_games(east1D, 0, 0, 0, shift)
    E1D = play_series(east1D, 0, shift)


    west1A = Game(season.W1, season.W8)
    #W1A = play_games(west1A, 0, 0, 0, shift)
    W1A = play_series(west1A, 0, shift)
    west1B = Game(season.W2, season.W7)
    #W1B = play_games(west1B, 0, 0, 0, shift)
    W1B = play_series(west1B, 0, shift)
    west1C = Game(season.W3, season.W6)
    #W1C = play_games(west1C, 0, 0, 0, shift)
    W1C = play_series(west1C, 0, shift)
    west1D = Game(season.W4, season.W5)
    #W1D = play_games(west1D, 0, 0, 0, shift)
    W1D = play_series(west1D, 0, shift)

    #round 2
    east2A = Game(E1A, E1D)
    #E2A = play_games(east2A, 0, 0, 0, shift)
    E2A = play_series(east2A, 0, shift)
    east2B = Game(E1B, E1C)
    #E2B = play_games(east2B, 0, 0, 0, shift)
    E2B = play_series(east2B, 0, shift)

    west2A = Game(W1A, W1D)
    #W2A = play_games(west2A, 0, 0, 0, shift)
    W2A = play_series(west2A, 0, shift)
    west2B = Game(W1B, W1C)
    #W2B = play_games(west2B, 0, 0, 0, shift)
    W2B = play_series(west2B, 0, shift)

    #round 3
    east3 = Game(E2A, E2B)
    #E3 = play_games(east3, 0, 0, 0, shift)
    E3 = play_series(east3, 0, shift)
    west3 = Game(W2A, W2B)
    #W3 = play_games(west3, 0, 0, 0, shift)
    W3 = play_series(west3, 0, shift)

    #finals
    W3 = season.W8
    final = Game(E3, W3)
    #champion = play_games(final, 1, 0, 0, shift)
    #champion = play_series(final, 1, shift)
    if (win == 1):
        champion = play_games(final, 0, index, 0, shift)
    else:
        champion = play_games(final, 0, 0, index, shift)
    return champion

