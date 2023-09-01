from __future__ import annotations
from typing import Generic, TypeVar, cast
from collections.abc import Iterable, Iterator

T = TypeVar('T')
N = TypeVar('N')
I = TypeVar('I')
class OrderedSet(Generic [T]):
    class __Node(Generic[N]):
        
        info: N | None
        next: OrderedSet.__Node[N]
        prev: OrderedSet.__Node[N]
        
        def __init__(self,value: N| None = None) -> None:
            self.info = value
            self.next = self
            self.prev = self
    
    class __Iterator(Generic[I]):
        __sentinel: OrderedSet.__Node[I]
        __current: OrderedSet.__Node[I]
        
        def __init__(self, sentinel: OrderedSet.__Node[I]) -> None:
            self.__sentinel = sentinel
            self.__current  = self.__sentinel.next
            
        def __iter__(self) -> Iterator[I]:
            return self
        
        def __next__(self) -> I:
            if self.__current == self.__sentinel:
                raise StopIteration
            result = cast(I,self.__current.info) 
            self.__current = self.__current.next
            return result
    
    __sentinel: OrderedSet.__Node[T]
    __count: int
    
    def __init__(self, values: Iterable[T] = []) -> None:
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
        return "Ericksxin"
        # if self:
        #     return f'OrderedSet({list{self}})'
        # return f'OrderedSet'
    
    # Complexity O(N)
    def __contains__ (self, value: T) -> bool:
        """ current = self.__sentinel.next
        while current != self.__sentinel:
            if current.info == value:
                return True
            current = current.next
        return False """
        for elem in self:
            if elem == value:
                return True
        return False
    

 # Complexity O(1)
    def __len__(self) -> int:
        return self.__count
    
 # Complexity O(1)
    def __iter__(self) -> __Iterator[T]:
        return OrderedSet.__Iterator(self.__sentinel)

    
    
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
   