from timeit import timeit

def somal(n):
    soma = 0
    for i in range(n + 1):#ON
        soma += i
    return soma


if __name__ == "__main__":
    resultado = somal(10)
    print(resultado)

#qual o big o dessa função?

tempo = timeit('somal(10)' , globals=globals(), number=10000)
print(f"tempo de execução: {tempo} segundos para 100.000 execuçoes")