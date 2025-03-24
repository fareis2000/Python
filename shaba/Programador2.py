import timeit

def lista2():
    return range(1000)#1

if __name__ == "__name__":
    resultado = lista2()
    print(list(resultado))
    print(len(list(resultado)))


number = 1000
tempo = timeit.timeit(lista2, number=number)
print(f"tempo de execução: {tempo} segundos para {number} execuçoes")