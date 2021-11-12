class Deceased:


    def __init__(self, name, age) -> None:
        self.name = name
#        self.father_name = father_name
#        self.mother_name = mother_name

        self.age = age
#        self.birth_date = birth_date
#        self.place_of_birth = place_of_birth 

#        self.death_date = death_date
#        self.place_of_death = place_of_death
#        self.cause_of_death = cause_of_death 

#        self.registry_office = registry_office
        

    def setNome(self, nome):
        self.nome = nome

    def setAge(self, age):
        self.age = age
        
    
    def getName(self):
        return self.name

    def getAge(self): 
        return self.age 


