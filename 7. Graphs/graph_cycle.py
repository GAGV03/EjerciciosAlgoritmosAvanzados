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
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['C', 'D']
}

def depth_first_search(start: str, graph: Graph) -> Iterator[str]:
    parent: str = ""
    stack: deque[str] = deque()
    visited: set[str] = set() 
    stack.append(start)
    while stack:
        current: str = stack.pop()
        print("Este es current: " + current)
        if current not in visited:
            stack.extend(graph[current][::-1])    
            visited.add(current)
            print("Visitados")
            print(visited)
            print("Padre actual: " + parent)
            print("-----------------------------")
            parent = current
            print(stack)
        elif current in visited:
            print("Este ya fue visitado" + current)
            if current is not parent:
                print("Ya fue visitado y no es parent")
                print(visited)
                yield current
            else:
                visited.add(current)
            
            
            
        
def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    lista = list(depth_first_search(initial,graph))
    return lista
            
if __name__ == '__main__':
    print(has_cycle("D",g))