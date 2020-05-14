class Student:
    being = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age == other.age:
            return True
        return False

    @classmethod
    def info(cls):
        cls.being = "animal"
        return cls.being


name1 = input("enter name1 : ")
age1 = int(input("enter age1 : "))
name2 = input("enter name2 : ")
age2 = int(input("enter age2 : "))

s1 = Student(name1, age1)
s2 = Student(name2, age2)

if s1.compare_age(s2):
    print("they are of same age")
else:
    print("they are of different age")

print(Student.info())
