TAMANHO = 65536


def criar_tabela_hash():
    tabela_hash = [[] for _ in range(TAMANHO)]
    return tabela_hash


# one_at_a_time (JENKINS)
def funcao_hash(chave):
    indice = 0
    i = len(chave) - 1
    while i >= 0:
        indice += ord(chave[i])
        indice += (indice << 10)
        indice ^= (indice >> 6)
        i -= 1
    indice += (indice << 3)
    indice ^= (indice >> 11)
    indice += (indice << 15)
    return indice % TAMANHO


def inserir(tabela_hash, objeto):
    chave = objeto[0]
    indice = funcao_hash(chave)
    chave_existe = False
    bucket = tabela_hash[indice]
    for i, kv in enumerate(bucket):
        k, v = kv
        if chave == k:
            chave_existe = True
            break
    if chave_existe:
        bucket[i] = (chave, objeto)
    else:
        bucket.append((chave, objeto))


def buscar(tabela_hash, chave):
    indice = funcao_hash(chave)
    bucket = tabela_hash[indice]
    for i, kv in enumerate(bucket):
        k, v = kv
        if chave == k:
            return v


def ler_entrada(tabela_hash):
    print('Digite \'sair\' para fechar o programa')
    while True:
        entrada = input('Entrada: ').lower()
        if entrada == 'sair':
            break
        else:
            busca = buscar(tabela_hash, entrada)
            if busca is None:
                print('Termo nao presente no dicionario\n')
            else:
                print('Chave:', busca[0])
                print('Descrição:', busca[1], '\n')
