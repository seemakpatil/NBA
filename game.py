import sys
import math
import random
import numpy
import scipy.stats as stats
from team import Team

class Game:
    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        
    def elo_diff(self, teamA, teamB, homeTeam): #homeTeam is 1 if A, 0 if B
        return teamA.elo - teamB.elo + (-100 if homeTeam == 0 else 100)

    def prob_win(self, teamA, teamB, homeTeam):
        return 1/(math.pow(10, -self.elo_diff(teamA, teamB, homeTeam)/400) + 1)

    def bucket(self, eloDiff):
        mean, stdev = 0, 0
        data = [(-12.8245614, 12.30145579), (-6.306451613, 12.51699004), (-7.740740741, 14.27131648), 
        (-5.203821656, 14.62555669), (-4.348837209, 14.6855856), (-1.388429752, 14.98853556)]
        if (eloDiff < -225):
            mean = data[0][0]
            stdev = data[0][1]
        elif (eloDiff < -180):
            mean = data[1][0]
            stdev = data[1][1]
        elif (eloDiff < -135):
            mean = data[2][0]
            stdev = data[2][1]
        elif (eloDiff < -90):
            mean = data[3][0]
            stdev = data[3][1]
        elif (eloDiff < -45):
            mean = data[4][0]
            stdev = data[4][1]
        elif (eloDiff < 0):
            mean = data[5][0]
            stdev = data[5][1]
        elif (eloDiff < 45):
            mean = -data[5][0]
            stdev = data[5][1]
        elif (eloDiff < 90):
            mean = -data[4][0]
            stdev = data[4][1]
        elif (eloDiff < 135):
            mean = -data[3][0]
            stdev = data[3][1]
        elif (eloDiff < 180):
            mean = data[2][0]
            stdev = data[2][1]
        elif (eloDiff < 225):
            mean = -data[1][0]
            stdev = data[1][1]
        else:
            mean = -data[0][0]
            stdev = data[0][1]
        lower, upper = 0, numpy.inf
        X = stats.truncnorm((lower - mean) / stdev, (upper - mean) / stdev, loc=mean, scale=stdev)
        return X.rvs(1)

    def elo_shift(self, winner, loser, homeTeam):
        eloDiff = self.elo_diff(winner, loser, homeTeam)
        mov = self.bucket(eloDiff)
        shift = 20*((mov+3)**0.8)/(7.5 + 0.006*eloDiff)
        winner.elo += shift
        loser.elo -= shift

def playin_game(game, winTest, loseTest, shift): #winTest 1 means team A wins, loseTest 1 means team B wins
    home = 0 if game.teamA.rank > game.teamB.rank else 1
    winProb = game.prob_win(game.teamA, game.teamB, home)

    if winTest == 1:
        game.elo_shift(game.teamA, game.teamB, home)
        return game.teamA, game.TeamB
    elif loseTest == 1:
        game.elo_shift(game.teamB, game.teamA, 1-home)
        return game.teamB, game.teamA
    elif random.random() <= winProb: #then team A wins
        game.elo_shift(game.teamA, game.teamB, home)
        return game.teamA, game.teamB
    else:
        game.elo_shift(game.teamB, game.teamA, 1-home)
        return game.teamB, game.teamA

def play_series(game, finals, shift):
    home = 0
    if (finals == 1): #1 means A is home, 0 means not
        home = 1 if game.teamA.wins > game.teamB.wins else 0
    else:
        home = 1 if game.teamA.rank < game.teamB.rank else 0

    if (home == 1):
        h = game.prob_win(game.teamA, game.teamB, 1)
        a = game.prob_win(game.teamA, game.teamB, 0)
    else:
        h = game.prob_win(game.teamB, game.teamA, 1)
        a = game.prob_win(game.teamB, game.teamA, 0)
    h1 = 1-h
    a1 = 1-a
    winProb = h*(a**3)*((h1**3) + 3*(h1**2)) + (h**2)*(a**2)*(1 + 2*h1 + 6*h1*a1 + 9*(h1**2)*a1) + \
    (h**3)*a*((a1**2) + 2*a1 + 9*h1*(a1**2)) + (h**4)*(a1**3)
    if (home == 0):
        winProb = 1-winProb
    if (random.random() <= winProb):
        return game.teamA
    else:
        return game.teamB


def play_games(game, finals, winTest, loseTest, shift): #test: 0 means no changes, if 1-7 then they win/lose that game
    winsA = 0
    winsB = 0
    start = 1
    hca = 0
    home = []
    if (finals == 1): # hca 1 means (winsA, winsB)
        hca = 1 if game.teamA.wins > game.teamB.wins else 0
    else:
        hca = 1 if game.teamA.rank < game.teamB.rank else 0

    if (hca == 1):
        h = game.prob_win(game.teamA, game.teamB, 1)
        a = game.prob_win(game.teamA, game.teamB, 0)
    else:
        h = game.prob_win(game.teamB, game.teamA, 1)
        a = game.prob_win(game.teamB, game.teamA, 0)
    h1 = 1-h
    a1 = 1-a
    if (winTest == 5 or loseTest == 5):
        start = 5
        score13 = 2*h*h1*(a1**2) + 2*a*a1*(h1**2)
        score22 = (h**2)*(a1**2) + 4*h*a*h1*a1 + (a**2)*(h1**2)
        score31 = 2*(h**2)*a*a1 + 2*h*(a**2)*h1
        total = score13 + score22 + score31
        p13 = score13/total
        p22 = score22/total + p13
        r = random.random()
        if (r <= p13):
            winsA = 1
            winsB = 3
        elif (r <= p22):
            winsA = 2
            winsB = 2
        else:
            winsA = 3
            winsB = 1

        if (hca == 0):
            temp = winsA
            winsA = winsB
            winsB = temp
    elif (winTest == 6 or loseTest == 6):
        start = 6
        #score23 = 3*(h**2)*h1*(a1**2) + 6*h*a*(h1**2)*a1 + (a**2)*(h1**3)
        #score32 = 3*h*(a**2)*(h1**2) + 6*(h**2)*a*h1*a1 + (h**3)*(a1**2)
        score23 = (h**2)*(a1**3) + 6*h*a*h1*(a1**2) + 3*(a**2)*(h1**2)*a1
        score32 = (a**3)*(h1**2) + 6*h*(a**2)*h1*a1 + 3*(h**2)*a*(a1**2)
        total = score23 + score32
        p23 = score23/total
        r = random.random()
        if (r <= p23):
            winsA = 2
            winsB = 3
        else:
            winsA = 3
            winsB = 2

        if (hca == 0):
            temp = winsA
            winsA = winsB
            winsB = temp
    elif (winTest == 7 or loseTest == 7):
        start = 7
        winsA = 3
        winsB = 3

    if (finals == 1): #1 means A is home, 0 means not
        #home = [1, 1, 0, 0, 1, 0, 1] if game.teamA.wins > game.teamB.wins else [0, 0, 1, 1, 0, 1, 0]
        home = [1, 1, 0, 0, 0, 1, 1] if game.teamA.wins > game.teamB.wins else [0, 0, 1, 1, 1, 0, 0]
    else:
        #home = [1, 1, 0, 0, 1, 0, 1] if game.teamA.rank < game.teamB.rank else [0, 0, 1, 1, 0, 1, 0]
        home = [1, 1, 0, 0, 0, 1, 1] if game.teamA.wins > game.teamB.wins else [0, 0, 1, 1, 1, 0, 0]
    
    for i in range(start,8):
        winProb = game.prob_win(game.teamA, game.teamB, home[i-1])
        if not shift:
            if i == winTest:
                winsA += 1
            elif i == loseTest:
                winsB += 1
            elif random.random() <= winProb: #then team A wins
                winsA += 1
            else:
                winsB += 1
        else:
            if i == winTest:
                game.elo_shift(game.teamA, game.teamB, home[i-1])
                winsA += 1
            elif i == loseTest:
                game.elo_shift(game.teamB, game.teamA, 1-home[i-1])
                winsB += 1
            elif random.random() <= winProb: #then team A wins
                game.elo_shift(game.teamA, game.teamB, home[i-1])
                winsA += 1
            else:
                game.elo_shift(game.teamB, game.teamA, 1-home[i-1])
                winsB += 1
        if winsA == 4:
            return game.teamA
        elif winsB == 4:
            return game.teamB