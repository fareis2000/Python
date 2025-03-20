import numpy as np
import matplotlib.pyplot as plt


def bisseccao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos nos extremos do intervalo.")

    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


def falsa_posicao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos nos extremos do intervalo.")

    for _ in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c

def func(x):
    return x ** 3 - 4 * x - 9


a, b = 2, 3

raiz_bissecao = bisseccao(func, a, b)
raiz_falsa_posicao = falsa_posicao(func, a, b)

print(f"Raiz pela Bissecção: {raiz_bissecao}")
print(f"Raiz pela Falsa Posição: {raiz_falsa_posicao}")

# Criando gráficos
x = np.linspace(a - 1, b + 1, 400)
y = func(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='f(x)')
plt.axhline(0, color='black', linewidth=1)
plt.scatter([raiz_bissecao, raiz_falsa_posicao], [0, 0], color=['red', 'blue'], label=['Bissecção', 'Falsa Posição'])
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Métodos Numéricos para Encontrar Raízes')
plt.grid()
plt.show()
