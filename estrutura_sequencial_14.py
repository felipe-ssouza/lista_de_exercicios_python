# -*- coding: utf-8 -*-
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diario de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que voce faca um programa que leia a variavel peso (peso de peixes) e calcule o excesso. Gravar na variavel excesso a quantidade de quilos alem do limite e na variavel multa o valor da multa que João devera pagar. Imprima os dados do programa com as mensagens adequadas.


peso = float(input('Peso (K): '))

if peso > 50 :
    excesso = peso - 50
    multa = excesso * 4
    print("Multa por Excesso de Peso: R$", multa)
else:
    print("OK!")
