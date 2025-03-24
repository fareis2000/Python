

#Feito Por Fabio Cesar Reis de Carvalho



#importa a função log da biblioteca math
from math import log
#importa a biblioteca numpy para operações matematicas
import numpy as np
#importa a bibliotecs matplotlib para Gráficos
import matplotlib.pyplot as plt

#criar um array de 100 pontos entre 1 e 10
n = np.linspace(1, 10, 100)

#Define os rótulos para cada tipo de complexidade
labels = ['Costante', 'Logarithmic','Linear','Log linear', 'Quedratic', 'Cubic', 'Exponencial' ]

#vai virar 100 números 1s,lista contendo a complexidade constante
big_o = [
    np.ones(n.shape),# Lista Contendo a complexidade constante np.ones(n.shape)
    np.log(n), # Lista Contendo a complexidade constante np.log(n)
    n, # Lista Contendo a complexidade constante n
    n * np.log(n), # Lista Contendo a complexidade linear logaritimica n * np.log(n)
    n ** 2, # Lista Contendo a complexidade Quadratica n * n
    n ** 3, # Lista Contendo a complexidade Cubica n * n * n
    2 ** n  # Lista Contendo a complexidade Exponencial n ** n
]

#exibe o array e a complexidade constatnte
print("Array n:")
print(n)

print("/nComplexidade Constante (0(1)):")
print(big_o[0])

print("/nComplexidade Logsritimica (0(log(n))):")
print(big_o[1])

print("/nComplexidade Logsritimica (n):")
print(big_o[2])

print("/nComplexidade Log Linear (n * np.log(n)):")
print(big_o[3])

print("/nComplexidade Quadratica (n ^ 2)")
print(big_o[4])

print("/nComplexidade Cubica (n ^ 2)")
print(big_o[5])

print("/nComplexidade Exponencial (n ** n)")
print(big_o[6])

#plota a complexidade constante
plt.plot(n,big_o[0], label=labels[0])
#plota a complexidade Logaritimica
plt.plot(n,big_o[1], label=labels[1])
#plota a complexidade Constante
plt.plot(n,big_o[2], label=labels[2])
#plota a complexidade Log Linear
plt.plot(n,big_o[3], label=labels[3])
#plota a complexidade quadratica
plt.plot(n,big_o[4], label=labels[4])
#plota a complexidade Cubica
plt.plot(n,big_o[5], label=labels[5])
#plota a complexidade Exponencial
plt.plot(n,big_o[6], label=labels[6])

plt.xlabel('n') #define o rotulo do eixo x
plt.ylabel("Tempo de execução") #define o rotulo do eixo y
plt.title("Comparação de complexividade") #Define o titulo do grafico
plt.legend()#Adiciona a legenda ao gráfico
plt.grid(True)# Adiciona uma grade ao gráfico
plt.show()#exibe o gráfico