import math

#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 18-Nov-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01746219 Eric Navarro
#----------------------------------------------------------

WeightedGraph = dict[str, set[tuple[str, float]]]
    
def dijkstra_spt(initial: str,graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    
    tempset: set[tuple[str,float]] = set()
    visited: set[str] = set()
    unvisited: set[str] = set()
    shortest_path: dict[str,str] = {}
    cost_dict: dict[str,float]= {}
    resulting_spt: WeightedGraph = {}
    costos: list[float] = []
                
    for vertex in graph:
        unvisited.add(vertex)
        if vertex is initial:
            cost_dict[vertex] = 0
        else:
            cost_dict[vertex] = math.inf
        
    while unvisited:
        for v in unvisited:
            costos.append(cost_dict[v])
        costo_minimo = min(costos)
        value = {i for i in cost_dict if cost_dict[i] == costo_minimo}
        min_vert = "".join(value) 
        if len(min_vert)>1:
            min_vert_sort = sorted(min_vert)
            for i in min_vert_sort:
                if i in unvisited:
                    min_vert = i
        neighbors = graph[min_vert] 
        for neighbor in neighbors:
            if neighbor[0] not in visited:
                cost = cost_dict[min_vert] + neighbor[1]
                if cost < cost_dict[neighbor[0]]:
                    cost_dict[neighbor[0]] = cost
                    shortest_path[neighbor[0]] = min_vert
        unvisited.remove(min_vert)
        visited.add(min_vert)
        costos.clear()
        
    for visit in sorted(visited):
        for vertshort in shortest_path: 
            if visit == vertshort:
                for vecino, costo in graph[vertshort]:
                    if vecino == shortest_path[vertshort]:
                        if visit not in resulting_spt:
                            tempset.add((vecino,costo))
                            resulting_spt[visit] = tempset
                            tempset = set()
                        else:
                            tempset.add((vecino,costo))
                            resulting_spt[visit].update(tempset)
                            tempset = set()
                        
            elif visit == shortest_path[vertshort]:
                for vecino, costo in graph[shortest_path[vertshort]]:
                    if vecino == vertshort:
                        if visit not in resulting_spt:    
                            tempset.add((vecino,costo))
                            resulting_spt[visit] = tempset
                            tempset=set()
                        else:
                            tempset.add((vecino,costo))
                            resulting_spt[visit].update(tempset)
                            tempset = set()
                            
    return (cost_dict,resulting_spt)


if __name__ == '__main__':
    print(dijkstra_spt('D', {'A': {('B', 4), ('E', 8)},
    'B': {('A', 4), ('E', 11), ('C', 8)},
    'C': {('B', 8), ('I', 2), ('G', 4), ('D', 7)},
    'D': {('C', 7), ('G', 14), ('H', 9)},
    'E': {('A', 8), ('B', 11), ('I', 7), ('F', 1)},
    'F': {('E', 1), ('I', 6), ('G', 2)},
    'G': {('F', 2), ('C', 4), ('D', 14), ('H', 10)},
    'H': {('D', 9), ('G', 10)},
    'I': {('C', 2), ('E', 7), ('F', 6)},
                  }))