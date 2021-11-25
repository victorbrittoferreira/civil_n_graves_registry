import datetime

from obituary import Obituary



class Deceased:


    def __init__(self , obituary, buried : bool ) -> None:
        self.obituary = obituary
        self.buried = buried
        self.dead_status = []


    def dead_status_update(self, updating):
        #now = datetime.datetime.today()
        updating_dated = (updating, datetime.datetime.today())
        self.dead_status.append(updating_dated)

    def status_records(self):
        for update in self.dead_status:
            print(update)
        
#    def getName(self):
#        return self.name
#
#    def getAge(self): 
#        return self.age 

#deceased_test = Deceased(obituary, True)

#print(deceased_test.buried)