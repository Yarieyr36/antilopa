class Student:
    print("Hello Bobik")

    def __init__(self, height=165):
        self.height = height



Artem = Student(height=170)
Yarik = Student()

print("my height = ", Artem.height)
print("my height = ", Yarik.height)