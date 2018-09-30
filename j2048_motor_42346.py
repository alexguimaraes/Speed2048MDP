# -*- coding: utf-8 -*-
from random import random
from random import choice


# reinicia o jogo, colocando dois 2/4 numa grelha vazia, pontos a 0 e booleanos de fim de jogo a false
def novo_jogo():
    grelha = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    fim = False
    vitoria = False
    pontos = 0
    inserir_2ou4(grelha)
    inserir_2ou4(grelha)
    return grelha, fim, vitoria, pontos


# devolve o valor da grelha na coordenada fornecida
def valor(jogo, linha, coluna):
    # jogo Ã© o tuplo (grelha, fim, vitoria, pontos)
    return jogo[0][linha - 1][coluna - 1]


# devolve o boleano vitoria que determina se o jogador ganhou ou nao
def ganhou_ou_perdeu(jogo):
    return jogo[2]


# devolve o booleano fim que determina se o jogo terminou ou nao
def terminou(jogo):
    return jogo[1]


# devolve os pontos feitos nas somas dos numeros
def pontuacao(jogo):
    return jogo[3]


# obter um 2 ou um 4 aleatoriamente, com probabilidades 90% e 10%
def get_2ou4():
    x = random()
    if x > 0.1:
        return 2
    else:
        return 4


# devolve as posicoes nao ocupadas da grelha
def get_posicoes_vazias(grelha):
    posicoes_vazias = []
    for linha in [0, 1, 2, 3]:
        for coluna in [0, 1, 2, 3]:
            if grelha[linha][coluna] == 0:
                posicoes_vazias.append([linha, coluna])

    return posicoes_vazias


# vai buscar um 2/4 e adiciona a uma posicao vazia
def inserir_2ou4(grelha):
    dois_ou_quatro = get_2ou4()
    posicoes_vazias = get_posicoes_vazias(grelha)
    posicao_vazia = choice(posicoes_vazias)
    # indices da posicao vazia
    linha = posicao_vazia[0]
    coluna = posicao_vazia[1]
    grelha[linha][coluna] = dois_ou_quatro


# devolve uma nova lista tendo copiado os valores para o inicio e acrescentando zeros no final
def mover_esquerda(uma_lista):
    resultado = []
    lenlista = len(uma_lista)
    for indice in range(lenlista):
        valor = uma_lista[indice]
        if valor != 0:
            resultado.append(valor)
    while len(resultado) < lenlista:
        resultado.append(0)
    return resultado


# se existem dois numeros iguais adjacentes soma os valores e incrementa os pontos
def somar_esquerda(uma_lista):
    resultado = []
    lenlista = len(uma_lista)
    pontos = 0
    indice = 0
    while indice < lenlista - 1:
        valor = uma_lista[indice]
        if valor == uma_lista[indice + 1]:
            soma = valor + valor
            resultado.append(soma)
            pontos = pontos + soma
            indice = indice + 2
        else:
            resultado.append(valor)
            indice = indice + 1
    if indice == lenlista - 1:
        resultado.append(uma_lista[indice])
    while len(resultado) < lenlista:
        resultado.append(0)
    return resultado, pontos


# devolve uma copia da grelha
def copiar_grelha(grelha):
    resultado = []
    numero_linhas = len(grelha)
    numero_colunas = len(grelha[0])
    for l in range(numero_linhas):
        nova_linha = []
        for c in range(numero_colunas):
            nova_linha.append(grelha[l][c])
        resultado.append(nova_linha)
    return resultado


# verifica se ocurreu um movimento e se sim acrescenta um 2/4
def atualizar_grelha(grelha_inicial, grelha):
    diferentes = False
    numero_linhas = len(grelha)
    numero_colunas = len(grelha[0])
    for l in range(numero_linhas):
        for c in range(numero_colunas):
            if grelha_inicial[l][c] != grelha[l][c]:
                diferentes = True
    if diferentes:
        posicoes_vazias = get_posicoes_vazias(grelha)
        if len(posicoes_vazias) != 0:
            inserir_2ou4(grelha)


# encosta todos os numeros a esquerda, soma os iguais adjacentes horizontalmente, verifica se houve movimento e verifica
# se o jogo acabou
def esquerda(jogo):
    grelha = jogo[0]
    fim = jogo[1]
    vitoria = jogo[2]
    pontos = jogo[3]
    grelha_inicial = copiar_grelha(grelha)
    numero_linhas = len(grelha)
    for l in range(numero_linhas):
        linha = grelha[l]
        linha2 = mover_esquerda(linha)
        (linha3, pontos_a_adicionar) = somar_esquerda(linha2)
        grelha[l] = linha3
        pontos = pontos + pontos_a_adicionar
    atualizar_grelha(grelha_inicial, grelha)
    if get_fim(grelha):
        print("Lost")
        fim = True
    elif get_vitoria(grelha):
        print("Won")
        vitoria = True
    return grelha, fim, vitoria, pontos


# reverte as linhas faz um movimento esquerda e volta a reverter as linhas para ter movido para a direita
def direita(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_revertida = reverte_linhas(grelha)
    jogo_revertido = (grelha_revertida, fim, vitoria, pontos)
    jogo_revertido_atualizado = esquerda(jogo_revertido)
    (grelha, fim, vitoria, pontos) = jogo_revertido_atualizado
    grelha_revertida = reverte_linhas(grelha)
    jogo_atualizado = (grelha_revertida, fim, vitoria, pontos)
    return jogo_atualizado


# troca linhas com colunas faz um movimento esquerda e volta a transpor para ter movido para cima
def acima(jogo):
    print("acima")
    print(jogo[0])
    (grelha, fim, vitoria, pontos) = jogo

    grelha_transposta = trocar_linhas_com_colunas(grelha)

    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)

    jogo_transposto_atualizado = esquerda(jogo_transposto)

    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado

    grelha_transposta = trocar_linhas_com_colunas(grelha)

    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)

    return jogo_atualizado


# troca linhas com colunas faz um movimento direita e volta a transpor para mover na direcao oposta do
def abaixo(jogo):
    print("abaixo")
    (grelha, fim, vitoria, pontos) = jogo

    grelha_transposta = trocar_linhas_com_colunas(grelha)

    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)

    jogo_transposto_atualizado = direita(jogo_transposto)

    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado

    grelha_transposta = trocar_linhas_com_colunas(grelha)

    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)

    return jogo_atualizado

# troca os valores finais das linhas pelos iniciais para o movimento esquerda servir para mover para a direita
def reverte_linhas(grelha):
   
    n_linhas = len(grelha)

    for l in range(n_linhas):
        grelha[l].reverse()

    return grelha




# troca as linhas com as colunas para o movimento esquerda servir para movimentar na vertical
def trocar_linhas_com_colunas(grelha):
   
    glista = []

    n_linhas = len(grelha)
    
    for linha in range(n_linhas):
        glista_coluna = []
        for coluna in grelha:
            glista_coluna.append(coluna[linha])
        glista.append(glista_coluna)

    grelha = glista

    return grelha


# verifica se existe um 2048 na grelha (condicao de vitoria)
def get_vitoria(grelha):
    numero_linhas = len(grelha)
    numero_colunas = len(grelha[0])
    vitoria = False
    for l in range(numero_linhas):
        for c in range(numero_colunas):
            if grelha[l][c] == 2048:
                vitoria = True
    return vitoria


# verifica se e possivel efetuar movimentos na horizontal/vertical vendo se existem iguais adjacentes nas linhas/colunas
def ha_iguais_adjacentes(grelha):
    numlinhas = len(grelha)
    numcolunas = len(grelha[0])
    iguais = False
    for l in range(numlinhas):
        for c in range(numcolunas - 1):
            if grelha[l][c] != 0 and grelha[l][c] == grelha[l][c + 1]:
                iguais = True
    for l in range(numlinhas - 1):
        for c in range(numcolunas):
            if grelha[l][c] != 0 and grelha[l][c] == grelha[l + 1][c]:
                iguais = True
    return iguais


# verifica se gameover por nao haver posicoes vazias nem movimentos possiveis
def get_fim(grelha):
    end = False
    ha_posicoes_vazias = True
    posicoes_vazias = get_posicoes_vazias(grelha)
    if len(posicoes_vazias) == 0:
        ha_posicoes_vazias = False
    if not ha_posicoes_vazias and not (ha_iguais_adjacentes(grelha)):
        end = True
    return end
