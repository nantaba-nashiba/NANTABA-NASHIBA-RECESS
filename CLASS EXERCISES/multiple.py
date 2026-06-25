class Class1:
    def w(self):
        print("This is Class1 method w")

class Class2(Class1):
    def w(self):
        print("This is Class2 method w")

class Class3(Class1):
    def w(self):
        print("This is Class3 method w")

class Class4(Class2, Class3):
    def w(self):
        print("This is Class4 method w")

        obj = Class4()
        obj.w()
        