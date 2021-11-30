import json 


def read_json() -> dict:

    """This function takes a file json type 
    and transforms and return it into a dictionary. 
    """

    try:
        obituary = None
        with open('./database/obituary.json') as json_file:   
            obituary = json.load(json_file)

        return obituary
    except:
        return print(
            "There was a problem executing the 'read_json' function from the leitura file")
    

