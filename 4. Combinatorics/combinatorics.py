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
    
    
if __name__ == '__main__':
    from pprint import pprint
    pprint(sorted_nicely(power_set([])))
    pprint(sorted_nicely(power_set(['x'])))
    pprint(sorted_nicely(power_set(['x','y'])))
    pprint(sorted_nicely(power_set(['x','y','z'])))
    pprint(sorted_nicely(power_set(['w','x','y','z'])))
    