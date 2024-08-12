from rewards.reward import Reward


class CombinationReward(Reward):
    def __init__(self, reward_objects: list[Reward]):
        self.rewards = reward_objects

    def calculate(self, board, done, illegal_move) -> tuple[float, float]:
        rewards = [rew.calculate(board, done, illegal_move) for rew in self.rewards]
        return sum(r[0] for r in rewards), sum(r[1] for r in rewards)

    def reset(self):
        for rew in self.rewards:
            rew.reset()



if __name__ == "__main__":
    pass
