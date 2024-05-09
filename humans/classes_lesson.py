import datetime
class Regimen:
    def __init__(self):
        self.size = []
    def add(self, amount: list):
        self.size = self.size + amount
    def remove(self, amount: list, name_s):
        if self.size:
            for a in amount:
                if a in name_s.size:
                    name_s.size.remove(a)


    def info(self):
        for i in self.size:
            for j in i.size:
            # return i.info()
                print(j.info())


class Squadron:
    def __init__(self):
        self.size = []
    def add(self, amount: list):
        self.size = self.size + amount
    def remove(self, amount: list):
        if self.size:
            for a in amount:
                if a in self.size:
                    self.size.remove(a)
    def info(self):
        for i in self.size:
            # return i.info()
            print(i.info())

class Human:
    def __init__(self, name):
        self.name = name
        self.date_of_birth = datetime.date(1990,3,27)
        self.__age = 30
    def info(self):
        try:
            return self.name + ' ' + str(self.__age) + ' ' + str(self.date_of_birth)
        except Exception as e:
            return 'need str'
    def set_db(self, y, m, d):
        self.date_of_birth = datetime.date(y,m,d)
    def set_age(self):
         self.__age = int(((datetime.datetime.now().date() - self.date_of_birth).days)/365)



