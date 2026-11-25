class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def details(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")

    def is_adult(self):
        if self.age >= 18:
            print("Adult: Yes")
        else:
            print("Adult: No")

s1 = Student("Visal", 22, "ST001")
s2 = Student("Nita", 16, "ST002")
s3 = Student("Sitha", 20, "ST003")

print("\n===== Student Information =====\n")
s = [s1, s2, s3]
for i in s:
    i.details()
    i.is_adult()
    print("")
