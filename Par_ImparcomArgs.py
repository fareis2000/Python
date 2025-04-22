def parimpar(*args):

    for numero in args:
        resto = numero % 2
        if resto == 0:
            print(numero, "é par")
        else:
            print(numero, "é impar")


parimpar(1, 2, 3, 4, 5)

numeros = 1, 2, 3, 4, 5

parimpar(*numeros)
