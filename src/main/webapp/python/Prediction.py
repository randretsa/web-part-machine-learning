from joblib import load
from Characteristics import Characteristics
import sys
import ast

def prediction(model_path,language):
    character = Characteristics()
    language = ast.literal_eval(language)
    X_test = character.characteristics(language=language)
    model = load(model_path)
    prediction = model.predict([X_test])
    print(language)
    print("len",str(len(language)) + "\n")
    print(prediction)
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