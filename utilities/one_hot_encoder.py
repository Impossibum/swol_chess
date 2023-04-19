class SimpleOneHotEncoder:
    def __init__(self, num_values: int):
        self.max_values = num_values
        self.encoder = self.create_encoding()

    def create_encoding(self):
        encoding = []
        for i in range(self.max_values):
            encoding.append([0] * self.max_values)
            encoding[i][i] = 1
        return encoding

    def encode(self, val: int):
        return self.encoder[val]


if __name__ == "__main__":
    pass
