print("4 ) Peça ao usuário para inserir um número.\n"
      "Verifique se o número é positivo, negativo ou zero e exiba uma mensagem apropriada.\n")
num = int(input("Digite o numero:\n"))
if(num < 0):
  print(num, "é negativo:")
elif(num == 0):
  print(num, "é igual a 0:")
else:
  print(num, "é positivo")