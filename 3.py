"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = str(input("Coloque um nome que tenha mais de 3 caracteres: "))
while len(nome) <= 3:
    nome = str(input("For favor, um nome com mais de 3 caracteres: "))
    
idade = float(input("Coloque sua idade: "))
while idade < 0 or idade > 150:
    idade = float(input("A idade deve ser entre 0 e 150: "))
    
salar = float(input("Coloque seu salário: "))
while salar <= 0:
    salar = float(input("O salário tem que ser maior que 0: "))
salar1 = str(salar)

sexo = str(input("Coloque seu sexo: (F ou M) "))
while sexo != "f" and sexo != "F" and sexo != "m" and sexo != "M":
    sexo = str(input("O sexo tem que sere F ou M: "))

status = str(input("Seu estado civil: (s , c, v, d) "))
while status != "s" and status != "S" and status != "c" and status != "C" and status != "v" and status != "V"\
        and status != "d" and status != "D":
    status = str(input("Deve ser S, C, V, ou D: "))

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salar1}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {status}")

