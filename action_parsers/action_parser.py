class ActionParser:
    def encode(self, move):
        raise NotImplementedError

    def decode(self, move):
        raise NotImplementedError

    def get_action_space(self):
        raise NotImplementedError
