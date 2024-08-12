from chess import Board


class Reward:
    def calculate(self, board: Board, done: bool, illegal_move: bool) -> tuple[float, float]:
        # Your custom reward class implementation here
        pass

    def reset(self):
        pass


if __name__ == "__main__":
    pass
