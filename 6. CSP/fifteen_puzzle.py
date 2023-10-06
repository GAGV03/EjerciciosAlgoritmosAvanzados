from typing import Optional, NamedTuple
from generic_search import astar, Node, node_to_path

Frame = tuple[tuple[int, ...], ...]
    
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
    holder = 0
    one,two,three,four = False,False,False,False
    lista = list(frame)
    for _ in range (0,4):
        for a in range (0,4):
            for b in range (0,4):
                if frame[a][b] == 0:
                    if one == False:
                        if a > 0:
                                holder = frame[a-1][b]
                                antTup = list(lista[a-1])
                                actTup = list(lista[a])
                                for i in range (0,4):
                                    if antTup[i] == holder:
                                        antTup[i] = 0
                                    if actTup[i] == 0:
                                        actTup[i] = holder
                                del lista [a-1]
                                del lista [a-1]
                                lista.insert(a-1,tuple(antTup))
                                lista.insert(a,tuple(actTup))
                                res = tuple(lista)
                                variants.append(res)   
                                lista = list(frame) 
                                one = True
                    elif two == False:
                        if a <= 2:
                            holder = frame[a+1][b]
                            #print(holder)
                            actTup = list(lista[a])
                            aftTup = list(lista[a+1])
                            for i in range(0,4):
                                if aftTup[i] == holder:
                                    aftTup[i] = 0
                                if actTup[i] == 0:
                                    actTup[i] = holder 
                            del lista [a+1]
                            del lista [a]
                            lista.insert(a,tuple(actTup))
                            lista.insert(a+1,tuple(aftTup))
                            res = tuple(lista)
                            variants.append(res)
                            lista = list(frame) 
                            two = True
                    elif three == False:
                        if b > 0:
                            holder = frame[a][b-1]
                            #print(holder)
                            actTup = list(lista[a])
                            for i in range(0,4):
                                if actTup[i] == 0:
                                    actTup[i] = holder 
                                    actTup[i-1] = 0
                            del lista [b-1]
                            lista.insert(b-1,tuple(actTup))
                            res = tuple(lista)
                            variants.append(res)
                            lista = list(frame) 
                            three = True
                    elif four == False:
                        if b < 2:
                            holder = frame[a][b+1]
                            actTup = list(lista[a])
                            for i in range(0,4):
                                if actTup[i] == 0:
                                    actTup[i] = holder
                                    actTup[i+a] = 0
                            del lista [b+1]
                            lista.insert(b+1,tuple(actTup))
                            res = tuple(lista)
                            variants.append(res)
                            lista = list(frame) 
                            four = True
    return variants
    
def heuristic(frame: Frame) -> float:
    count = 0.0
    for tup, tup2 in zip (goal,frame):
        for elem,elem2 in zip (tup,tup2):
            if elem != elem2:
                count += 1.0
    return count

if __name__ == '__main__':
    
    from pprint import pprint
    
    prueba = ((2,3,4,5),
              (1,2,3,4),
              (9,10,12,13),
              (15,0,34,5))
    
    prueba2 = ((2, 3, 4, 8),
               (1, 5, 7, 11),
               (9, 6, 12, 0),
               (13, 14, 10, 15))
    
    # print(goal_test(prueba))
    # print(heuristic(prueba2))
    # print(prueba[0][0])
    pprint(successors( ((2,3,4,5),
                        (1,2,3,4),
                        (9,10,12,13),
                        (15,0,34,5))))