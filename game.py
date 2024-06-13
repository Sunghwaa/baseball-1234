class Game:
    def guess(self, guessNumber):
        if guessNumber is None:
            raise TypeError()

        if len(guessNumber) != 3:
            raise TypeError()

        for char in guessNumber:
            if not char.isdigit():
                raise TypeError()
