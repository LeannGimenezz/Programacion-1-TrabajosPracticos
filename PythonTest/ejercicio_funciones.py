def sumDigits(number):
    add=0
    while number!=0:
        resto=number%10
        number//=10
        add+=resto
        
    return add