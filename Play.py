from Game import Game
from Neuron_Net import AgentNet
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from Exp_buffer import ExpReplayBuffer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import *
import Main
from Main import Main_Gr
from threading import Thread
import time




if __name__ == '__main__':
    game = Game(0, 5, 1, 150, 32)

    agent = AgentNet(3 * 156 + 4, 32)

    state = game.reset()

    agent.load_state_dict(torch.load("files/Save_Model.txt", map_location='cpu'))
    agent.eval()
    if ( False):
        Thread(target=Main_Gr, args=(game,), daemon = True).start()

    while True:
        time.sleep(0.05)
        qvalues = agent.get_qvalues([state])

        action = agent.sample_actions(qvalues)
        #print(action)
        new_state, reward, done = game.step(action)
        #exp_buffer.add(state, action, reward, new_state, done)
        if done:
            state = game.reset()
            # print('---: ' + str(reward))
        else:
            state = new_state
