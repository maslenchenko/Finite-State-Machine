from main import FSM
import random

state = FSM()
while True:
    probability = random.random()
    state.send(probability)
    if state.stopped is True:
        break
