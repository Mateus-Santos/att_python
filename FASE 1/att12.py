print("12) Peça ao usuário um número e calcule sua sequência de Fibonacci até esse número.\n");
num = int(input("Digite o valor que deseja calcular em Fibonacci: \n"))
fibonnaci = [1]
soma = 0
j = 0
while(fibonnaci[-1] < num):
    soma = fibonnaci[j-1] + fibonnaci[j]
    fibonnaci.append(soma)
    j = j + 1
fibonnaci.insert(0, 1)
print(fibonnaci)