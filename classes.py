class Human:
    name: str
    age: int
    def __init__(self):
        self.name = "Jordan"
        self.age = 30
    def __str__(self):
        return 'this is a human'

    def see_info(self):
        print(self.name)
        print(self.age)
class Child(Human):
    def __init__(self):
        super().__init__
        self.name = 'Mike'
        self.age = 10
        self.current_loc = [0] * 3
    def __str__(self):
        return self.name
    def get_loc (self):
        return self.current_loc
    def set_loc (self, loc):
        self.current_loc = loc

child1 = Child()
# child1.see_info()
human1 = Human()
# human1.see_info()
child2 = Child()
child2.age = 11
child2.name = 'Pete'
# child2.see_info()
# print(human1)

class Bus:
    amount: list
    def __init__(self):
        self.amount = []
        self.current_loc = [0] * 3
    def change_bus_loc(self, a , b, c):
        if self.amount:
            for child in self.amount:
                child.set_loc([a, b, c])
    def cur_loc(self):
        for child in self.amount:
            print(child.get_loc())
    def add_on_board(self, child):
        self.amount.append(child)
        return self.amount
    def delete_on_board(self, child):
        self.amount.remove(child)
        return self.amount
school_bus = Bus()
print(school_bus.amount)
school_bus.add_on_board(child1)
print(school_bus.amount)
school_bus.add_on_board(child2)
print(school_bus.amount)
# school_bus.delete_on_board(child1)
# print(school_bus.amount)
print(child1)
print(child2)
print(human1)
school_bus.change_bus_loc(1, 2, 3)
school_bus.cur_loc()
# print(child2.get_loc())
child3 = Child()
school_bus.add_on_board(child3)
school_bus.change_bus_loc(2, 2, 3)
school_bus.cur_loc()























