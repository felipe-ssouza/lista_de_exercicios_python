# -*- coding: utf-8 -*-
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)


tamanho = int(input('Tamanho do arquivo para download (MB): '))

velocidade = int(input('Velocidade do link de internet (Mbps): '))

tempo = tamanho / velocidade / 60

print("Tempo aproximado de download: %2.f" % tempo , "minutos")
