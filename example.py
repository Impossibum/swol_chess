from gym_chess import ChessEnv
import gym
from random import sample

env = ChessEnv()
done = False

while not done:
    # sampling a move from the handy list of legal moves as sampling from action space would cause illegal moves
    action = sample(env.legal_moves, 1)[0]
    obs, reward, done, info = env.step(action)

env.close()
