from timeit import timeit


#o objetivo é criar uma lista com 1000

def lista1():
    lista = []
    for i in range(1000):#ON
        lista.append(i)
    return lista

if __name__ == "__main__":
    resultado = lista1()
    print(resultado)
    print(len(resultado))

number = 1000

tempo = timeit(lista1, number=number)
print(f"tempo de execução: {tempo} segundos para {number} execuçoes")