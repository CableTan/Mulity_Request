import time
import pickle
import torch
import torch.nn as nn
import torch.nn.functional as F
# -*- coding: UTF-8 -*-

class Actor(nn.Module):
    def __init__(self, state_dim, action_dim,action_bound):
        super(Actor,self).__init__()
        self.f1 = nn.Linear(input_dim, 256)
        self.f2 = nn.Linear(256, 128)
        self.f3 = nn.Linear(128, 64)
        self.f4 = nn.Linear(64, n_action)
        self.device =torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.to(self.device)
        self.str_time = time.strftime("%Y%m%d%H%M%S")