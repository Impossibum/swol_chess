from chess import Board


class Observation:
    def calculate(self, board: Board):
        raise NotImplementedError

    def reset(self):
        pass

    def get_obs_space(self):
        raise NotImplementedError

    def mirror_board(self, board: Board):
        return board.mirror()

if __name__ == "__main__":
    pass
