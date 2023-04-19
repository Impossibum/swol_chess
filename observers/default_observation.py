from observers.observer import Observation
from utilities.one_hot_encoder import SimpleOneHotEncoder
from itertools import chain
from gym import spaces


class DefaultObservation(Observation):
    def __init__(self, white_only=True):
        self.piece_dict = {
            'P': 1, 'p': 7,
            'N': 2, 'n': 8,
            'B': 3, 'b': 9,
            'R': 4, 'r': 10,
            'Q': 5, 'q': 11,
            'K': 6, 'k': 12
        }
        self.white_only = white_only
        self.encoder = SimpleOneHotEncoder(len(self.piece_dict)+1)
        # 64 squares of len 13 one hot vectors + 2 to indicate color and 2 for castling rights
        self.obs_space = spaces.Discrete((64*13)+4)

    def calculate(self, board):
        if self.white_only and not board.turn:
            board = self.mirror_board(board)
        obs = list(chain(*self._board_to_matrix(board)))
        obs = list(chain(*[self.encoder.encode(x) for x in obs]))
        if board.turn:
            obs.extend([1, 0])
        else:
            obs.extend([0, 1])

        if board.castling_rights:
            obs.extend([1, 0])
        else:
            obs.extend([0, 1])
        return obs

    def _board_to_matrix(self, board):
        board_matrix = [[0 for _ in range(8)] for _ in range(8)]

        for square, piece in board.piece_map().items():
            row, col = divmod(square, 8)
            board_matrix[row][col] = self.piece_dict[piece.symbol()]

        return board_matrix

    def get_obs_space(self):
        return self.obs_space


if __name__ == "__main__":
    pass
