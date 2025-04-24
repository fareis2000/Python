
letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'i' in letras:
        print('PARABENS')
        break

    print(letras)