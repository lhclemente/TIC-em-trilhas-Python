"""
Nome: Lucas
Função: Carteiro 
Pega a carta na distribuidora => leva até a casa do destinatario => entrega na casa do destinatario 

f(x) = 2.x => Y
f(10) = 2.10 => 20
"""
def multiplica(numero, multiplicador):
    resultado = numero * multiplicador
    return resultado

print(multiplica(10, 2))
print(multiplica(20, 4))
print(multiplica(30, 6))
print(multiplica(40, 4))
print(multiplica(50, 8))
print(multiplica(60, 9))
print(multiplica(70, 12))
print(multiplica(80, 10))

#Issó é um função com parametros

def imprime(texto):
    print("O texto é", texto)

imprime("Clemente")


def dobrar(numero): 

    return numero * 2 

resultado = dobrar(5) 

print(resultado)