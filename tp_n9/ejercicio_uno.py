class Person:
    def __init__(self, name="", age=0, dni=""):
        self.name=name
        self.age=age
        self.dni=dni
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name=name
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if age >=0 :
            self.age=age
        else:
            print("La edad no puede ser un valor negativo")
        
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        if len(dni)==8:
            self.dni=dni
        else:
            print("Formato invalido de dni")
            
    def showPerson(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Dni: {self.dni}")
        
    def isAdult(self):
        if self.age>=18:
            return True
        else:
            return False
        
person1=Person("Juliano", 22, "43637501")
person2=Person()

person2.set_age(17)

person1.showPerson()
print(person1.isAdult())

person2.showPerson()
print(person2.isAdult())