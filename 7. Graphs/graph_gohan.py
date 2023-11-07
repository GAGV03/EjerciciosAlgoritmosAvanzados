from typing import Optional, List, Dict


Graph = dict[str, list[str]]


def has_cycle(initial: str, graph: Graph) -> Optional[List[str]]:
    visited: set[str] = set()
    father: Dict[str, Optional[str]] = dict()
    cycle = dfs_cycle(graph, initial, visited, father)
    if cycle is not None:
        return cycle
    return None

def dfs_cycle(graph, initial, visited, father):
    visited.add(initial)
    for vertice in graph[initial]:
        if vertice in visited:
            if vertice != father[initial]:
                return rebuild_cycle(father, vertice, initial)
        else:
            father[vertice] = initial
            ciclo = dfs_cycle(graph, vertice, visited, father)
            if ciclo is not None:
                return ciclo
    return None

def rebuild_cycle(father, start, end):
    vertex = end
    cycle = []
    while vertex != start:
        cycle.append(vertex)
        vertex = father[vertex]
    cycle.append(start)
    cycle.reverse()
    cycle.append(start)
    return cycle