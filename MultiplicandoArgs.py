def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

muti1 = mult(1, 2, 3, 4, 5)
print(muti1)

numeros2 = [1, 2, 3, 4, 5]
numeros = 1, 2, 3, 4, 5

outramult2 = mult(*numeros2)
print(outramult2)
outramult = mult(*numeros)
print(outramult)

