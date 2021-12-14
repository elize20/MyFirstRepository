#Написать класс Student, который наследует класс human,
#у которого среди прочих признаков есть 'Кол-во сданных дз'
#Перезагрузить операторы сравнения так, чтобы студенты
#сравнивались по кол-ву сданных ими дз

class Human():
    def __init__(self, first_name, last_name, gender, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
    
    def say(self, text):
        print(f'{self.first_name} {self.last_name} says: {text}')
    

class Student(Human):
    def __init__(self, first_name, last_name, gender, age, height, weight, id, course, group, number_homeworks):
        super().__init__(first_name, last_name, gender, age, height, weight)
        self.id = id
        self.course = course
        self.group = group
        self.number_homeworks = number_homeworks
    
    def info(self):
        return self.first_name + ' ' + self.last_name
    
    def __eq__(self, student):
        return self.number_homeworks.__eq__(student.number_homeworks)
    
    def __ne__(self, student):
        return self.number_homeworks != student.number_homeworks
    
    def __lt__(self, student):
        return self.number_homeworks < student.number_homeworks
    
    def __gt__(self, student):
        return self.number_homeworks > student.number_homeworks
    
    def __le__(self, student):
        return self.number_homeworks <= student.number_homeworks
    
    def __ge__(self, student):
        return self.number_homeworks >= student.number_homeworks


Jonh = Student('Jonh', 'Adamson', 'male', 23, 183, 76, 123490, 2, 2, 17)
Katie = Student('Katie', 'Parson', 'female', 21, 173, 55, 123481, 2, 1, 17)
Tom = Student('Tom', 'Gilbert', 'male', 22, 170, 62, 123401, 3, 3, 21)
for st in (Jonh, Katie, Tom):
    print(f'{st.info()} has passed {st.number_homeworks} homeworks')
print('------------------------------')
print(f'Jonh == Katie -> {Jonh == Katie}')
print(f'Jonh != Tom -> {Jonh != Tom}')
print(f'Katie < Tom -> {Katie < Tom}')
print(f'Jonh > Tom -> {Jonh > Tom}')
print(f'Tom <= Katie -> {Tom <= Katie}')
print(f'Katie >= Jonh -> {Katie >= Jonh}')