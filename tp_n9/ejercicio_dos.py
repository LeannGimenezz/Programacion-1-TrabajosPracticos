class Person:
    def __init__(self, name, age, dni):
        self.name=name
        self.age=age
        self.dni=dni
        
    def __str__(self):
        return f"Nombre: {self.name}, edad: {self.age} dni:{self.dni}"
    
class Account:
    def __init__(self, owner, quantity=0.0):
        self.owner=owner
        self.quantity=quantity
        
    def get_quantity(self):
        return self.quantity
    
    def show_info(self):
        print("Datos del titular")
        print(self.owner)
        print(f"Saldo disponible : {self.quantity} pesos")
        
    def enter(self, quantity):
        if quantity>0:
            self.quantity+=quantity
    
    def take_out(self, quantity):
        if quantity>0:
            self.quantity-=quantity
            

person1=Person("Juliano", 22, "43637501")
account1=Account(person1, 100.0)

account1.show_info()
account1.enter(10000)
account1.show_info()
account1.take_out(1000)
account1.show_info()