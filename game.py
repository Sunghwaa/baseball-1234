from game_result import GameResult


class Game:
    def __init__(self):
        super().__init__()
        self.question = ""

    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)
        return GameResult(True, 3, 0)

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for char in guessNumber:
            if not char.isdigit():
                raise TypeError()
        if len(guessNumber) != len(set(guessNumber)):
            raise TypeError()
