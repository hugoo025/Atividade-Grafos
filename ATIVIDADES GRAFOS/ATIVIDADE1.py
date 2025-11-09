def criar_grafo():
    return{}


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
    else:
        print(f"Vértice '{vertice}' já existe")


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
    
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    
    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)


def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        print(f"O vértice '{vertice}' não existe no grafo")
        return []
    
    
def listar_vizinhos(grafo, vertice):
    lista = vizinhos(grafo, vertice)

    if vertice in grafo and lista:
        print(f"Vizinhos de {vertice}: {lista}")
    elif vertice in grafo and not lista:
        print(f"O vértice '{vertice}' não possui vizinhos")


def exibir_grafo(grafo):
    print("\nLista de Adjacência")
    for v in grafo:
        print(f"{v} -> {grafo[v]}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)

    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        print(f"Vértice '{vertice}' não existe.")
        return

    for v in list(grafo.keys()):
        if vertice in grafo[v]:
            grafo[v].remove(vertice)

    del grafo[vertice]


def existe_aresta(grafo, origem, destino):
    return origem in grafo and destino in grafo[origem]


def grau_vertices(grafo):
 for v in grafo:
        grau_saida = len(grafo[v])
        grau_entrada = sum(1 for u in grafo if v in grafo[u])
        print(f"{v}: entrada={grau_entrada}, saída={grau_saida}, total={grau_entrada + grau_saida}")


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True


def main():
    grafo = criar_grafo()

    inserir_vertice(grafo, "A")
    inserir_vertice(grafo, "B")
    inserir_vertice(grafo, "C")

    inserir_aresta(grafo, "A", "B", nao_direcionado=True)
    inserir_aresta(grafo, "A", "C")

    exibir_grafo(grafo)

    print("\nVizinhos de A:", vizinhos(grafo, "A"))
    listar_vizinhos(grafo, "C")
    listar_vizinhos(grafo, "D")

    print("\nExiste aresta A -> C?", existe_aresta(grafo, "A", "C"))
    print("Existe aresta C -> A?", existe_aresta(grafo, "C", "A"))

    print("\nGrau dos vértices:")
    grau_vertices(grafo)

    caminho = ["A", "B", "C"]
    print(f"\nPercurso {caminho} é válido?", percurso_valido(grafo, caminho))

    remover_vertice(grafo, "B")
    print("\nVértice B removida com sucesso!")
    exibir_grafo(grafo)

if __name__ == "__main__":
    main()