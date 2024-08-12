from chess_coliseum import ChessEnv
from random import sample


# Simple defaults for all 3 args are provided but custom solutions will likely yield far better results.
env = ChessEnv(observation_class=None, reward_class=None, parser=None)
done = False
# simulate 10 games with random mover agents
for i in range(10):
    env.reset()
    while not done:
        # sampling a move from the handy list of legal moves as sampling from action space could cause illegal moves
        action = sample(env.legal_moves, 1)[0]
        obs, reward, done, info = env.step(action)
        # if match is concluded, print the results
        if 'result' in info:
            print(info['result'])
    done = False

env.close()
