numeros = []
print("11) Peça ao usuário para inserir três números. Determine o maior e o menor entre eles.\n\n")
numero = int(input("Digite o primeiro número:\n"))
numeros.append(numero)
num1 = int(input("Digite o segundo número:\n"))
numeros.append(numero)
num3 = int(input("Digite o terceiro número:\n"))
numeros.append(numero)
maiores = [0,0,0]
for x in range(len(numeros)):
    for y in range(len(numeros)):
        if(numeros[y] > numeros[x]):
            maiores.append(numeros(x))
    
print("Maiores: ", maiores)