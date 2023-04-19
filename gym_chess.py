import gym
from gym import spaces
import chess
from rewards.default_reward import DefaultReward
from observers.default_observation import DefaultObservation
from action_parsers.default_discrete_parser import DefaultDiscreteParser


class ChessEnv(gym.Env):
    def __init__(self, observation_class=None, reward_class=None, parser=None):
        super(ChessEnv, self).__init__()
        self.board = chess.Board()
        self.legal_moves = []
        self.observation = observation_class or DefaultObservation()
        self.reward = reward_class or DefaultReward()
        self.parser = parser or DefaultDiscreteParser()
        self.observation_space = self.observation.get_obs_space()
        self.action_space = self.parser.get_action_space()
        self.populate_legal_moves()

    def reset(self):
        self.reward.reset()
        self.observation.reset()
        self.board.reset()
        self.populate_legal_moves()
        return self.observation.calculate(self.board)

    def step(self, action):
        move = self.parser.decode(action)

        if action not in self.legal_moves:
            return self.observation.calculate(self.board), -1.0, True, {'result': 'illegal_move'}

        self.board.push(move)
        done = self.board.is_game_over()
        reward = self.reward.calculate(self.board, done)
        info = {}

        if done:
            info['result'] = self.board.result()
        else:
            self.populate_legal_moves()

        return self.observation.calculate(self.board), reward, done, info
        #return [], reward, done, info

    def render(self, mode='human'):
        print(self.board)

    def populate_legal_moves(self):
        self.legal_moves = [self.parser.encode(m) for m in list(self.board.legal_moves)]


if __name__ == "__main__":
    pass
