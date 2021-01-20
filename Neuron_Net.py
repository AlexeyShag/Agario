import math
import random
import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F
import torch.optim as optim
from Main import *


# Is_Train = False
#
#
Cnt_Angs = 16
# Input_size = 168
Pi = math.acos(-1)
# eps = 80
# gam = 0.9
# Steps = 0
#
Actions = []
for i in range(Cnt_Angs):
    Actions += [(i+1) * 2*Pi / Cnt_Angs]

class AgentNet(nn.Module):
    def __init__(self, input_size, n_actions, eps=0.1):
        super(AgentNet, self).__init__()
        self.eps = eps
        self.net = nn.Sequential(
            nn.Linear(input_size, 400),
            nn.ReLU(),
            nn.Linear(400, 200),
            nn.ReLU(),
            nn.Linear(200, 100),
            nn.ReLU(),
            nn.Linear(100, n_actions)
        )

    def forward(self, x):
        return self.net(x)

    def sample_actions(self, qvalues):
        epsilon = self.eps

        random_action = np.random.choice(qvalues.size)
        best_action = qvalues.argmax()
        #print(random.random())
        if random.random() < self.eps:
            return random_action
        else:
            return best_action

    def get_qvalues(self, state):
        state = torch.tensor(state, dtype=torch.float)
        qvalues = self.forward(state)
        return qvalues.data.cpu().numpy()



# ////////////////////////////////////////////////

