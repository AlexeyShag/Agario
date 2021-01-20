import sys
import math
import time
import random
from Game import Game
from Player import *
from Form import *
from Neuron_Net import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

Size_Win = 512

class pos:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def copy(self):
        return pos(self.x, self.y)


myapp = None


def max(a, b):
    if a > b:
        return a
    return b


class Gr_Win(QtWidgets.QMainWindow):
    Id_NN = 6

    def __init__(self, Game, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.B_Start_Game.clicked.connect(self.B_Start_Game_Click)

        self.painter = QtGui.QPainter(self)

        self.game_env = Game
        if self.game_env.Cnt_Me == 1:
                self.id_Pls = 0
        else:
            self.id_Pls = -10
        self.ReDraw = None
        self.photo = 1
    def Clichk(self):
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save('Line/' + str(self.photo) + 'shot.jpg', 'jpg')
        #print(screenshot.toImage().pixel(0,0))
        self.photo += 1

    def B_Start_Game_Click(self):
        self.ui.lvl = 1
        self.ui.Edit()

        self.ReDraw.start()
        self.update()


    def paintEvent(self, event):

        self.painter.begin(self)
        if self.ui.lvl == 1:
            for Pl in self.game_env.Pls:
                if Pl.life == False: continue
                if Pl.Type == 0:
                    self.painter.setBrush(QtGui.QBrush(QtCore.Qt.green))
                    self.painter.setPen(QtGui.QPen(QtCore.Qt.green))
                    self.painter.drawEllipse(
                        QtCore.QRectF(Pl.x - Pl.score, Pl.y - Pl.score, Pl.score * 2, Pl.score * 2))
                if Pl.Type == 1:
                    self.painter.setBrush(QtGui.QBrush(QtCore.Qt.red))
                    self.painter.setPen(QtGui.QPen(QtCore.Qt.red))
                    self.painter.drawEllipse(
                        QtCore.QRectF(Pl.x - Pl.score, Pl.y - Pl.score, Pl.score * 2, Pl.score * 2))
                if Pl.Type == 2:
                    self.painter.setBrush(QtGui.QBrush(QtCore.Qt.blue))
                    self.painter.setPen(QtGui.QPen(QtCore.Qt.blue))
                    self.painter.drawEllipse(
                        QtCore.QRectF(Pl.x - Pl.score, Pl.y - Pl.score, Pl.score * 2, Pl.score * 2))
                if Pl.Type == 3:
                    self.painter.setBrush(QtGui.QBrush(QtCore.Qt.black))
                    self.painter.setPen(QtGui.QPen(QtCore.Qt.black))
                    self.painter.drawEllipse(
                        QtCore.QRectF(Pl.x - Pl.score, Pl.y - Pl.score, Pl.score * 2, Pl.score * 2))
        elif self.ui.lvl == 0:
            self.painter.setBrush(QtGui.QBrush(QtCore.Qt.white))
            self.painter.setPen(QtGui.QPen(QtCore.Qt.white))
            self.painter.drawRect(0, 0, 500, 500)
        self.painter.end()
        pass

    def eventFilter(self, obj, event):
        if event.type() == QEvent.HoverMove and self.ui.lvl == 1 and self.id_Pls != -10:
            self.game_env.Pls[self.id_Pls].Aim.x = event.pos().x()
            self.game_env.Pls[self.id_Pls].Aim.y = event.pos().y()
            return True

        return super(Gr_Win, self).eventFilter(obj, event)


class ReDrawProcess(QThread):

    def __init__(self,myapp, parent=None):
        super(ReDrawProcess, self).__init__((parent))
        self.myapp = myapp
    def run(self):
        self.myapp.game_env.reset()
        #st = 0
        while True:
            time.sleep(0.05)
            self.myapp.game_env.Move_Pl()
            #st += 1
            #if(st == 10):
                #st = 0
            self.myapp.Clichk()
            self.myapp.update()
            if( self.myapp.game_env.Cnt_life == 1):
                self.myapp.game_env.reset()





def Main_Gr(gme = Game(0, 0, 1, 150, 4)):
    global myapp
    game = gme
    app = QtWidgets.QApplication(sys.argv)

    myapp = Gr_Win(game)
    myapp.installEventFilter(myapp)
    ReDraw = ReDrawProcess(myapp)
    ReDraw.finished.connect(app.exit)
    myapp.ReDraw = ReDraw
    myapp.show()
    myapp.ui.Load()
    myapp.ui.Edit()
    app.exec_()





if __name__ == "__main__":
    Main_Gr()
