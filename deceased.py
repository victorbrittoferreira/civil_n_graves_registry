import datetime
class Deceased:


    def __init__(self, name, age , buried = bool ) -> None:

        self.name = name
#        self.father_name = father_name
#        self.mother_name = mother_name

        self.age = age
#        self.birth_date = birth_date
#        self.place_of_birth = place_of_birth 

#        self.death_date = death_date
#        self.place_of_death = place_of_death
#        self.cause_of_death = cause_of_death 
#        self.burial_date = burial_date
        self.buried = buried
        self.date_of_cemetery_registration = datetime.datetime.today()

#        self.registry_office = registry_office
        self.dead_status = []

    def setNome(self, nome):
        self.nome = nome

    def setAge(self, age):
        self.age = age

    def dead_status_update(self, updating):
        #now = datetime.datetime.today()
        updating_dated = (updating, datetime.datetime.today())
        self.dead_status.append(updating_dated)

    def status_records(self):
        for update in self.dead_status:
            print(update)
        
    def getName(self):
        return self.name

    def getAge(self): 
        return self.age 

#deceased_test = Deceased("victor",30)

#print(deceased_test.buried)