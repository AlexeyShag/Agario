import random
import math

Size_Win = 512

Pi = math.acos(-1)


class pos:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def copy(self):
        return pos(self.x, self.y)


def max(a, b):
    if a > b:
        return a
    return b


def min(a, b):
    if a > b:
        return b
    return a


class Player:
    ang = 0

    def __init__(self):
        self.x = random.randint( 100, Size_Win  - 100)
        self.y = random.randint( 100, Size_Win  - 100)

        self.IsMe = True
        self.Type = 0

        self.speed = 10
        self.score = 5
        self.Sc = [10, 10, 10, 1]

        self.SetAim()
        self.life = True

    def __init__(self, ME, Tp, score):
        self.x = random.randint(score *2, Size_Win - score *2)
        self.y = random.randint(score *2, Size_Win - score *2)

        self.IsMe = ME
        self.Type = Tp
        self.speed = 10
        self.score = score

        self.Sc = [10, 10, 10, 1]
        self.SetAim(0, 0)
        self.life = True

    def ReLife(self, Me, Tp):

        self.IsMe = Me
        self.Type = Tp
        self.speed = 10
        self.score = self.Sc[Tp]
        self.x = random.randint(self.score*2, Size_Win - self.score *2)
        self.y = random.randint(self.score *2, Size_Win - self.score *2)
        self.SetAim(0, 0)

    def SetAim(self):
        self.Aim = pos(0, 0)

    def SetAim(self, X, Y):
        self.Aim = pos(X, Y)

    def Get_Ang(self, X, Y):
        if X == 0:
            if Y > 0:
                self.ang = 3 * Pi / 2
            else:
                self.ang = Pi / 2
        elif Y == 0:
            if X > 0:
                self.ang = 0
            else:
                self.ang = Pi
        else:
            self.ang = math.atan(-(Y) / (X))

            if Y < 0 and X > 0:
                self.ang = self.ang
            elif Y < 0 and X < 0:
                self.ang += Pi
            elif Y > 0 and X < 0:
                self.ang = Pi + self.ang
            elif Y > 0 and X > 0:
                self.ang = 2 * Pi + self.ang
        return self.ang

    def Move_Pl(self):
        self.x += self.speed * math.cos(self.ang)
        self.y -= self.speed * math.sin(self.ang)

    def Eat(self, Enemy):
        self.score = min(100, self.score + Enemy.score // 5 + 1)
        self.speed = max(3, 10 - self.score // 5)

        if (Enemy.Type == 3):
            Enemy.ReLife(Enemy.IsMe, Enemy.Type)
        else:
            Enemy.life = False
