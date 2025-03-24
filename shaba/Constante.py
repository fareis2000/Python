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
big_o = [np.ones(n.shape)]

#exibe o array e a complexidade constatnte
print("Array n:")
print(n)
print("/nComplexidade Constante (0(1)):")
print(big_o[0])
#plota a complexidade constante
plt.plot(n,big_o[0], label=labels[0])

plt.xlabel('n') #define o rotulo do eixo x
plt.ylabel("Tempo de execução") #define o rotulo do eixo y
plt.title("Comparação de complexividade") #Define o titulo do grafico
plt.legend()#Adiciona a legenda ao gráfico
plt.grid(True)# Adiciona uma grade ao gráfico
plt.show()#exibe o gráfico


