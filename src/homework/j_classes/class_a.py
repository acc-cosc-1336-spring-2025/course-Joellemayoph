import random

class Die:
    def __init__(self):
        self.roll_value = 1

    def roll(self):
        self.roll_value = random.randint(1,6)

    def get_rolled_value(self):
        return self.roll_value


