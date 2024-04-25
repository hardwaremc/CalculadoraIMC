#IMC = Peso / (Altura * Altura)

print("Academia MC Valinhos")
print("..........................")
print("Seja bem-vindo(a)!")

nome = input("Me diga, por favor, o seu nome: ")
idade = int(input("Agora preciso que você me informe a sua idade: "))
altura = float(input("Informe a sua altura: "))
nascimento = 2024 - idade
peso = float(input("Informe o seu peso: "))
IMC = peso / (altura * altura)

print("Olá, Senhor(a)", nome)
print("Sua idade é: ", idade, "anos.")
print("Você nasceu em: ", nascimento)
print("Sua altura é  de: ", altura, "metros.")
print("Seu peso é: ", peso)
print("Seu IMC é: {:.2f} kg/m²".format(IMC))