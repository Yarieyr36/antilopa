import random


class Student:
    def __init__(self, name="Студент"):
        self.name = name
        self.home = None
        self.education = Education(education_list)  # Ініціалізація освіти
        self.job = None
        self.money = 100
        self.knowledge = 50
        self.stress = 30
        self.satiety = 50
        self.skills = 1
        self.friends = 3

    def get_home(self):
        self.home = Home()

    def study(self):
        if self.education.level >= 3:
            print("Максимальний рівень освіти досягнуто!")
            return
        self.knowledge += random.randint(5, 10)
        self.stress += random.randint(3, 7)
        self.satiety -= 5
        self.skills += 1
        print(f"Навчався. Знання: {self.knowledge}, Навички: {self.skills}")

    def get_job(self):
        if self.job:  # Якщо студент вже має роботу, він більше не шукає нову
            print("Студент вже працює.")
            return

        if self.skills >= 3 and self.education.level >= 2:
            self.job = Job(job_list)
            print(f"Отримав роботу: {self.job.job}, зарплата: {self.job.salary}")
        else:
            print("Недостатньо навичок для роботи! Треба вчитися.")

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                return
            self.satiety += 10
            self.home.food -= 10
            print(f"Поїв, ситість: {self.satiety}")

    def relax(self):
        self.stress = max(self.stress - 10, 0)
        self.money -= 5
        self.friends += 1
        print(f"Відпочивав з друзями. Стрес: {self.stress}")

    def work(self):
        if self.job:
            self.money += self.job.salary
            self.stress += self.job.stress_level
            print(f"Працював. Гроші: {self.money}, Стрес: {self.stress}")
        else:
            print("Немає роботи! Потрібно більше навичок.")

    def shopping(self, item):
        if item == "food":
            self.home.food += 50
            self.money -= 20
            print("Купив їжу")
        elif item == "books":
            self.knowledge += 10
            self.money -= 15
            print("Купив книги")

    def is_alive(self):
        if self.satiety <= 0:
            print("Гра закінчена. Студент помер від голоду.")
            return False
        if self.stress >= 100:
            print("Гра закінчена. Студент впав у депресію.")
            return False
        if self.money < -100:
            print("Гра закінчена. Студент банкрут.")
            return False
        return True

    def live_day(self, day):
        print(f"\nДень {day}")

        if self.stress > 80:
            print("Студент сильно перевтомлений! Треба відпочити.")
            self.relax()
        elif self.satiety < 30:
            print("Студент голодний! Треба поїсти.")
            self.eat()
        elif self.education.level < 3 and self.knowledge < 70:
            print("Студент вирішив вчитися.")
            self.study()
        elif not self.job and self.skills >= 3:
            print("Студент знайшов роботу!")
            self.get_job()
        elif self.job and (self.money < 500 or random.randint(1, 2) == 1):
            print("Студент працює.")
            self.work()
        elif random.randint(1, 4) == 1:
            print("Студент вирішив відпочити.")
            self.relax()
        else:
            print("Студент вирішив вчитися.")
            self.study()

        # Випадкові події
        if random.randint(1, 5) == 1:
            print("Несподівана подія! Отримав стипендію.")
            self.money += 50
        if random.randint(1, 6) == 2:
            print("Важкий день... рівень стресу виріс.")
            self.stress += 5
        if random.randint(1, 7) == 3:
            print("Взаємодія з друзями! Друзі допомогли з мотивацією.")
            self.stress -= 5
            self.skills += 1

        if not self.is_alive():
            return False
        return True


class Home:
    def __init__(self):
        self.food = 50


education_list = {
    "Школа": {"level": 1},
    "Коледж": {"level": 2},
    "Університет": {"level": 3},
}


class Education:
    def __init__(self, edu_list):
        self.education = random.choice(list(edu_list.keys()))
        self.level = edu_list[self.education]["level"]


job_list = {
    "Офіціант": {"salary": 30, "stress_level": 10},
    "Програміст": {"salary": 100, "stress_level": 20},
    "Інженер": {"salary": 70, "stress_level": 15},
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list.keys()))
        self.salary = job_list[self.job]["salary"]
        self.stress_level = job_list[self.job]["stress_level"]


# Запуск гри
student = Student()
student.get_home()

for day in range(1, 30):
    if not student.live_day(day):
        break
