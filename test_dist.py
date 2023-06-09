import sys
import math
import random
import numpy as np
from team import Team
from season import Season, play_season
from game import Game, playin_game

if __name__ == "__main__":
    eloList = []
    playoffType = 1 #0 means no play in, 1 means play in
    for i in range(25000):
        print(i)
        E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, W1, W2, W3, W4, W5, W6, W7, W8, W9, W10 = (None,)*20
        r = random.randint(0, 7)
        if (r == 0):
            #2015-16
            E1 = Team("E1", 1642.356507, 1, 57)
            E2 = Team("E2", 1632.913283, 2, 56)
            E3 = Team("E3", 1579.871616, 3, 48)
            E4 = Team("E4", 1605.928624, 4, 48)
            E5 = Team("E5", 1573.581622, 5, 48)
            E6 = Team("E6", 1585.314466, 6, 48)
            E7 = Team("E7", 1519.049235, 7, 45)
            E8 = Team("E8", 1514.63454, 8, 44)
            E9 = Team("E9", 1453.750716, 9, 42)
            E10 = Team("E10", 1529.963754, 10, 41)
            W1 = Team("W1", 1788.472611, 1, 73)
            W2 = Team("W2", 1766.650681, 2, 67)
            W3 = Team("W3", 1682.811367, 3, 55)
            W4 = Team("W4", 1632.683621, 4, 53)
            W5 = Team("W5", 1585.557545, 5, 44)
            W6 = Team("W6", 1530.825816, 6, 42)
            W7 = Team("W7", 1453.274827, 7, 42)
            W8 = Team("W8", 1550.275157, 8, 41)
            W9 = Team("W9", 1538.76186, 9, 40)
            W10 = Team("W10", 1424.76719, 10, 33)
        elif (r == 1):
            #2016-17
            E1 = Team("E1", 1586.548998, 1, 53)
            E2 = Team("E2", 1544.969479, 2, 51)
            E3 = Team("E3", 1600.327521, 3, 51)
            E4 = Team("E4", 1587.292796, 4, 49)
            E5 = Team("E5", 1478.81584, 5, 43)
            E6 = Team("E6", 1502.303351, 6, 42)
            E7 = Team("E7", 1525.604928, 7, 42)
            E8 = Team("E8", 1518.698213, 8, 41)
            E9 = Team("E9", 1568.746275, 9, 41)
            E10 = Team("E10", 1440.539978, 10, 37)
            W1 = Team("W1", 1769.61789, 1, 67)
            W2 = Team("W2", 1661.086921, 2, 61)
            W3 = Team("W3", 1601.636708, 3, 55)
            W4 = Team("W4", 1635.603658, 4, 51)
            W5 = Team("W5", 1617.155001, 5, 51)
            W6 = Team("W6", 1542.7311455746, 6, 47)
            W7 = Team("W7", 1482.283149, 7, 43)
            W8 = Team("W8", 1563.283259, 8, 41)
            W9 = Team("W9", 1551.67756, 9, 40)
            W10 = Team("W10", 1482.420788, 10, 34)
        elif (r == 2):
            #2017-18
            E1 = Team("E1", 1675.616215, 1, 59)
            E2 = Team("E2", 1575.480725, 2, 55)
            E3 = Team("E3", 1660.410398, 3, 52)
            E4 = Team("E4", 1552.252717, 4, 50)
            E5 = Team("E5", 1556.721843, 5, 48)
            E6 = Team("E6", 1505.736767, 6, 44)
            E7 = Team("E7", 1514.049444, 7, 44)
            E8 = Team("E8", 1482.671174, 8, 43)
            E9 = Team("E9", 1487.700508, 9, 39)
            E10 = Team("E10", 1500.940417, 10, 36)
            W1 = Team("W1", 1732.213741, 1, 65)
            W2 = Team("W2", 1577.964814, 2, 58)
            W3 = Team("W3", 1614.263041, 3, 49)
            W4 = Team("W4", 1619.559364, 4, 48)
            W5 = Team("W5", 1686.339186, 5, 48)
            W6 = Team("W6", 1588.290373, 6, 48)
            W7 = Team("W7", 1580.171433, 7, 47)
            W8 = Team("W8", 1551.421614, 8, 47)
            W9 = Team("W9", 1587.070202, 9, 46)
            W10 = Team("W10", 1506.10923, 10, 42)
        elif (r == 3):
            #2018-19
            E1 = Team("E1", 1666.994641, 1, 60)
            E2 = Team("E2", 1644.110577, 2, 58)
            E3 = Team("E3", 1574.572545, 3, 51)
            E4 = Team("E4", 1586.066516, 4, 49)
            E5 = Team("E5", 1537.953947, 5, 48)
            E6 = Team("E6", 1517.072749, 6, 42)
            E7 = Team("E7", 1592.652024, 7, 42)
            E8 = Team("E8", 1498.859878, 8, 41)
            E9 = Team("E9", 1494.657367, 9, 39)
            E10 = Team("E10", 1496.66071, 10, 39)
            W1 = Team("W1", 1633.965443, 1, 57)
            W2 = Team("W2", 1595.375917, 2, 54)
            W3 = Team("W3", 1663.807169, 3, 53)
            W4 = Team("W4", 1712.585762, 4, 53)
            W5 = Team("W5", 1637.325338, 5, 50)
            W6 = Team("W6", 1581.016001, 6, 49)
            W7 = Team("W7", 1578.035069, 7, 48)
            W8 = Team("W8", 1542.82516, 8, 48)
            W9 = Team("W9", 1455.819675, 9, 39)
            W10 = Team("W10", 1462.213754, 10, 37)
        elif (r == 4):
            #2019-20
            E1 = Team("E1", 1671.257796, 1, 56)
            E2 = Team("E2", 1702.789483, 2, 53)
            E3 = Team("E3", 1646.531602, 3, 48)
            E4 = Team("E4", 1575.478438, 4, 45)
            E5 = Team("E5", 1557.137014, 5, 44)
            E6 = Team("E6", 1575.822608, 6, 43)
            E7 = Team("E7", 1509.438021, 7, 35)
            E8 = Team("E8", 1498.832477, 8, 33)
            E9 = Team("E9", 1374.65922, 9, 25)
            E10 = Team("E10", 1397.021678, 10, 23)
            W1 = Team("W1", 1610.759238, 1, 52)
            W2 = Team("W2", 1648.807883, 2, 49)
            W3 = Team("W3", 1551.103844, 3, 46)
            W4 = Team("W4", 1542.304608, 4, 44)
            W5 = Team("W5", 1575.537267, 5, 44)
            W6 = Team("W6", 1551.668964, 6, 44)
            W7 = Team("W7", 1553.706704, 7, 43)
            W8 = Team("W8", 1533.830679, 8, 35)
            W9 = Team("W9", 1555.600597, 9, 34)
            W10 = Team("W10", 1571.681561, 10, 34)
        elif (r == 5):
            #2020-21
            E1 = Team("E1", 1624.918781, 1, 49)
            E2 = Team("E2", 1614.415804, 2, 48)
            E3 = Team("E3", 1621.559733, 3, 46)
            E4 = Team("E4", 1599.437157, 4, 41)
            E5 = Team("E5", 1567.746732, 5, 41)
            E6 = Team("E6", 1565.159023, 6, 40)
            E7 = Team("E7", 1509.302865, 7, 36)
            E8 = Team("E8", 1511.179657, 8, 34)
            E9 = Team("E9", 1484.361991, 9, 34)
            E10 = Team("E10", 1426.443459, 10, 33)
            W1 = Team("W1", 1675.0549, 1, 52)
            W2 = Team("W2", 1649.284558, 2, 51)
            W3 = Team("W3", 1633.368412, 3, 47)
            W4 = Team("W4", 1617.838902, 4, 47)
            W5 = Team("W5", 1569.274863, 5, 42)
            W6 = Team("W6", 1617.621313, 6, 42)
            W7 = Team("W7", 1576.879857, 7, 42)
            W8 = Team("W8", 1549.656648, 9, 39)
            W9 = Team("W9", 1559.102257, 8, 38)
            W10 = Team("W10", 1471.274687, 10, 33)
        elif (r == 6):
            #2021-22
            E1 = Team("E1", 1596.872769, 1, 53)
            E2 = Team("E2", 1730.483025, 2, 51)
            E3 = Team("E3", 1577.357836, 3, 51)
            E4 = Team("E4", 1603.006549, 4, 51)
            E5 = Team("E5", 1601.489103, 5, 48)
            E6 = Team("E6", 1461.243681, 6, 46)
            E7 = Team("E7", 1544.821148, 7, 44)
            E8 = Team("E8", 1495.462706, 9, 44)
            E9 = Team("E9", 1563.918805, 8, 43)
            E10 = Team("E10", 1548.167777, 10, 43)
            W1 = Team("W1", 1672.600919, 1, 64)
            W2 = Team("W2", 1637.797872, 2, 56)
            W3 = Team("W3", 1610.056299, 3, 53)
            W4 = Team("W4", 1598.770266, 4, 52)
            W5 = Team("W5", 1589.147694, 5, 49)
            W6 = Team("W6", 1549.251713, 6, 48)
            W7 = Team("W7", 1561.909407, 7, 46)
            W8 = Team("W8", 1537.785097, 8, 42)
            W9 = Team("W9", 1515.735831, 9, 36)
            W10 = Team("W10", 1491.192218, 10, 34)
        else:
            #2022-23
            E1 = Team("E1", 1598.308948, 1, 58)
            E2 = Team("E2", 1682.054208, 2, 57)
            E3 = Team("E3", 1637.971022, 3, 54)
            E4 = Team("E4", 1601.488226, 4, 51) 
            E5 = Team("E5", 1587.778241, 5, 47)
            E6 = Team("E6", 1514.629197, 6, 45)
            E7 = Team("E7", 1546.102894, 8, 44)
            E8 = Team("E8", 1533.24877, 7, 41)
            E9 = Team("E9", 1569.686512, 9, 41)
            E10 = Team("E10", 1541.762118, 10, 40)
            W1 = Team("W1", 1548.908515, 1, 53)
            W2 = Team("W2", 1600.183097, 2, 51)
            W3 = Team("W3", 1538.309857, 3, 48)
            W4 = Team("W4", 1575.214725, 4, 45)
            W5 = Team("W5", 1548.601354, 5, 44)
            W6 = Team("W6", 1603.339713, 6, 44)
            W7 = Team("W7", 1571.343079, 7, 43)
            W8 = Team("W8", 1539.803364, 8, 42)
            W9 = Team("W9", 1540.227457, 9, 42)
            W10 = Team("W10", 1518.857459, 10, 40)

        if (playoffType == 0):
            season = Season(E1, E2, E3, E4, E5, E6, E7, E8, W1, W2, W3, W4, W5, W6, W7, W8)
            play_season(season, 1)
            eloList.append((E1.elo, E2.elo, E3.elo, E4.elo, E5.elo, E6.elo, E7.elo, E8.elo, 
                W1.elo, W2.elo, W3.elo, W4.elo, W5.elo, W6.elo, W7.elo, W8.elo))
        else:
            playEast1 = Game(E7, E8) # 7 plays 8
            PE1A, PE1B = playin_game(playEast1, 0, 0, 1)
            PE1A.rank = 7
            playEast2 = Game(E9, E10) # 9 plays 10
            PE2A, PE2B = playin_game(playEast2, 0, 0, 1)
            playEast3 = Game(PE1B, PE2A) # loser of 7-8 plays winner of 9-10
            PE3A, PE3B = playin_game(playEast3, 0, 0, 1)
            PE3A.rank = 8

            playWest1 = Game(W7, W8)
            PW1A, PW1B = playin_game(playWest1, 0, 0, 1)
            PW1A.rank = 7
            playWest2 = Game(W9, W10)
            PW2A, PW2B = playin_game(playWest2, 0, 0, 1)
            playWest3 = Game(PW1B, PW2A)
            PW3A, PW3B = playin_game(playWest3, 0, 0, 1)
            PW3A.rank = 8
            season = Season(E1, E2, E3, E4, E5, E6, PE1A, PE3A, W1, W2, W3, W4, W5, W6, PW1A, PW3A)
            play_season(season, 1)
            eloList.append((E1.elo, E2.elo, E3.elo, E4.elo, E5.elo, E6.elo, PE1A.elo, PE3A.elo, 
                W1.elo, W2.elo, W3.elo, W4.elo, W5.elo, W6.elo, PW1A.elo, PW3A.elo))
    dist = []
    for i in range(len(eloList[0])):
        temp = [x[i][0] for x in eloList]
        arr = np.asarray(temp)
        m = np.mean(arr)
        s = np.std(arr)
        dist.append((m,s))
    print(dist)
