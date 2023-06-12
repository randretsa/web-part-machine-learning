class Characteristics:
    
    # les caractéristiques du language
    def characteristics(self, language):
        charateristics = []
        charateristics.append(self.cardinality(language))
        charateristics.append(self.is_fixe_length(language))
        charateristics.append(self.one_digit_number(language))
        charateristics.append(self.zero_digit_number(language))
        charateristics.append(self.is_prefix(language))
        return charateristics

    # la cardinalité
    def cardinality(self, language):
        return len(language)
    
    # language de longeur fixe
    def is_fixe_length(self, language):
        length = 0
        if(language == []):
            return 0
        else:
            length = len(language[0])
        
        for word in language:
            if(len(word)!=length):
                return 0
        return 1
    
    # nombre de 1 dans le language
    def one_digit_number(self, language):
        number = 0
        for word in language:
            number = number + word.count('1')
        return number

   # le nombre de zero dans le language 
    def zero_digit_number(self, language):
        number = 0
        for word in language:
            number = number + word.count('0')
        return number
    
    # prefixe ou pas
    def is_prefix(self,language):
        for i in range(len(language)):
            for j in range(len(language)):
                if i != j and language[i].startswith(language[j]):
                    return 0
        return 1