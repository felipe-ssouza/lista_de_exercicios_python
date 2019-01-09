# -*- coding: utf-8 -*-
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# 1 litro cada 6 metros quadrados
# latas 18 litros 80 reais
# latas 3,6 litros 25 reais

area = int(input('Informe o tamanho da área a ser pintada (m2): '))

litros = area / 6

if litros <= 18 :
    latas = 1
else:
    latas = litros / 18

precoLatas = latas * 80

if litros <= 3.6 :
    galoes = 1
else:
    galoes = litros / 3.6

precoGaloes = galoes * 25


print("Preço da tinta em latas (18 litros): R$ %2.f" % precoLatas,
        "\nPreço da tinta em galões (3.6 litros): R$ %2.f" % precoGaloes)
