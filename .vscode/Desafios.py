# DESAFIO 1: Filtros Lógicos e Conjuntos

# 1. Criando o Conjunto A: x > 0 e x < 4


# conjunto_a = set(range(1, 4))

# conjunto_b = {2, 4, 6, 8, 10}

# interseccao = conjunto_a & conjunto_b

# print(f"Os elementos do Conjunto A são: {conjunto_a}")
# print(f"Os elementos do Conjunto B são: {conjunto_b}")

# numero_encontrado = list(interseccao)[0]
# print(f"\n=> O número que pertence à intersecção de A e B é o: {numero_encontrado}")    


# # DESAFIO 2: Topologia de Grafos e JSON

# # Criando a estrutura hierárquica (3 níveis, 5 vértices)


# import json

# arvore_topologia = {
#     "vertice": "A",
#     "filhos": [
#         {
#             "vertice": "B",
#             "filhos": [
#                 {"vertice": "D"},
#                 {"vertice": "E"}
#             ]
#         },
#         {
#             "vertice": "C",
#             "filhos": []
#         }
#     ]
# }


# def desenhar_arvore(no, nivel=0):
    
#     if nivel == 0:
#         prefixo = "🌳 Raiz: "
#     else:
#         prefixo = "    " * (nivel - 1) + " └── "    
#     print(prefixo + no["vertice"])
    
#     if "filhos" in no:
#         for filho in no["filhos"]:
#             desenhar_arvore(filho, nivel + 1)

# print("\n--- Visualização da Árvore Genealógica ---")
# desenhar_arvore(arvore_topologia)


# DESAFIO 3: Fecho de Kleene e Validação de Inputs


# alfabeto = {'0', '1'}

# def pertence_fecho_kleene(palavra):
    
#     return all(simbolo in alfabeto for simbolo in palavra)

# def pertence_fecho_positivo(palavra):
    
#     return len(palavra) > 0 and all(simbolo in alfabeto for simbolo in palavra)

# palavra_teste = "0101"
# palavra_vazia = ""  

# print("--- RESULTADOS DO DESAFIO 3 ---")
# print(f"1) '0101' pertence a Σ* ? -> {pertence_fecho_kleene(palavra_teste)}")
# print(f"2) Epsilon (vazio) pertence a Σ+ ? -> {pertence_fecho_positivo(palavra_vazia)}")


# DESAFIO 3: Extra

# alfabeto = {'0', '1'}

# def pertence_fecho_kleene(palavra):
#     return all(simbolo in alfabeto for simbolo in palavra)

# def pertence_fecho_positivo(palavra):
#     return len(palavra) > 0 and all(simbolo in alfabeto for simbolo in palavra)

# print("--- VALIDADOR DE ALFABETO BINÁRIO ---")
# print("Regra: O alfabeto só aceita os símbolos '0' e '1'.\n")

# # A função input() pausa o código e espera você digitar algo no terminal
# palavra_usuario = input("Digite uma sequência aleatória (ou aperte Enter para testar o vazio): ")

# print(f"\nVocê digitou: '{palavra_usuario}'")

# # Analisando a palavra que você digitou
# resultado_kleene = pertence_fecho_kleene(palavra_usuario)
# resultado_positivo = pertence_fecho_positivo(palavra_usuario)

# print(f"1) Pertence ao Fecho de Kleene (Σ*) ? -> {resultado_kleene}")
# print(f"2) Pertence ao Fecho Positivo (Σ+) ? -> {resultado_positivo}")


# DESAFIO 4: Alfabetos e Regex na Prática
# Onde L é o conjunto de palavras sobre Σ = {a, b} que contêm o sufixo exato 'bb'[cite: 1].

# import re

# def pertence_a_linguagem(w):

#     padrao = r'^[ab]*bb$'
#     return bool(re.match(padrao, w))


# palavra_1 = "ababb"  
# palavra_2 = "aba"    

# print("--- VALIDAÇÃO DA LINGUAGEM L (SUFIXO 'bb') ---")
# print(f"Palavra '{palavra_1}' pertence a L? -> {pertence_a_linguagem(palavra_1)}")
# print(f"Palavra '{palavra_2}' pertence a L? -> {pertence_a_linguagem(palavra_2)}")


# DESAFIO 5: Árvores e Algoritmos de Busca (BFS - Busca em Largura)
# Explora a árvore por níveis hierárquicos (Pai/Filho) para encontrar um vértice específico.

from collections import deque

arvore = {
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': [],         
    'D': [],         
    'E': []          
}

def busca_bfs(arvore_grafo, raiz, alvo):
    fila = deque([raiz])
    
    print(f"--- INICIANDO BUSCA BFS PELO VÉRTICE '{alvo}' ---")
    
    while fila:
        vertice_atual = fila.popleft()
        print(f"Visitando vértice: {vertice_atual}")
        
        if vertice_atual == alvo:
            return f"Sucesso! O vértice '{alvo}' foi encontrado na árvore."
        
        for filho in arvore_grafo.get(vertice_atual, []):
            fila.append(filho)
            
    return f"O vértice '{alvo}' não pertence a esta árvore."

resultado = busca_bfs(arvore, 'A', 'E')
print(f"\n{resultado}")