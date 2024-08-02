import random


def sorteio_unitario(nomes):
    nomes_list = nomes.split(',')
    numero_sorteado = random.randrange(0, len(nomes_list))
    return nomes_list[numero_sorteado].strip()

def sorteio_ordenado(nomes):
    # import ipdb; ipdb.set_trace(context=10)
    nomes_list = nomes.split(',')
    random.shuffle(nomes_list)
    return nomes_list
