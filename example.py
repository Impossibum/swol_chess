from chess_coliseum import ChessEnv
from random import sample

env = ChessEnv()
done = False
# simulate 10 games with random mover agents
for i in range(10):
    env.reset()
    while not done:
        # sampling a move from the handy list of legal moves as sampling from action space would cause illegal moves
        action = sample(env.legal_moves, 1)[0]
        obs, reward, done, info = env.step(action)
        # if match is concluded, print the results
        if info:
            print(info)
    done = False

env.close()
