class Animal :

    def __init__(self, name):
        self.name = name
        

    def info(self):
            print("Animal Name:", self.name)
            
class Dog(Animal):
     def __init__(self, name, breed):
       
        super().__init__(name)
        self.breed = breed
     
     def details(self):
      print(self.name, "is a", self.breed)

z = Dog("Buddy", "Golden Retriever")
z.info()
     