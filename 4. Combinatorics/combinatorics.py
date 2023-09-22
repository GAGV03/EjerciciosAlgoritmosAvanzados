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
    pprint(sorted_nicely(permutations(['w','x','y','z'],1)))