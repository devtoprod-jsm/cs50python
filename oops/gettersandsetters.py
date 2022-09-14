class Student:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        return f"I am {self.fname} {self.lname}, I am {self.age} years old"

    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self,fname):
        self._fname = fname

    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self,lname):
        self._lname = lname

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if age < 0 :
            raise ValueError("Age should be 0 and above")
        self._age = age

def get_student(fname,lname,age):
     return Student(fname,lname,age)

def main():
    fname = input("Give fname: ")
    lname = input("Give lname: ")
    age =  int(input("Give age: "))
    student = Student(fname,lname,age)
    print(student)

if __name__ == "__main__":
    main()