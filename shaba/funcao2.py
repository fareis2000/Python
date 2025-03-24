from timeit import timeit


def soma2(n):
    return (n * (n + 1)) / 2#1


if __name__ == "__main__":
    resultado = soma2(10)
    print(resultado)

#comparar o tempo de duas funçoes

tempo = timeit('soma2(10)' , globals=globals(), number=10000)
print(f"tempo de execução: {tempo} segundos para 100.000 execuçoes")