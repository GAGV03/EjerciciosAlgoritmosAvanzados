#----------------------------------------------------------
# Lab #6: Graph Cycle Detection
#
# Date: 03-Nov-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01777771 Erick Navarro
#----------------------------------------------------------


from typing import Iterator, Optional
from collections  import deque

Graph = dict[str,list[str]]

g: Graph = {
                'A': ['B'],
                'B': ['A', 'D'],
                'C': ['D', 'E'],
                'D': ['B', 'C', 'E', 'F'],
                'E': ['C', 'D', 'F'],
                'F': ['D', 'E']
}

def depth_first_search(start: str, graph: Graph) -> Optional[list[str]]:
    parent: str = ""
    prev_parent: str = ""
    stack: deque[str] = deque()
    visited: set[str] = set() 
    visitados: list[str] = list()
    stack.append(start)
    while stack:
        current: str = stack.pop()
        print("Nodo actual: " + current)
        print("Padre actual: " + parent)
        print("Padre anterior: " + prev_parent)
        if current not in visited:
            stack.extend(graph[current][::-1])    
            print("La stack actual es: ")
            print(stack)
            visited.add(current)
            visitados.append(current)
            prev_parent = parent
            parent = current
        elif current in visited:
            if current is not prev_parent:
                visitados.append(current)
                pos_current = visitados.index(current)
                resultado = visitados[pos_current:]
                return resultado
            else:
                print("EL NODO ACTUAL ES EL ANTIGUO PADRE")
                print(stack)
                continue
    return None
            
            
            
        
def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    if depth_first_search(initial,graph) is None:
        return None
    else:
        lista = depth_first_search(initial,graph)
        return lista
            
if __name__ == '__main__':
    print(has_cycle("F",g))