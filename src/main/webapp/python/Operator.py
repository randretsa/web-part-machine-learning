class Operator:
    def residuel(self, lanquage, word):
        residu = []
        position = len(word)
        for mot in lanquage:
            prefixe = mot[0 : position]
            if prefixe == word:
                new_word = mot[position:]

                if len(new_word) > 0: residu.append(new_word)
                else: residu.append("e")
        return residu

    def quotient(self, language, diviseur):
        quotient = []
        for mot in diviseur:
            li = self.residuel(language, mot)
            for word in li:
                quotient.append(word)
        l = list(set(quotient))
        return l

    def petterson(self, langage):
        L0 = langage
        L1 = self.quotient(langage, langage)
        L1.remove('e')
        occurences = [L0, L1]
        li = L1
        i = 2
        while (1 < 2):
            leftL2 = self.quotient(li,langage)
            rightL2 = self.quotient(langage, li)
            li = list(set(leftL2 + rightL2))

            if 'e' in li:
                # print("L" + str(i) +" :" + str(li))
                #return False
                return 0
            subid = 0
            for sublist in occurences:
                if sublist == li:
                    # print("L" + str(subid)+" et L"+ str(i) +" sont similaires")
                    # print(occurences)
                    #return True
                    return 1
                subid = subid + 1
            occurences.append(li)
            i = i +1
