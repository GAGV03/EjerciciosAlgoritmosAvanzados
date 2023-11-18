import math
from typing import NamedTuple, Optional
from heapq import heapify,heappop

#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 18-Nov-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01777771 Erickx Navarro
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
        if(len(min_vert)>1):
            min_vert = min_vert[0]
            print("fue cortado: "+min_vert)
        neighbors = graph[min_vert] #El pedo está aquí en 4 tests, usar el más chiquito en nombre
        for neighbor in neighbors:
            if neighbor[0] not in visited:
                cost = cost_dict[min_vert] + neighbor[1]
                if cost < cost_dict[neighbor[0]]:
                    cost_dict[neighbor[0]] = cost
                    shortest_path[neighbor[0]] = min_vert
        unvisited.remove(min_vert) #Segundo pedo
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
    print(dijkstra_spt('A', {'A': {('B', 5), ('C', 10), ('E', 6)},
                   'B': {('A', 5), ('D', 2)},
                   'C': {('A', 10), ('D', 1), ('E', 3)},
                   'D': {('B', 2), ('C', 1), ('E', 4)},
                   'E': {('A', 6), ('C', 3), ('D', 4)},
                  }))