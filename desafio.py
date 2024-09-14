#criar uma lista vasia, que possa ser adicionado 5 números inteiros 

def receber_entrada():
    lista = []

    while(True):
        crie_uma_lista = int(input("insira um número (0 para sair): "))

        if (crie_uma_lista == 0):
            return lista
        
        lista.append(crie_uma_lista)

l = receber_entrada()
print(l)