from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar('T')
N = TypeVar('N')

class OrderedSet(Generic [T]):
    class __Node(Generic[N]):
        
        info: N | None
        next: OrderedSet.__Node[N]
        prev: OrderedSet.__Node[N]
        
        def __init__(self,value: N| None = None) -> None:
            self.info = value
            self.next = self
            self.prev = self
    
    __sentinel: OrderedSet.__Node[T]
    __count: int
    
    def __init__(self, values: list[T] = []) -> None:
        self.__sentinel = OrderedSet.__Node()
        self.__count = 0
        for elem in values:
            self.add(elem)
           
           
    # Complexity O(N)
    def add(self, value: T) -> None:
        if(value in self):
            return
        self.__count += 1
        new_node = OrderedSet.__Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node   
      
    # Complexity O(N)        
    def __repr__(self) -> str:
        result: list[T] = []
        current = self.__sentinel.next
        while current != self.__sentinel:
            if current.info is not None:
                result.append(current.info)
            current = current.next
        return f'OrderedSet({result})'
    
    # Complexity O(N)
    def __contains__ (self, value: T) -> bool:
        current = self.__sentinel.next
        while current != self.__sentinel:
            if current.info == value:
                return True
            current = current.next
        return False

 # Complexity O(1)
    def __len__(self) -> int:
        return self.__count

    
    
if __name__ == '__main__':
   a: OrderedSet[int] = OrderedSet([4,8,15,16,23,42])
   print(a)
   print(f'{hash(a): x}')
   print(f'{a is None = }') 
   print(f'{a == a =}')
   print(f'{repr(a) =}')
   a.add(4)
   a.add(8)
   a.add(15)
   print(f'{repr(a) = }')
   print(f'{len(a) = }')
   
   #Iterator: allow visiting all the elements of a collection in a sequential fashion
try:#Using iterators
    print()
    x = [3,7,10,20]
    it = iter(x)
    print(f'{x = },{it = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
except StopIteration:
    print('stop')