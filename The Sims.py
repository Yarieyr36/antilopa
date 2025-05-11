import  random
class Human:
    def __init__(self, name="Name", job=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= self.car.consumption:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                return
            else:
                self.satiety += 5
                self.home.food -= 5
                self.mess += 1

    def chill(self):
        self.gladness += 15
        self.home.mess += 2

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= self.car.consumption:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= self.car.consumption:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            self.car.fuel += 100
            self.money -= 100
            print("I bought fuel")
        elif manage == "food":
            self.home.food += 50
            self.money -= 45
            print("I bought food")
        elif manage == "sweets":
            self.gladness += 10
            self.satiety += 2
            self.money -= 10
            print("I bought sweets!")
    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
    def is_alive(self):
        if self.satiety < 0:
            print("Game Over, you dead...")
            return False
        if self.money < -500:
            print("Game Over, you are Bankrupt...")
            return False
        if self.gladness < 0:
            print("Game Over, you in Depresion...")
            return False

    def live(self, day):
        if self. is_alive() == False:
            return False
        if self.home == None:
            print("I settled in the house!")
            self.get_home()
        if self.car == None:
            self.get_car()
            print(f"I bought car {self.car.brand} !")
        if self.job == None:
            self.get_job()
            print(f"I going to get a job {self.job.job},and my salary is {self.job.salary} !")


        self.days_indexes(day)
        if self.satiety < 20:
            print("I am going to eat")
            self.eat()
        elif self.gladness <20:
            if self.home.mess > 15:
                print("I will clean my home")
                self.clean_home()
            else:
                print("Lets chill!")
            self.chill()
        elif self.money < -50:
            print("I need to work")
            self.work()


        dice = random.randint(1,4)
        if dice == 1:
            print("Lets chill!")
            self.chill()
        elif dice == 2:
            print("I will work")
            self.work()
        elif dice == 3:
            print("I will clean my home")
            self.clean_home()
        elif dice == 4:
            print("It`s time for sweets!")
            self.shopping(manage="sweets!")


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

brands_of_car = {
"BMW": {"fuel": 100, "strength": 100, "consumption": 10},
"Lada": {"fuel": 50, "strength": 40, "consumption": 6},
"Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
"Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot move")
            return False

job_list = {
"Java developer": {"salary": 50, "gladness_less": 10},
"Python developer": {"salary": 40, "gladness_less": 3},
"C++ developer": {"salary": 45, "gladness_less": 20},
"Rust developer": {"salary": 70, "gladness_less": 1},
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

Oleg = Human(name="Oleg")
for day in range(1,30):
    if Oleg.live(day) == False:
        break