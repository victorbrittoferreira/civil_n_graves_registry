import datetime
class Deceased:


    def __init__(self, name, age , buried = bool ) -> None:

        self.buried = buried
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