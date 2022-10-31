""" Crie um simulador para a execução dos algoritmos de substituição de páginas. Para isso teremos 1 matriz com 10 linhas e
5 colunas para modelar as molduras de páginas na memória RAM e outra matriz 100 linhas e 5 colunas que vai representar
as páginas em disco. Os campos da matriz são:  Número de Página (N), Instrução (I), Dado (D), Bit de Acesso (R), Bit de
Modificação (M). """

from random import randint


def substituir_pag():
    print('Substituir página')


matriz_100x5 = []  # Matriz de páginas em disco
for cont in range(0, 100):
    n = cont  # A coluna N terá os números de 0 a 99, sequencialmente
    i = cont + 1  # A coluna I terá os números de 1 a 100, sequencialmente
    d = randint(1, 50)  # A coluna D terá números de 1 a 50, sorteados ale aleatoriamente
    r = 0  # A coluna R = 0
    m = 0  # A coluna M = 0
    matriz_100x5.append([n, i, d, r, m])
    print(matriz_100x5.__getitem__(cont))

print('==============================')

matriz_10x5 = []  # Matriz de molduras de páginas na memória RAM
for cont in range(0, 10):
    ind = randint(0, 99)  # Sorteia um índice da matriz 100x5
    matriz_10x5.append(
        matriz_100x5.__getitem__(ind))  # Adiciona a linha da matriz 100x5, referente ao índice sorteado, na matriz 10x5
    print(matriz_10x5.__getitem__(cont))

for c in range(0, 500):
    instrucao = randint(1,
                        100)  # Número de 1 a 100, referente a instrução (campo I) que está sendo requisitada para a execução na CPU
    esta_na_ram = False
    for linha in matriz_10x5:  # Pesquisa no campo I da matriz 10x5 para verificar se o valor da instrução está carregado na memória RAM
        if linha.__getitem__(1) == instrucao:  # Caso esteja, duas operações serão realizadas:
            linha.__setitem__(3, 1)  # O bit de acesso R vai receber o valor 1
            chance_modif = randint(0, 100)  # A página terá 30% de chance de sofrer uma modificação
            if chance_modif <= 30:  # Caso a probabilidade seja atingida, duas ações serão realizadas:
                linha.__setitem__(2, linha.__getitem__(
                    2) + 1)  # O campo Dado (D) será atualizado da seguinte maneira: D = D + 1
                linha.__setitem__(4, 1)  # O campo Modificado será atualizado: M = 1
            esta_na_ram = True
            break
    if not esta_na_ram:  # Caso o número de instrução sorteado não esteja presente na matriz 10x5
        substituir_pag()  # deverá ser utilizado um algoritmo de substituição de página para realizar a substituição
print('==============================')
for cont in range(0, 100):
    print(matriz_100x5.__getitem__(cont))
print('==============================')
for cont in range(0, 10):
    print(matriz_10x5.__getitem__(cont))