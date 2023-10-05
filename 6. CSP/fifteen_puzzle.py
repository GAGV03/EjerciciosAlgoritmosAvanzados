from typing import Optional, NamedTuple
from generic_search import astar, Node, node_to_path

Frame = tuple[tuple[int, ...], ...]

class GridLocation(NamedTuple):
    row: int
    column: int
    
goal = ((1,2,3,4),
        (5,6,7,8),
        (9,10,11,12),
        (13,14,15,0))

def solve_puzzle(frame: Frame) -> None:
    result: Optional[Node[Frame]] = astar(
        frame, goal_test, successors, heuristic)
    

def goal_test(frame: Frame) -> bool:
    return frame == goal


def successors(frame: Frame) -> list[Frame]:
    variants: list[Frame] = []
    
    
    return []

def heuristic(frame: Frame) -> float:
    count = 0.0
    for tup, tup2 in zip (goal,frame):
        for elem,elem2 in zip (tup,tup2):
            if elem != elem2:
                count += 1.0
    return count

if __name__ == '__main__':
    prueba = ((2,3,4,5),
              (1,2,3,4),
              (9,10,12,13),
              (15,0,34,5))
    
    prueba2 = ((2, 3, 4, 8),
               (1, 5, 7, 11),
               (9, 6, 12, 0),
               (13, 14, 10, 15))
    
    print(goal_test(prueba))
    print(heuristic(prueba2))