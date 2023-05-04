import sys
import math
import random
import numpy as np
from team import Team
from season import Season, play_season
from game import Game, playin_game
if __name__ == "__main__":
    #no play in 2-2-1-1-1
    dist1 = [(1700.6859351625826, 131.19180701190965), (1705.236974027424, 158.51151585357522), 
    (1636.8692706139573, 109.59288834396588), (1589.6290496719548, 85.23851833889245), 
    (1528.4808852672109, 77.57296166701951), (1487.022790245591, 74.38241324713641), 
    (1487.575328171612, 63.66327456521548), (1456.3506316916487, 53.51489998848491), 
    (1775.4306555901858, 185.21027708213643), (1686.238691908711, 140.3360481810979), 
    (1618.4509140064188, 109.30208020343393), (1614.23898805305, 107.25814898675763), 
    (1580.7971136010342, 89.09025555045471), (1543.5761487236032, 82.0510095932112), 
    (1505.0105015280026, 86.30609191617454), (1495.3793444382843, 50.33546031446618)]
    #play in 2-2-1-1-1
    dist2 = [(1692.389543656258, 132.98551081864593), (1700.1558126096395, 158.5202100989468), 
    (1636.1274910728976, 108.63911612230561), (1589.5124098476194, 85.17621968845654), 
    (1529.221899546, 77.85501951286945), (1487.6369256068035, 74.27877415862834), 
    (1505.0678381704465, 68.10017701190066), (1489.6469602923576, 87.0645012985579), 
    (1770.2531389560459, 186.78145974979512), (1679.50132858381, 138.68070168413826), 
    (1619.621016708503, 108.62462669284855), (1615.8829332262692, 108.82365144522456), 
    (1579.9060202818018, 87.71968160192765), (1544.040567443969, 82.91432830834665), 
    (1538.3500133199584, 82.5006860795304), (1512.538828511587, 77.76812152517361)]
    #play in 2-3-2
    dist3 = [(1686.5297051795033, 132.23765492764284), (1695.7154645569253, 158.01788295249742), 
    (1634.7786597164943, 110.89673485819466), (1587.035882518899, 86.07204302253908), 
    (1533.9813689844868, 81.02319290191451), (1491.5840100036944, 77.1404652261145), 
    (1508.3606503937576, 71.28968760529864), (1492.4676471779997, 89.5540820023258), 
    (1760.9534893866985, 184.9573345204897), (1673.849505613389, 138.8281674753076), 
    (1617.537051801657, 109.71396719748067), (1612.7609002639933, 109.10895028276536), 
    (1586.5600051776894, 92.73904177784193), (1547.8343946549246, 84.60886233105248), 
    (1543.0198680161266, 86.7662176894334), (1515.8910347991782, 81.07088441256863)]
    winsDist = [55.625, 53.625, 50, 48, 45.875, 43.75, 41.5, 40.125, 
    60.375, 55.875, 50.75, 49.125, 46.5, 45.5, 44.25, 41.875]
    ct0 = 0
    i = 0
    while i < 25000:
        #print(i)
        noPlayInDist = []
        for x in dist1:
            noPlayInDist.append(np.random.normal(x[0], x[1], 1)[0])
        E1 = Team("E1", noPlayInDist[0], 1, winsDist[0])
        E2 = Team("E2", noPlayInDist[1], 2, winsDist[1])
        E3 = Team("E3", noPlayInDist[2], 3, winsDist[2])
        E4 = Team("E4", noPlayInDist[3], 4, winsDist[3])
        E5 = Team("E5", noPlayInDist[4], 5, winsDist[4])
        E6 = Team("E6", noPlayInDist[5], 6, winsDist[5])
        E7 = Team("E7", noPlayInDist[6], 7, winsDist[6])
        E8 = Team("E8", noPlayInDist[7], 8, winsDist[7])
        W1 = Team("W1", noPlayInDist[8], 1, winsDist[8])
        W2 = Team("W2", noPlayInDist[9], 2, winsDist[9])
        W3 = Team("W3", noPlayInDist[10], 3, winsDist[10])
        W4 = Team("W4", noPlayInDist[11], 4, winsDist[11])
        W5 = Team("W5", noPlayInDist[12], 5, winsDist[12])
        W6 = Team("W6", noPlayInDist[13], 6, winsDist[13])
        W7 = Team("W7", noPlayInDist[14], 7, winsDist[14])
        W8 = Team("W8", noPlayInDist[15], 8, winsDist[15])
        season = Season(E1, E2, E3, E4, E5, E6, E7, E8, W1, W2, W3, W4, W5, W6, W7, W8)
        y = play_season(season, 0)
        if (y == False):
            continue
        elif (y.name == W8.name):
            ct0+=1
            i+=1
        else:
            i+=1
    print(ct0/25000)
    ct1 = 0
    i = 0
    while i < 25000:
        #print(i)
        playInDist = []
        for x in dist2:
            playInDist.append(np.random.normal(x[0], x[1], 1)[0])
        E1 = Team("E1", playInDist[0], 1, winsDist[0])
        E2 = Team("E2", playInDist[1], 2, winsDist[1])
        E3 = Team("E3", playInDist[2], 3, winsDist[2])
        E4 = Team("E4", playInDist[3], 4, winsDist[3])
        E5 = Team("E5", playInDist[4], 5, winsDist[4])
        E6 = Team("E6", playInDist[5], 6, winsDist[5])
        E7 = Team("E7", playInDist[6], 7, winsDist[6])
        E8 = Team("E8", playInDist[7], 8, winsDist[7])
        W1 = Team("W1", playInDist[8], 1, winsDist[8])
        W2 = Team("W2", playInDist[9], 2, winsDist[9])
        W3 = Team("W3", playInDist[10], 3, winsDist[10])
        W4 = Team("W4", playInDist[11], 4, winsDist[11])
        W5 = Team("W5", playInDist[12], 5, winsDist[12])
        W6 = Team("W6", playInDist[13], 6, winsDist[13])
        W7 = Team("W7", playInDist[14], 7, winsDist[14])
        W8 = Team("W8", playInDist[15], 8, winsDist[15])
        season = Season(E1, E2, E3, E4, E5, E6, E7, E8, W1, W2, W3, W4, W5, W6, W7, W8)
        y = play_season(season, 0)
        if (y == False):
            continue
        elif (y.name == E1.name):
            ct1+=1
            i+=1
        else:
            i+=1
    print(ct1/25000)
    for j in range(1,8):
        for k in range(0,2):
            ct2 = 0
            i = 0
            while i < 25000:
                #print(i)
                newDist = []
                for x in dist3:
                    newDist.append(np.random.normal(x[0], x[1], 1)[0])
                E1 = Team("E1", newDist[0], 1, winsDist[0])
                E2 = Team("E2", newDist[1], 2, winsDist[1])
                E3 = Team("E3", newDist[2], 3, winsDist[2])
                E4 = Team("E4", newDist[3], 4, winsDist[3])
                E5 = Team("E5", newDist[4], 5, winsDist[4])
                E6 = Team("E6", newDist[5], 6, winsDist[5])
                E7 = Team("E7", newDist[6], 7, winsDist[6])
                E8 = Team("E8", newDist[7], 8, winsDist[7])
                W1 = Team("W1", newDist[8], 1, winsDist[8])
                W2 = Team("W2", newDist[9], 2, winsDist[9])
                W3 = Team("W3", newDist[10], 3, winsDist[10])
                W4 = Team("W4", newDist[11], 4, winsDist[11])
                W5 = Team("W5", newDist[12], 5, winsDist[12])
                W6 = Team("W6", newDist[13], 6, winsDist[13])
                W7 = Team("W7", newDist[14], 7, winsDist[14])
                W8 = Team("W8", newDist[15], 8, winsDist[15])
                season = Season(E1, E2, E3, E4, E5, E6, E7, E8, W1, W2, W3, W4, W5, W6, W7, W8)
                y = play_season(season, 0, k, j)
                if (y == False):
                    continue
                elif (y.name == W8.name):
                    ct2+=1
                    i+=1
                else:
                    i+=1
            print(ct2/25000)


