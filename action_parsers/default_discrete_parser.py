from action_parsers.action_parser import ActionParser
from chess import Move
from gym import spaces


class DefaultDiscreteParser(ActionParser):
    def __init__(self):
        self.action_space = spaces.Discrete(64 * 64)  # 64 * 64 possible moves

    def encode(self, move):
        from_square = move.from_square
        to_square = move.to_square
        encoded_move = from_square * 64 + to_square
        return encoded_move

    def decode(self, action):
        from_square = action // 64
        to_square = action % 64
        return Move(from_square, to_square)

    def get_action_space(self):
        return self.action_space
