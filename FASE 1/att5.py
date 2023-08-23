print("5 ) Peça ao usuário para inserir sua idade. Verifique se ele é menor de idade (menor que 18) ou não.\n")
idade = int(input("Digite sua idade\n"));
if(idade < 0):
  print("Viagem no tempo?");
elif(idade >= 18 and idade <= 100):
  print("Você já pode ser preso.");
elif(idade < 18 and idade > 0):
  print("Você é de menor.");
else:
  print("Quem é você?");