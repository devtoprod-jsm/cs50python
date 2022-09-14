class Student:
    def __init__(self,fname,lname,age):
        if age < 0:
            raise ValueError("Age should be 0 and above")
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def __str__(self):
        return f"I am {self.fname} {self.lname}, and I am {self.age} years old"

    def  fullname(self):
        return self.fname + " " + self.lname


def get_student():
    fname = input("Give firstname: ")
    lname = input("Give lastname: ")
    age = int(input("Give age: "))
    return Student(fname,lname,age)

def main():
    student = get_student()
    print(student)
    print(student.fullname())

if __name__ == "__main__":
    main()