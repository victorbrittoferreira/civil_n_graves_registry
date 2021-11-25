from typing import List
import json


def data_dict_to_json_file(obituary: List[dict]) -> None: 
    """
    This function takes an object of type dict and processes the respective methods of adding,
    filtering and returning the dictionary in json file.dict
    """


    obituary_json_data = {
        "obituarys": [
            {
        "id" : 0,
        "name": "name",
        "father_name": "father_name",
        "mother_name": "mother_name",
        "marital_status": "marital_status",
        "spouse_name": "spouse_name",
        "sons_name": "sons_name",
        "declarator_of_death_name": "declarator_of_death_name",
        "doctor_name": "doctor_name",
        "age": 0,
        "birth_date": 0,
        "marital_date": 0,
        "death_date": 0,
        "death_time": 0,
        "burial_date": 0,
        "burial_time": 0,
        "place_of_birth": "place_of_birth",
        "place_of_marital": "place_of_marital",
        "place_of_death": "place_of_death",
        "place_of_burial": "place_of_burial",
        "birth_registry_office": "birth_registry_office",
        "marital_registry_office": "marital_registry_office",
        "death_registry_office": "death_registry_office",
        "cause_of_death": "cause_of_death",
        "date_of_cemetery_registration": 0
            }
        ]
    }


    def dict_to_json_():
        try:
            with open('./database/obituary_w_test.json', 'w') as fp:
                json.dump(obituary_json_data, fp, ensure_ascii= False, indent= 4)
                
        except:
            return print("There was a problem executing the 'execute_filtros' function from the escrita file")  

    dict_to_json_()


