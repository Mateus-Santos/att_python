print("10) Crie uma variável chamada saldo e atribua um valor inicial. Simule operações de depósito e saque, atualizando o saldo.\n")
saldo = float(input("Digite o seu saldo:\n"))
opcao = int(input("Digite a opção que deseja acessar [1] SAQUE [2] DEPOSITO"))
if(opcao == 1):
  saque = float(input("Digite o valor do saque:\n"))
  saldo = saldo - saque;
  print("Seu saldo atual é de: ", saldo);
elif(opcao == 2):
  deposito = float(input("Digite o valor do deposito:\n"))
  saldo = saldo + deposito
  print("Seu saldo atual é de: ", saldo)