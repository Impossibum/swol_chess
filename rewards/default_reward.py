from rewards.reward import Reward


class DefaultReward(Reward):
    def calculate(self, board, done):
        if done:
            if board.is_checkmate():
                if board.turn:
                    return [-1, 1]
                else:
                    return [1, -1]
            elif board.is_stalemate() or board.is_insufficient_material():
                return [0, 0]
            else:
                return [0, 0]
        else:
            return [0, 0]


if __name__ == "__main__":
    pass
