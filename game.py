class Game:
    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)

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
