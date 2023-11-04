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

def depth_first_search_cycle(start: str, graph: Graph) -> Optional[list[str]]:
    parent: str = ""
    prev_parent: str = ""
    stack: deque[str] = deque()
    stack_reversa: deque[str] = deque()
    len_prev_stack: int = 0
    len_prev_stackRev: int = 0
    switch_bucle: bool = True
    visited: set[str] = set() 
    visitados: list[str] = list()
    stack.append(start)
    
    while stack:
        len_prev_stack = len(stack)
        current: str = stack.pop()
        visitados.append(current)
        if current not in visited:
            stack.extend(graph[current][::-1]) 
            visited.add(current)
            prev_parent = parent
            parent = current
        
        else:            
            if (len(stack_reversa) - len_prev_stackRev) >= 2: 
                switch_bucle = True
                prev_parent = parent
                parent = current
                continue
            
            elif len_prev_stack == len(stack)+1:
                len_prev_stackRev = len(stack_reversa)
                stack_reversa.extend(graph[current][::-1])
                switch_bucle = False 
                prev_parent = parent
                parent = current
                continue

            if switch_bucle:
                if current is not prev_parent:
                    visitados.append(current)
                    pos_current = visitados.index(current)
                    resultado = visitados[pos_current:]
                    return resultado
                else:
                    switch_bucle = False
                    prev_parent = parent
                    parent = current
                    print(stack)
                    continue
    return None
            
        
def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    if depth_first_search_cycle(initial,graph) is None:
        return None
    else:
        lista = depth_first_search_cycle(initial,graph)
        return lista
            
if __name__ == '__main__':
    print(has_cycle("F",g))




