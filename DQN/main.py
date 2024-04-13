import os
import gym
import numpy as np
from PIL import Image
import torch
from breakout import *
from model import AtariNet
from agent import Agent

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

env = DQNBreakout(device=device)

model = AtariNet(nb_actions=4)
model.to(device)
model.load_model()

agent = Agent(model=model, device=device, epsilon=1.0, nb_warmup=1000, nb_actions=4, learning_rate=0.00001,
              memory_capacity=1000000, batch_size=64)

agent.train(env=env, epochs=20000)