'''
class Engine:
    def __init__(self):
        print("Engine started.")

class Wheels:
    def __init__(self):
        print("Wheels installed.")

class Car(Engine, Wheels):
    def __init__(self):
        super().__init__()
        Wheels.__init__(self)
        print("Car is ready for drive.")

print("Initializing engine:")
car1 = Engine()

print("Building the car:")
car2 = Car()
 '''
'''
class Job:
    def __init__(self):
        print("Profession exists.")

class Doctor(Job):
    def __init__(self):
        super().__init__()
        print("Treats patients.")

class Engineer(Job):
    def __init__(self):
        super().__init__()
        print("Builds and designs.")

print("Profession 1:")
p1 = Doctor()

print("Profession 2:")
p2 = Engineer()
'''