from Generator import Generator
from Characteristics import Characteristics
from Operator import Operator
import csv
class File:
    def generate_false_csv(self, file_path):
        generator = Generator()
        character = Characteristics()
        sardinas = Operator()
        
        data = []

        for i in range(0,50):
            language = []
            classe = 1
            
            while(classe!=0):
                language = generator.generate_language()
                classe = sardinas.petterson(language)

            columns = character.characteristics(language=language)
            columns.append(classe)
            data.append(columns)
        
        # Write data to CSV file
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["cardinality","is_fixe","one_digit_nbr","zero_digit_nbr","is_prefixe","classe"])
            writer.writerows(data)
        
    def generate_csv(self, file_path):
        generator = Generator()
        character = Characteristics()
        sardinas = Operator()
        
        data = []

        for i in range(0,4000):
            language = generator.generate_language()
            classe = sardinas.petterson(language)
            columns = character.characteristics(language=language)
            columns.append(classe)
            data.append(columns)
        
        # Write data to CSV file
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["cardinality","is_fixe","one_digit_nbr","zero_digit_nbr","is_prefixe","classe"])
            writer.writerows(data)
        