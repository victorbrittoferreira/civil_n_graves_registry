import datetime

class Obituary:
    #>>>>>>>>>>>trabalhar os typehints
    #>>>>>>>>>> SQL Alchemy
    #Geek university

    # será instanciada depois
    #date_of_cemetery_registration = datetime.datetime.today()

    #def __init__(self, id,  name, father_name, mother_name, marital_status, spouse_name, sons_name, declarator_of_death_name, doctor_name, age, birth_date, marital_date, death_date, death_time, burial_date, burial_time, place_of_birth, place_of_marital, place_of_death, place_of_burial, birth_registry_office, marital_registry_office, death_registry_office, cause_of_death, date_of_cemetery_registration ) -> None:
    def __init__(self, id, name, age,  cause_of_death ) -> None:


        self.id = id
        
        # NAMES
        self.name = name
#        self.father_name = father_name
#        self.mother_name = mother_name
#        self.marital_status = marital_status
#        self.spouse_name = spouse_name 
#        self.sons_name = sons_name
#        self.declarator_of_death_name = declarator_of_death_name
#        self.doctor_name = doctor_name
#        
#        #DATES  # must improve date+time
        self.age = age
#        self.birth_date = birth_date
#        self.marital_date = marital_date
#        self.death_date = death_date
#        self.death_time = death_time
#        self.burial_date = burial_date
#        self.burial_time = burial_time
#
#        #PLACES
#        self.place_of_birth = place_of_birth
#        self.place_of_marital = place_of_marital 
#        self.place_of_death = place_of_death
#        self.place_of_burial = place_of_burial
#
#        #REGISTRY OFFICE
#        self.birth_registry_office = birth_registry_office
#        self.marital_registry_office = marital_registry_office
#        self.death_registry_office = death_registry_office
#
        self.cause_of_death = cause_of_death 
        
        self.date_of_cemetery_registration = datetime.datetime.today()
        #self.date_of_cemetery_registration = date_of_cemetery_registration

obituary = Obituary("victor", 30 , "Covid-19, SRAG, IRA")