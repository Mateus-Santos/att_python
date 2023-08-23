print("4) Crie dois conjuntos, conjunto1 e conjunto2, com alguns elementos comuns e alguns diferentes. "
      "Crie um novo conjunto, resultado, que contenha todos os elementos que estão presentes em apenas"
      "um dos conjuntos.")
conjunto1 = {"A", "B", "C", "D", "E"}
conjunto2 = {"D", "E", "F"}
resultado = {}
resultado = (conjunto1 ^ conjunto2)
print(resultado)