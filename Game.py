import Player as Player
from Player import *


class Game:
    Cnt_Me = 0
    Cnt_Bot_low = 0
    Cnt_Bot_High = 0
    Cnt_food = 0
    Cnt_Ang = 16

    Pi = math.acos(-1)
    Cnt_Players = 0
    Pls = []
    done = True

    Re = 0
    Cnt_life = 0
    Steps = 10
    Actions = []

    def __init__(self):
        super(Game, self).__init__()

    def __init__(self, Pl_Me, Bot_low, Bot_High, Food_kolvo, Cnt_a):
        self.Cnt_Me = Pl_Me
        self.Cnt_Bot_low = Bot_low
        self.Cnt_Bot_High = Bot_High
        self.Cnt_food = Food_kolvo

        self.Cnt_Players = self.Cnt_Me + self.Cnt_Bot_low + self.Cnt_Bot_High + self.Cnt_food
        self.Id_NN = self.Cnt_Me + self.Cnt_Bot_low
        self.Cnt_Ang = Cnt_a
        for i in range(self.Cnt_Ang):
            self.Actions += [2 * Pi * (i+1) / self.Cnt_Ang]

    def reset(self):
        self.Pl_Aim = []
        self.Pls = []
        self.done = True
        Steps = 0
        self.Cnt_life = self.Cnt_Me + self.Cnt_Bot_low + self.Cnt_Bot_High
        for i in range(self.Cnt_Players):
            if (i < self.Cnt_Me):
                self.Pls += [Player(True, 0, 10)]
                self.Pls[i].ReLife(self.Pls[i].IsMe, self.Pls[i].Type)
                continue
            if (i < self.Cnt_Bot_low + self.Cnt_Me):
                self.Pls += [Player(False, 1, 10)]
                self.Pls[i].ReLife(self.Pls[i].IsMe, self.Pls[i].Type)
                continue

            if (i < self.Cnt_Bot_High + self.Cnt_Bot_low + self.Cnt_Me):
                self.Pls += [Player(False, 2, 10)]
                self.Pls[i].ReLife(self.Pls[i].IsMe, self.Pls[i].Type)
                continue

            else:
                self.Pls += [Player(False, 3, 3)]
                self.Pls[i].ReLife(self.Pls[i].IsMe, self.Pls[i].Type)
                continue

        for i in range(self.Cnt_Players):
            self.Pls[i].life = True

        for i in range(self.Cnt_Players):
            if (self.Pls[i].Type != 3):
                while True:
                    j = random.randint(0, self.Cnt_Players-1)
                    if (self.Pls[i].score >= self.Pls[j].score + 5):
                        self.Pls[i].SetAim(-1, j)
                        break
        Ans = []

        Ids = []
        for i in range(self.Cnt_Players):
            Ids += [[self.Pls[i].x, self.Pls[i].y, self.Pls[i].score]]
        Ids = sorted(Ids, key=self.comp)
        for i in Ids:
            Ans += [i[0], i[1], i[2]]
        Ans.append(self.Pls[self.Id_NN].x)
        Ans.append(self.Pls[self.Id_NN].y)
        Ans.append(Size_Win - self.Pls[self.Id_NN].x)
        Ans.append(Size_Win - self.Pls[self.Id_NN].y)
        return Ans



    def IsIn(self, X, Y, s, x, y):
        if X - s < x and X + s > x and Y - s < y and Y + s > y:
            return True
        return False

    def Out_Game(self, a):
        if (a.x < 0 or a.x > Size_Win or a.y < 0 or a.y > Size_Win):
            return True
        else:
            return False

    def Dist(self, pl, a, b):
        return math.sqrt((pl.x - a)**2 + (pl.y - b)**2)

    def Get_World(self):
        Ans = []
        Res = []
        for i in range(Size_Win):
            Res.append(0)
        for i in range(Size_Win):
            Ans.append(Res)

        for pl in self.Pls:
            X = pl.x - pl.score
            Y = pl.y - pl.score
            for i in range(pl.score * 2):
                if (X + i > Size_Win or X + i < 0): continue
                for j in range(pl.score * 2):
                    if(Y + j > Size_Win or Y + j < 0): continue
                    if( self.Dist(pl,X+i,Y+j) <= pl.score):
                        Ans[X+i][Y+j] = pl.Type

        return Ans


    def step(self, id):
        #print(id)
        #print(' -- ' + str(id))
        ang = self.Actions[id]
        # if (self.Cnt_life == 1):
        #     self.reset();
        self.Pls[self.Id_NN].ang = ang
        self.Pls[self.Id_NN].Move_Pl()
        self.Re = 0
        if (self.Steps == 20):
            for Pl in self.Pls:
                if (Pl.Type < 3):
                    Pl.score = max(10, Pl.score - 1)
            self.Steps = 0



        State = self.Move_Pl()
        if (self.Out_Game(self.Pls[self.Id_NN])):
            self.done = False

        self.Steps += 1
        return State, self.Re, not self.done


    def D(self, a, b,c):
        return abs(a.x - b) + abs(a.y - c)

    def comp(self, a):
        return self.D(self.Pls[self.Id_NN], a[0], a[1])

    def Move_Pl(self):
        Ans = []
        p = pos(0, 0)
        for i in range(self.Cnt_Players):
            if (self.Pls[i].life == False): continue
            if (self.Pls[i].Type == 3): continue

            if self.Pls[i].Aim.x == -1:
                p = self.Pls[i].Aim.copy()
                self.Pls[i].Aim.x = self.Pls[p.y].x
                self.Pls[i].Aim.y = self.Pls[p.y].y
            for j in range(self.Cnt_Players):
                if (self.Pls[j].life == False): continue
                if self.IsIn(self.Pls[i].x, self.Pls[i].y, self.Pls[i].score, self.Pls[j].x, self.Pls[j].y) and \
                        self.Pls[i].score >= self.Pls[j].score + 5:
                    if (self.Pls[i].Type == 2):
                        self.Re += self.Pls[j].score
                    if (self.Pls[j].Type == 2):
                        self.done = False
                    if (self.Pls[j].Type < 3):
                        self.Cnt_life -= 1
                    self.Pls[i].Eat(self.Pls[j])

                    while True:
                        if (self.Pls[i].Type == 0): break
                        k = random.randint(0, self.Cnt_Players - 1)
                        if (self.Pls[i].score >= self.Pls[k].score + 5):
                            self.Pls[i].Aim.x = -1
                            self.Pls[i].Aim.y = k
                            break
                    f = True
                    break

            if (self.Pls[i].Aim.x - self.Pls[i].x == 0) and (self.Pls[i].Aim.y - self.Pls[i].y == 0) or (
                    self.Pls[i].Type == 2):
                continue
            else:
                X = self.Pls[i].Aim.x - self.Pls[i].x
                Y = self.Pls[i].Aim.y - self.Pls[i].y
                self.Pls[i].Get_Ang(X, Y)
                self.Pls[i].Move_Pl()

                if self.Pls[i].Type != 0:
                    self.Pls[i].Aim = p.copy()
        Ids = []
        for i in range(self.Cnt_Players):
            Ids += [[self.Pls[i].x, self.Pls[i].y, self.Pls[i].score]]
        Ids = sorted(Ids, key = self.comp)
        for i in Ids:
            Ans += [i[0], i[1], i[2]]
        Ans.append(self.Pls[self.Id_NN].x)
        Ans.append(self.Pls[self.Id_NN].y)
        Ans.append(Size_Win - self.Pls[self.Id_NN].x)
        Ans.append(Size_Win - self.Pls[self.Id_NN].y)
        return Ans


