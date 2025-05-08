from xml.dom import NoModificationAllowedErr


class no:
# define uma função
# __init__ é o contrutor da classe nó
# self convensão - para referir a instancia da classe
    def __init__(self, valor):
        self.valor = valor  # armazena o  valor do nó
        self.esquerda = None #inicializa a instância para o nó esq
        self.direita = None #inicializa a instância para o nó dir
# metodo para mostrar o valor do nó
    def mostra_no(self):
        print(self.valor)

#Definição da classe ArvoreBinariaBusca, que representa a árvore de busca
#Esta classe contém métodos para inserir valores e exibir as ligações
class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None #inicializa a raiz da arvore como vazia (None)
        self.ligacoes = [] #Lista para armazenar as ligações entre os nó para visualizar

        #metodo para inserir um novo valor na arvore
    def inserir(self,valor):
        novo = no(valor) #cria um novo nó com valor passado
        if self.raiz is None: #se a arvore estiver vazia
            self.raiz = novo #a raiz recebe o valor do novo
        else:
            atual = self.raiz #Começa a busca a partir da raiz
            while True:
                pai = atual #armazena o nó atual como pai
                if valor < atual.valor: #se o valor for menor que o nó atual
                    atual = atual.esquerda # move para o nó filho do nó atual
                    if atual is None: # se não houver nó a esquerda
                        pai.esquerda = novo # insere o novo nó á esquerda do pai
                        self.ligacoes.append(str(pai.valor) + ' -> ' + str(novo.valor))#adiciona um item a uma lista
                        return
                else: # Se o valor for >= ao valor do nó atual
                    atual = atual.direita #move para o nó filho da direita
                    if atual is None: #se não houver nó a direita
                        pai.direita = novo # insere um novo nó á direita do pai
                        self.ligacoes.append(str(pai.valor) + ' -> ' + str(novo.valor))
                        return


# metodo para percorrer e exibir todos os nos da arvore esquerda.
    def mostrar_esquerda(self, no):
        if no: #se o nó atual não for None
            print(no.valor) #exibe o valor do nó final
            self.mostrar_esquerda(no.esquerda) #percorre a subaarvore direita
            self.mostrar_esquerda(no.direita) #percorre a subaarvore esquerda

# metodo para percorrer e exibir todos os nos da arvore direita.
    def mostrar_direita(self, no):
        if no: #se o nó atual não for None
            print(no.valor) #exibe o valor do nó final
            self.mostrar_direita(no.direita) #percorre a subaarvore direita
            self.mostrar_direita(no.esquerda) #percorre a subaarvore esquerda


#metodo para exibir todas as ligações entre os nós
    def mostrar_ligacoes(self):
     print("\nÁrvore de ligações:")
     for ligacao in self.ligacoes: #faz a interação sobre a ligações
         print(ligacao) # Exibe cada ligação

# exemplo de uso de arvore binaria de busca
arvore = ArvoreBinariaBusca() #cria uma nova arvore binaria de busca

#inserção dos valores na arvore
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

# exibe todos os nós da subarvore da raiz
print("Todos os nós da esquerda:")
arvore.mostrar_esquerda(arvore.raiz.esquerda)

# exibe todos os nós da subarvore direita da raiz
print("\nTodos os nós da direita:")
arvore.mostrar_direita(arvore.raiz.direita)

# exibe a árvore de ligações
arvore.mostrar_ligacoes()