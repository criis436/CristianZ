
# credito=0
# print("ingrese su ingreso mensual")

# Ingresos_mesual=int(input(
#     Ingrese si





# nivel_educacional=int(input('''
#     ingrese su nivel nivel_educacional:
#     1.Basico
#     2.medio 
#     3.superior'''))
# if 


import random as rd

num1=int(input("ingrese un numero: "))
num2=int(input("ngrese un numero mayor al anterior: "))

if num2<num1:
    print("error")
else:
    num_final=rd.randint(num1,num2)
    print("su numero final es: ", num_final)
    for i in range (num_final):
        print("▄")
