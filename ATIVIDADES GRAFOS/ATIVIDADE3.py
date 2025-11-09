def criar_grafo():
    return {"vertices": [], "arestas": []}


def inserir_vertice(grafo, vertice):
    if vertice not in grafo["vertices"]:
        grafo["vertices"].append(vertice)
    else:
        print(f"Vértice '{vertice}' já existe.")


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo["vertices"]:
        inserir_vertice(grafo, origem)
    if destino not in grafo["vertices"]:
        inserir_vertice(grafo, destino)

    for e in grafo["arestas"]:
        if e["nao_direcionado"] == nao_direcionado:
            if not nao_direcionado and e["origem"] == origem and e["destino"] == destino:
                return
            if nao_direcionado and (
                (e["origem"] == origem and e["destino"] == destino) or
                (e["origem"] == destino and e["destino"] == origem)
            ):
                return

    grafo["arestas"].append({
        "origem": origem,
        "destino": destino,
        "nao_direcionado": nao_direcionado
    })


def remover_vertice(grafo, vertice):
    if vertice not in grafo["vertices"]:
        print(f"Vértice '{vertice}' não existe.")
        return

    grafo["vertices"].remove(vertice)

    grafo["arestas"] = [
        e for e in grafo["arestas"]
        if e["origem"] != vertice and e["destino"] != vertice
    ]


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    removida = False
    nova_lista = []

    for e in grafo["arestas"]:
        if not removida:
            if not nao_direcionado and not e["nao_direcionado"]:
                if e["origem"] == origem and e["destino"] == destino:
                    removida = True
                    continue

            if nao_direcionado and e["nao_direcionado"]:
                if ((e["origem"] == origem and e["destino"] == destino) or
                    (e["origem"] == destino and e["destino"] == origem)):
                    removida = True
                    continue

        nova_lista.append(e)

    if not removida:
        print("Aresta não encontrada.")
    grafo["arestas"] = nova_lista


def existe_aresta(grafo, origem, destino):
    for e in grafo["arestas"]:
        if not e["nao_direcionado"]:
            if e["origem"] == origem and e["destino"] == destino:
                return True
        else:
            if ((e["origem"] == origem and e["destino"] == destino) or
                (e["origem"] == destino and e["destino"] == origem)):
                return True
    return False


def vizinhos(grafo, vertice):
    if vertice not in grafo["vertices"]:
        print(f"O vértice '{vertice}' não existe.")
        return []

    viz = []
    for e in grafo["arestas"]:
        if not e["nao_direcionado"]:
            if e["origem"] == vertice:
                viz.append(e["destino"])
        else:
            if e["origem"] == vertice:
                viz.append(e["destino"])
            elif e["destino"] == vertice:
                viz.append(e["origem"])
    return viz


def listar_vizinhos(grafo, vertice):
    lista = vizinhos(grafo, vertice)
    if lista:
        print(f"Vizinhos de {vertice}: {lista}")
    elif vertice in grafo["vertices"]:
        print(f"O vértice '{vertice}' não possui vizinhos.")
    else:
        print(f"O vértice '{vertice}' não existe no grafo.")


def grau_vertices(grafo):
    for v in grafo["vertices"]:
        entrada = 0
        saida = 0
        for e in grafo["arestas"]:
            if e["nao_direcionado"]:
                if e["origem"] == v or e["destino"] == v:
                    entrada += 1
                    saida += 1
            else:
                if e["origem"] == v:
                    saida += 1
                if e["destino"] == v:
                    entrada += 1
        total = entrada + saida
        print(f"{v}: entrada={entrada}, saída={saida}, total={total}")


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return False
    for i in range(len(caminho) - 1):
        if not existe_aresta(grafo, caminho[i], caminho[i+1]):
            return False
    return True


def exibir_grafo(grafo):
    print("\nVértices:", grafo["vertices"])
    print("Arestas:")
    for e in grafo["arestas"]:
        if e["nao_direcionado"]:
            print(f"{e['origem']} -- {e['destino']}")
        else:
            print(f"{e['origem']} -> {e['destino']}")


def main():
    g = criar_grafo()

    inserir_vertice(g, "A")
    inserir_vertice(g, "B")
    inserir_vertice(g, "C")

    inserir_aresta(g, "A", "B", nao_direcionado=True)
    inserir_aresta(g, "A", "C", nao_direcionado=False)

    exibir_grafo(g)

    print("\nVizinhos de A:", vizinhos(g, "A"))
    listar_vizinhos(g, "B")
    listar_vizinhos(g, "D")

    print("\nExiste aresta A -> C?", existe_aresta(g, "A", "C"))
    print("Existe aresta C -> A?", existe_aresta(g, "C", "A"))

    print("\nGrau dos vértices:")
    grau_vertices(g)

    caminho = ["A", "B", "C"]
    print(f"\nPercurso {caminho} é válido?", percurso_valido(g, caminho))

    print("\nRemovendo vértice B e aresta A--B...")
    remover_vertice(g, "B")
    exibir_grafo(g)


if __name__ == "__main__":
    main()