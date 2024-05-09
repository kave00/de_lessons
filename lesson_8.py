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
        self.__age = 30
    def set_age(self, age):
        self.__age = age
    def info(self):
        try:
            return self.name + ' ' + str(self.__age)
        except Exception as e:
            return 'need str'
        finally:
            print("succeeded?")
# h1 = Human('John')
# # print(h1.info())
# h2 = Human('Derek')
# h2.set_age(25)
# # print(h2.info())
# h3 = Human('Bob')
# h4 = Human('Jose')
# h4.set_age(28)
# # print(h4.info())
#
# r1 = Regimen()
# s1 = Squadron()
# s2 = Squadron()
# s1.add([h1, h2])
# s2.add([h3, h4])
# # s1.info()
# # s2.info()
# r1.add([s1, s2])
# # r1.info()
# s1.remove([h2])
# # s1.info()
# # r1.info()
# r1.remove([h3], s2)
# # r1.info()
# # s2.info()
# h4 = Human(1.2)
# print(h4.info())



