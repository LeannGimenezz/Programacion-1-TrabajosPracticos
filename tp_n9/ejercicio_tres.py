class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        
    def major_side(self):
        return max(self.side1, self.side2, self.side3)
    
    def triangle_type(self):
        if self.side1==self.side2==self.side3:
            return "Equilatero"
        elif self.side1==self.side2 or self.side1==self.side3 or self.side2 == self.side3:
            return "Isosceles"
        else:
            return "Escaleno"

def main():
    side1=float(input("Ingrese la longitud del lado 1: "))  
    side2=float(input("Ingrese la longitud del lado 2: "))
    side3=float(input("Ingrese la longitud del lado 3: "))
    
    triangle1=Triangle(side1, side2, side3)
    
    print(f"El lado mayor del triangulo es {triangle1.major_side()}") 
    print(f"El triangulo es {triangle1.triangle_type()}")
    
    
main()      