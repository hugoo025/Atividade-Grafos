def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print(f"Vértice: {vertice}, existe!")
        return
    else:
        vertices.append(vertice)
        for linha in matriz:
            linha.append(0)
        novo_tamanho = len(vertices)
        matriz.append([0] * novo_tamanho)


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1

    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe")
        return

    idx = vertices.index(vertice)

    matriz.pop(idx)

    for linha in matriz:
        linha.pop(idx)

    vertices.pop(idx)

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        print("Um dos vértices não existe")
        return

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 0

    if nao_direcionado:
        matriz[j][i] = 0


def existe_aresta(matriz, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        return False
    i = vertices.index(origem)
    j = vertices.index(destino)
    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"O vértice '{vertice}' não existe")
        return []

    i = vertices.index(vertice)
    lista = []
    for j, val in enumerate(matriz[i]):
        if val == 1:
            lista.append(vertices[j])
    return lista


def grau_vertices(matriz, vertices):
    graus = {}
    n = len(vertices)
    for i, v in enumerate(vertices):
        grau_saida = sum(matriz[i]) if n > 0 else 0
        grau_entrada = sum(matriz[row][i] for row in range(n)) if n > 0 else 0
        graus[v] = {"entrada": grau_entrada, "saida": grau_saida, "total": grau_entrada + grau_saida}
    return graus


def percurso_valido(matriz, vertices, caminho):
    if len(caminho) <= 1:
        return True

    for k in range(len(caminho) - 1):
        u = caminho[k]
        v = caminho[k + 1]
        if not existe_aresta(matriz, vertices, u, v):
            return False
    return True

def listar_vizinhos(matriz, vertices, vertice):
    lista = vizinhos(matriz, vertices, vertice)
    if lista:
        print(f"Vizinhos de {vertice}: {lista}")
    else:
        print(f"O vértice '{vertice}' não existe ou não possui vizinhos")


def exibir_grafo(matriz, vertices):
    if not vertices:
        print("Grafo vazio")
        return

    cabecalho = " " + " ".join(f"{v:>3}" for v in vertices)
    print(cabecalho)
    print(" " + "------" * len(vertices))

    for i, v in enumerate(vertices):
        linha = " ".join(f"{val:>3}" for val in matriz[i])
        print(f"{v:>3} |{linha}")


def main():
    matriz, vertices = criar_grafo()

    inserir_vertice(matriz, vertices, "A")
    inserir_vertice(matriz, vertices, "B")
    inserir_vertice(matriz, vertices, "C")

    inserir_aresta(matriz, vertices, "A", "B", nao_direcionado=True)
    inserir_aresta(matriz, vertices, "A", "C", nao_direcionado=False)

    print("\nGrafo inicial:")
    exibir_grafo(matriz, vertices)

    print("\nVizinhos de A: ", vizinhos(matriz, vertices, "A"))
    listar_vizinhos(matriz, vertices, "B")
    listar_vizinhos(matriz, vertices, "C")

    print("\nExiste aresta C -> A?", existe_aresta(matriz, vertices, "C", "A"))
    print("Existe aresta A -> C?", existe_aresta(matriz, vertices, "A", "C"))

    print("\nGrau dos vértices: ")
    graus = grau_vertices(matriz, vertices)
    for v, g in graus.items():
        print(f"{v}: entrada = {g['entrada']}, saida = {g['saida']}, total = {g['total']}")

    caminho = ["A", "B", "C"]
    print(f"\nPercurso {caminho} é válido?", percurso_valido(matriz, vertices, caminho))

    print("\nAresta A <-> B e Vértice B removidas com sucesso!")
    remover_aresta(matriz, vertices, "A", "B", nao_direcionado=True)
    remover_vertice(matriz, vertices, "B")

    print("\nGrafo final (após remoções): ")
    exibir_grafo(matriz, vertices)
    
if "__main__" == __name__:
    main()