print("12) Peça ao usuário um número e calcule sua sequência de Fibonacci até esse número.\n");
num = int(input("Digite o valor que deseja calcular em Fibonacci: \n"))
fibonnaci = [1]
soma = 0
for j in range(num):
    print(j)
    soma = fibonnaci[j-1] + fibonnaci[j]
    fibonnaci.append(soma)
fibonnaci.insert(0, 1)
print(fibonnaci)