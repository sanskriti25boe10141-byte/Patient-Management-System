import json  
#file used to store patient record 

FILE_NAME = "patients.json"
#load patient data from JSON file 

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

#save patient data to JSON file

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
