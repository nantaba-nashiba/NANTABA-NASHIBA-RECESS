class Animal :

    def __init__(self, name):
        self.name = name
        

    def info(self):
            print("Animal Name:", self.name)
            
class Dog(Animal):
    def sound(self):
        print(self.name,"barks")

w=Dog("Buddy")
w.info()
w.sound()
