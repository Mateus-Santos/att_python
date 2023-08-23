print("7) Peça ao usuário um número e imprima sua tabuada de multiplicação de 1 a 10 usando um loop for")
numero = int(input("Digite o número que deseja multiplicar."))
for num in range(1,11):
  print(num, " x ", numero, " = ", numero*num)