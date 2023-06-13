from joblib import load
from Characteristics import Characteristics
from Operator import Operator
import sys
import ast

def prediction(model_path,language):
    sardinas = Operator()
    character = Characteristics()
    language = ast.literal_eval(language)
    X_test = character.characteristics(language=language)
    model = load(model_path)
    prediction = model.predict([X_test])
    petterson = sardinas.petterson(langage=language)

    print(language)
    print(";")
    ML_message = "selon ML c un code" if prediction[0]==1 else "selon ML c est pas un code"
    print(ML_message)
    print(";")
    Peterson_message = "selon Petterson c un code" if petterson==1 else "selon Petterson c est pas code"
    print(Peterson_message)
#Get command-line arguments
args = sys.argv

if(len(args)>1):
    #model path
    model_path = args[1]
    #remove the script name from arguments
    #arguments = args[2:]
    arguments = args[2]
    # call the function
    prediction(model_path,arguments)
else:
    print("please provide the array of string as argument")