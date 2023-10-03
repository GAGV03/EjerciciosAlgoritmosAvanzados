from typing import Any, Iterator, Optional
from collections import deque

#BINARY TREE TRAVERSALS
#DEPTH-FIRST SEARCH (DFS)
#BREATH-FIRST SEARCH (BFS)

Tree = Optional[list[Any]]

t: Tree = \
    ['A',
     ['B',
      ['D',None,None],
      None],
     ['C',
      None,
      ['E',
       ['F',None,None],
       ['G',None,None]]]]
    
def in_order(root:Tree) -> Iterator[str]:
    if root:
        value, left, right = root
        # for x in in_order(left):
        #     yield x
        yield from in_order(left) #Recorre todos los nodos de la izquierda
        yield value
        yield from in_order(right) #Recorre todos los nodos de la derecha
        
def pre_order(root:Tree) -> Iterator[str]: #DFS
    if root:
        value, left, right = root
        # for x in in_order(left):
        #     yield x
        yield value
        yield from pre_order(left) #Recorre todos los nodos de la izquierda
        yield from pre_order(right) #Recorre todos los nodos de la derecha
        
def post_order(root:Tree) -> Iterator[str]:
    if root:
        value, left, right = root
        # for x in in_order(left):
        #     yield x
        yield from post_order(left) #Recorre todos los nodos de la izquierda
        yield from post_order(right) #Recorre todos los nodos de la derecha
        yield value
        
def level_order (root: Tree) -> Iterator[str]: #BFS
    queue: deque[Tree] = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current:
            value, left, right = current
            queue.append(left)
            queue.append(right)
            yield value

if __name__ == '__main__':
    print(f'{list(in_order(t)) = }')
    print(f'{list(pre_order(t)) = }')
    print(f'{list(post_order(t)) = }')
    print(f'{list(level_order(t)) = }')