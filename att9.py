print("9) Implemente um contador regressivo "
      "onde o usuário insere um número e o programa exibe a contagem regressiva até zero, "
      "mostrando cada número.\n")
numero = int(input("Digite um número:\n"))
print("\n",numero)
while(numero > 0):
  numero = numero - 1
  print(numero)