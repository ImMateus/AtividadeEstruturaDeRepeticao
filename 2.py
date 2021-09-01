"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

user = input("Usuário: ")
senha = input("Senha: ")

while user == senha:
    senha = input("A senha não pode ser igual ao nome de usuário: ")

print(f"A usuário é: {user}")
print(f"A senha é: {senha}")
