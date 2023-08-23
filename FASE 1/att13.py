from random import randint
print("13)  Crie um jogo de adivinhação em que o computador escolhe um número entre 1 e 100, "
      "e o jogador tenta adivinhar. Dê dicas se o palpite estiver errado e permita que ele" 
      "tente novamente\n")

numeros = []

for x in range(1,101):
    numeros.append(x)
escolhido = randint(1,100)
print(escolhido)
num = int(input("Digite tente advinhar o valor escolhido.\n"))
while(num != escolhido):
    print("Errou!!\n")
    if(num < escolhido):
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")
    num = int(input("Digite novamente e tente advinhar o valor escolhido.\n"))
print("!!!ACERTOU!!!")