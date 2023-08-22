from typing import Generic, TypeVar

T = TypeVar('T')

class OrderedSet(Generic [T]):
    ...
    
    
    
if __name__ == '__main__':
   a: OrderedSet[int] = OrderedSet()
   print(a)
   print(f'{hash(a): x}')
   print(f'{a is None = }') 
   print(f'{a == a =}')
   print(f'{repr(a) =}')