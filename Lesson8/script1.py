'''
Написать класс animals, который включает общие признаки и поведения
животных. От animals наследовать класс mammals, который включает
общие признаки и поведения млекопитающих. От mammals наследовать
human, cat, dog, у каждого свои признаки и поведения
'''
class animals:
    def __init__(self, type, age, height, weight):
        self.type = type
        self.age = age
        self.height = height
        self.weight = weight

    def grow(self):
        print(f'{self.type} grows, moves and lives for {self.age} years')
    
    def reproduce(self):
        print(f'{self.type} can reproduce')
    
    def eat(self):
        print(f'{self.type} can breathe and eat')


class mammals(animals):
    def __init__(self, type, age, height, weight, gender, sound):
        super().__init__(type, age, height, weight)
        self.gender = gender
        self.sound = sound
    
    def sounds(self):
        print(f'{self.type} makes {self.sound} sounds')


class cat(mammals):
    def __init__(self, type, age, height, weight, gender, sound, name, color):
        super().__init__(type, age, height, weight, gender, sound)
        self.name = name
        self.color = color
    
    def walk_at_night(self):
        print(f'{self.type} {self.name} likes to walk at night and disturb sleep')


class dog(mammals):
    def __init__(self, type, age, height, weight, gender, sound, name, color):
        super().__init__(type, age, height, weight, gender, sound)
        self.name = name
        self.color = color
    
    def wait(self):
        print(f'{self.type} {self.name} waits for the owner')


class human(mammals):
    def __init__(self, type, age, height, weight, gender, sound, first_name, last_name, position):
        super().__init__(type, age, height, weight, gender, sound)
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
    
    def grow(self):
        print(f'{self.first_name} grows, moves and lives for {self.age} years')
    
    def say(self, text):
        print(f'{self.first_name} {self.last_name} says: {text}')
    
    def activity(self):
        if self.position == 'student':
            print(f'{self.first_name} {self.last_name} studies')
        elif self.position == 'employee':
            print(f'{self.first_name} {self.last_name} works')
        elif self.position == 'kindergarten student':
            print(f'{self.first_name} {self.last_name} goes to kindergarten')


Jonh = human('Human', 23, 183, 76, 'male', 'speech', 'Jonh', 'Konor', 'student')
Jonh.grow()
Jonh.activity()

cat_Emily = cat('Cat', 3, 6.8, 65, 'female', 'meow', 'Emily', 'black')
cat_Emily.sounds()
cat_Emily.walk_at_night()