from rewards.reward import Reward


class DefaultReward(Reward):
    def calculate(self, board, done):
        if done:
            if board.is_checkmate():
                return 1.0
            elif board.is_stalemate() or board.is_insufficient_material():
                return 0.0
            else:
                return 0.5
        else:
            return 0.0


if __name__ == "__main__":
    pass
