from typing import Optional, NamedTuple
from generic_search import astar, Node, node_to_path
import time

Frame = tuple[tuple[int, ...], ...]
    
def solve_puzzle(frame: Frame) -> None:
    result: Optional[Node[Frame]] = astar(
        frame, goal_test, successors, heuristic)
    if result is None:
        print('No se puede generar una respuesta')
    else:
        path: list[Frame] = node_to_path(result)
        xo: int = 0
        yo: int = 0

        xf: int = 0
        yf: int = 0
        value = 0
        if(len(path) == 2):
            print("Solution requires ", len(path) -1," step",sep="")
        else:
            print("Solution requires ", len(path) -1," steps",sep="")
        for f in range(len(path) - 1):
            for i in range(4):
                for j in range(4):
                    if path[f][i][j] == 0:
                        xo = j
                        yo = i
                        value = path[f+1][i][j]
                        
                    if path[f+1][i][j] == 0:
                        xf = j
                        yf = i
                   
            if yo < yf:
                print("Step ",f+1,": Move ", value,  " up",sep="")
            if yo > yf:
                print("Step ",f+1,": Move ", value,  " down",sep="")
            if xo < xf:
                print("Step ",f+1,": Move ", value,  " left",sep="")
            if xo > xf:
                print("Step ",f+1,": Move ", value,  " right",sep="")

def goal_test(frame: Frame) -> bool:
    goal : Frame = ((1,2,3,4),
        (5,6,7,8),
        (9,10,11,12),
        (13,14,15,0))
    return goal == frame

def successors(frame: Frame) -> list[Frame]:
    inicio = time.time()
    variants: list[Frame] = [] 
    holder = 0
    one,two,three,four = False,False,False,False
    lista = list(frame)
    for _ in range (0,4):
        for a in range (0,4):
            for b in range (0,4):
                if frame[a][b] == 0:
                    if one == False:
                        if a <= 2:
                                holder = frame[a+1][b]
                                actTup = list(lista[a])
                                aftTup = list(lista[a+1])
                                for i in range(0,4):
                                    if aftTup[i] == holder:
                                        aftTup[i] = 0
                                    if actTup[i] == 0:
                                        actTup[i] = holder 
                                del lista [a]
                                del lista [a]
                                lista.insert(a,tuple(actTup))
                                lista.insert(a+1,tuple(aftTup))
                                res = tuple(lista)
                                variants.append(res)
                                lista = list(frame) 
                                one = True
                        else:
                                one = True
                    elif two == False:
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
                                two = True         
                        else:
                                two = True
                    elif three == False:
                        if b <= 2:
                                holder = frame[a][b+1]
                                actTup = list(lista[a])
                                for i in range(0,4):
                                    if actTup[i] == 0:
                                        actTup[i] = holder
                                        actTup[i+1] = 0
                                        break
                                del lista [a]
                                lista.insert(a,tuple(actTup))
                                res = tuple(lista)
                                variants.append(res)
                                lista = list(frame) 
                                three = True
                        else:
                            three = True
                    elif four == False:
                        if b > 0:
                                holder = frame[a][b-1]
                                actTup = list(lista[a])
                                for i in range(0,4):
                                    if actTup[i] == 0:
                                        actTup[i] = holder 
                                        actTup[i-1] = 0
                                del lista [a]
                                lista.insert(a,tuple(actTup))
                                res = tuple(lista)
                                variants.append(res)
                                lista = list(frame) 
                                four = True
                        else:
                            four = True 
    fin = time.time()
    return list(variants)
    
def heuristic(frame: Frame) -> float:
    goal : Frame = ((1,2,3,4),
        (5,6,7,8),
        (9,10,11,12),
        (13,14,15,0))
    count = 0.0
    for a in range (0,4):
        for b in range (0,4):
            if frame[a][b] != goal[a][b]:
                count += 1.0
    return count
if __name__ == '__main__':
    
    from pprint import pprint
                           
""" solve_puzzle(((2, 3, 4, 8),
            (1, 5, 7, 11),
            (9, 6, 12, 0),
            (13, 14, 10, 15)))  """
            
""" print('Mi successors: ')

pprint(successors(((2, 3, 11, 8),
                   (7, 5, 4, 0),
                   (9, 6, 1, 12),
                   (13, 14, 10, 15)))) 

print('Successors de Carlos: ')

pprint(successors2(((2, 3, 11, 8),
                    (7, 5, 4, 0),
                    (9, 6, 1, 12),
                    (13, 14, 10, 15)))) 

print(successors(((2, 3, 4, 8),
                   (7, 5, 0, 11),
                   (9, 6, 1, 12),
                   (13, 14, 10, 15))) == successors2(((2, 3, 4, 8),
                    (7, 5, 0, 11),
                    (9, 6, 1, 12),
                    (13, 14, 10, 15)))) """


