#Peça os coeficientes de uma equação do 2ºgrau e calcule as suas raízes

a = float(input("Digite o coeficiente a:")) 
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

delta = b**2 - 4*a*c

if delta < 0:
    print('A equação não possui raízes reais')
    exit()

x1 = (-b + delta**0.5) / (2*a)

x2 = (-b - delta**0.5) / (2*a)

print(f'As raízes da equação são: {x1} e {x2}')
