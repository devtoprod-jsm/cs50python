import random


class Student:
    houses = ["Kostka","Campion","Xavier","Britto"]
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    @classmethod
    def get_house(cls):
        return random.choice(cls.houses)

    @classmethod
    def get(cls):
        fname = input("Give your fname: ")
        lname = input("Give your lname: ")
        age = int(input("Give your age: "))
        return cls(fname,lname,age)

print(Student.get_house())