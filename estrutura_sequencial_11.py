# Faca um Programa que peca 2 numeros inteiros e um numero real. Calcule e mostre:
#
#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo.


numero1 = int(input('Entre com o primero numero Inteiro: '))
numero2 = int(input('Entre com o segundo numero Inteiro: '))
numero3 = float(input('Entre com um numero Real: '))

print("Produto do dobro do primeiro numero com metade do segundo: ", (numero1*2)*(numero2/2))
print("Soma do triplo do primeiro com o terceiro: ", (numero1*3) + numero3)
print("Terceiro elevado ao cubo: ", numero3 * numero3 * numero3)
