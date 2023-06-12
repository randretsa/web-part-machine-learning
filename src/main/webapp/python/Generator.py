import random


class Generator:
    @staticmethod
    def generate_word():
        length = random.randint(1, 7)
        word = ""
        for position in range(0, length):
            letter = random.randint(0, 1)
            word = word + str(letter)
        return word

    def generate_language(self):
        L = []
        length = random.randint(1, 5)
        for position in range(0, length):
            word = self.generate_word()
            L.append(word)
        return L

