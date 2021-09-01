"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""

print("Digite um número entre 0 e 10")
num = float(input())

while num < 0 or num > 10:
    num = float(input("Inválido, por favor coloque um valor válido: "))
