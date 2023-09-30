#----------------------------------------------------------
# Lab #3: Combinatorics
# Permutations and combinations with repetitions.
#
# Date: 29-Sep-2022
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01746219 Eric Navarro
#----------------------------------------------------------


from comparable import C

def power_set(s: list[C])-> list[list[C]]:
    if s:
        r = power_set(s[:-1])
        return r + [t + [s[-1]] for t in r]
    else:
        return [[]]
    
def sorted_nicely(s: list[list[C]]) -> list[list[C]]:
    def size_and_content(t: list[C]) -> tuple[int,list[C]]:
        return (len(t),t)
    return sorted(s,key=size_and_content)

def combinations(s: list[C], k: int) -> list[list[C]]:
    return [t for t in power_set(s) if len(t) == k]

def insert(x: C, s: list[C],i:int) -> list[C]:
    return s[:i] + [x] + s[i:]
    
def insert_everywhere(x: C, s:list[C]) -> list[list[C]]:
    return [insert(x,s,i) for i in range (len(s) + 1)]

def permute(s:list[C])-> list[list[C]]:
    if s:
        return sum([insert_everywhere(s[0],t) for t in permute(s[1:])],[])
    else:
        return [[]]

def permutations(s:list[C],k:int) -> list[list[C]]:
    return sum([permute (t) for t in combinations (s,k)],[])

def permutations_with_repetition(s: list[C],k: int) -> list[list[C]]:
    if s and k > 0:
        unicos = []
        set_unicos = set()
        res = []
        for elem in s:
            res.extend([elem] * k)
        resPer = permutations(res,k)
        for x in resPer:
            if tuple(x) not in set_unicos:
                unicos.append(x)
                set_unicos.add(tuple(x))
        return unicos
    elif k == 0:
        return []
    else:
        return []
    
def combinations_with_repetition(s: list[C],k: int) -> list[list[C]]:
    unicos = []
    set_unicos = set()
    res = []
    if s and k > 0:
        for elem in s:
            res.extend([elem] * k)
        resPer = combinations(res,k)
        for x in resPer:
            if tuple(x) not in set_unicos:
                unicos.append(x)
                set_unicos.add(tuple(x))
        return unicos
    elif k == 0:
        return []
    else:
        return []
    
if __name__ == '__main__':
    from pprint import pprint
    # pprint(sorted_nicely(power_set([])))
    # pprint(sorted_nicely(power_set(['x'])))
    # pprint(sorted_nicely(power_set(['x','y'])))
    # pprint(sorted_nicely(power_set(['x','y','z'])))
    # pprint(sorted_nicely(power_set(['w','x','y','z'])))
    # pprint(insert('x',['y','z'],3))
    # pprint(insert_everywhere('x',['y','z']))
    #pprint(permute(['x','y','z']))
    ##pprint(sorted_nicely(permute(['w','x','y','z'])))
    #pprint(sorted_nicely(permutations(['w','x','y','z'],3)))
    #pprint(sorted_nicely(permutations_with_repetition([0,1],4)))
    #pprint(sorted_nicely((permutations(['a','a','b','b','c','c'],2))))
    #pprint(sorted_nicely((permutations_with_repetition([0,1],6))))
    #pprint(sorted_nicely((permutations([0,1],3))))
    pprint(sorted_nicely((combinations_with_repetition(['a','b','c'],2))))
        
    
# def permutations_with_repetition(s: list[C],k: int) -> list[list[C]]:
#     if s and k > 0:
#         unicos = []
#         set_unicos = set()
#         res = []
#         for elem in s:
#             res.extend([elem] * k)
#         resPer = permutations(res,k)
#         for x in resPer:
#             if tuple(x) not in set_unicos:
#                 unicos.append(x)
#                 set_unicos.add(tuple(x))
#         return unicos
#     elif k == 0:
#         return []
#     else:
#         return []