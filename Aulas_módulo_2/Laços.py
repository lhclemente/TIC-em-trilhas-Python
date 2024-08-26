"""
Lista_de_compras = ["Leite", "Ovos", "Açucar", "Uranio", "Etanol"]
for item in Lista_de_compras: 
    print("Peguei o item", item)
"""
#Exemplo de laço com a variavel while

numero = 0;

while True:
    print("Número", numero)
    numero = numero + 1

    if   numero % 2 == 0: #Significa que o número é par
        print(numero, "é par")
        continue

    print(numero, "é impar")
    break