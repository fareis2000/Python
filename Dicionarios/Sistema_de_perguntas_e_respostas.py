# Lista de perguntas, onde cada pergunta é um dicionário contendo:
# - o enunciado da pergunta,
# - uma lista de opções de resposta,
# - e a resposta correta.
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# Variável que armazena a quantidade de respostas corretas
qtd_acertos = 0

# Loop que percorre cada pergunta na lista
for i, pergunta in enumerate(perguntas):
    # Mostra o número da questão e o enunciado
    print(f'Qustão: {i}\n {pergunta["Pergunta"]}\n')

    # Pega as opções da pergunta atual
    opcoes = pergunta['Opções']

    # Exibe as opções com um número para o usuário escolher
    for d, opcao in enumerate(opcoes):
        print(f'{d})', opcao)
    print()

    # Solicita ao usuário que escolha uma das opções
    escolha = input('Escolha uma opção: ')
    print()

    # Variáveis auxiliares para verificar se a resposta está correta
    acertou = False
    escola_int = None
    qtd_opcoes = len(opcoes)

    # Verifica se o usuário digitou um número
    if escolha.isdigit():
        escola_int = int(escolha)

    # Verifica se o número está dentro do intervalo válido de opções
    if escola_int is not None:
        if 0 <= escola_int < qtd_opcoes:
            # Verifica se a opção escolhida é igual à resposta correta
            if opcoes[escola_int] == pergunta['Resposta']:
                acertou = True

    # Mostra o resultado da resposta e atualiza o total de acertos
    if acertou:
        qtd_acertos += 1
        print('Acertou👍\n')
    else:
        print('Errou❌\n')

# Exibe o total de acertos ao final
print('Voce acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
