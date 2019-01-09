# -*- coding: utf-8 -*-
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# 18 litros lata

# 3 metros quadrados 1 litro

# preco da lata 80.00

tamanho = float(input('Tamanho da área a ser pintada (m2): '))

litros = tamanho / 3

if litros <= 18 :
    latas = 1
else:
    latas = litros / 18

preco = latas * 80

print("Quantidade de litros:  %.2f" % litros, "\nQuantidade de latas: ", round(latas), "\nPreço total: R$ %.2f" % preco)
