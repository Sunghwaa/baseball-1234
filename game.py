class Game:
    def guess(self, guessNumber):
        if guessNumber is None:
            raise TypeError()

        if len(guessNumber) != 3:
            raise TypeError()

        for char in guessNumber:
            if not char.isdigit():
                raise TypeError()

        if guessNumber[0] == guessNumber[1] or \
                guessNumber[0] == guessNumber[2] or \
                guessNumber[1] == guessNumber[2]:
            raise TypeError()
