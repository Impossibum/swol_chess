from rewards.reward import Reward


class PieceRatioReward(Reward):
    def __init__(self):
        self.piece_values = {
            'P': 1, 'p': 1,
            'N': 3, 'n': 3,
            'B': 3, 'b': 3,
            'R': 5, 'r': 5,
            'Q': 13, 'q': 13,
            'K': 0, 'k': 0
        }
        self.white_ratio = 0.5
        self.black_ratio = 0.5

    def tally_piece_scores(self, board)-> tuple[float, float]:
        _white_score = 0
        _black_score = 0
        for _, p in board.piece_map().items():
            if p.symbol() == p.symbol().upper():
                _white_score += self.piece_values[p.symbol()]
            else:
                _black_score += self.piece_values[p.symbol()]

        return _white_score, _black_score

    def calculate(self, board, done, illegal_move) -> tuple[float, float]:
        white_piece_score, black_piece_score = self.tally_piece_scores(board)
        #if white's turn
        reward = [0, 0]
        if board.turn or done:
            if white_piece_score != 0:
                ratio = white_piece_score / (white_piece_score + black_piece_score)
            else:
                if black_piece_score != 0:
                    ratio = 0
                else:
                    ratio = 0.5
            reward[0] = ratio - self.white_ratio
            self.white_ratio = ratio

        # if black's turn
        if not board.turn or done:
            if black_piece_score != 0:
                ratio = black_piece_score / (white_piece_score + black_piece_score)
            else:
                if white_piece_score != 0:
                    ratio = 0
                else:
                    ratio = 0.5
            reward[1] = ratio - self.black_ratio
            self.black_ratio = ratio

        return reward[0], reward[1]

    def reset(self):
        self.white_ratio = 0.5
        self.black_ratio = 0.5



if __name__ == "__main__":
    pass
