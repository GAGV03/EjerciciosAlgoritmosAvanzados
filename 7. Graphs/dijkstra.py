import math
from typing import NamedTuple, Optional
from heapq import heapify,heappop

#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 17-Nov-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01777771 Erickx Navarro
#----------------------------------------------------------

WeightedGraph = dict[str, set[tuple[str, float]]]

class Edge(NamedTuple):
    
    weight: float
    u: str
    v: str
    
    def __eq__(self, other:object) -> bool: 
        if isinstance(other,Edge):
            return (self.weight == other.weight and ((self.u == other.u and self.v == other.v) or (self.u == other.v and self.v == other.u)))
        else:
            return False
        
    def __hash__(self) -> int:
        return hash(self.weight) + hash(self.u) + hash(self.v)
    
    
def make_heap(graph: WeightedGraph) -> list[Edge]:
    result : set [Edge] = set()
    u : str
    neighbors: set[tuple[str,float]]
    for u, neighbors in graph.items():
        v: str
        weight: float
        for v, weight in neighbors:
            result.add(Edge(weight,u,v))
    queue: list [Edge] = list(result)
    heapify(queue)
    return queue
    

def dijkstra_spt(initial: str,graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    
    visited: set[str] = set()
    unvisited: set[str] = set()
    prev_vertex: dict[str,str] = {}
    cost_dict: dict[str,float]= {}
    resulting_spt: WeightedGraph = {}
    costos: list[float] = []
    vecinitos: list[float] = []
            
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
        neighbors = graph[min_vert] 
        for neighbor in neighbors:
            if neighbor[0] not in visited:
                cost = cost_dict[min_vert] + neighbor[1]
                if cost < cost_dict[neighbor[0]]:
                    cost_dict[neighbor[0]] = cost
                    prev_vertex[neighbor[0]] = min_vert
        unvisited.remove(min_vert)
        visited.add(min_vert)
        costos.clear()
        
    print(cost_dict)
    for i in sorted(prev_vertex):
        print('{' + prev_vertex[i] + ', ' + i + '}')
    
    return ({},{})

    
    
if __name__ == '__main__':
    dijkstra_spt('A', {'A': {('B', 5), ('C', 10), ('E', 6)},
                   'B': {('A', 5), ('D', 2)},
                   'C': {('A', 10), ('D', 1), ('E', 3)},
                   'D': {('B', 2), ('C', 1), ('E', 4)},
                   'E': {('A', 6), ('C', 3), ('D', 4)},
                  })