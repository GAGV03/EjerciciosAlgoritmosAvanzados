from csp import Constraint, CSP
from typing import NamedTuple, Optional

Grid = list[list[int]]

class GridLocation(NamedTuple):
    row: int
    column: int

def cheack_square(square:Grid) -> bool:
    ([a,b,c],
     [d,e,f],
     [g,h,i]) = square
    return ((a+b+c) #Rows
            ==(d+e+f)
            ==(g,h,i)
            ==(a+d+g) #Columns
            ==(b,e,h)
            ==(c+f+i)
            ==(a+e+i) #Diagonals
            ==(g+e+c))
    
    
class MagicPuzzleConstraint(Constraint[int,GridLocation]):
    def __init__(self, variables: list[int]) -> None:
        super().__init__(variables)
        self.variables: list[int] = variables
        
    def satisfied(self, assignment: dict[int, GridLocation]) -> bool:
        if len(assignment) != len(set(assignment.values())):
            return False
        if len(assignment) < 9:
            return True
        
        square: Grid = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]
        for var, (row,col) in assignment.items():
            square[row][col] = var
        return cheack_square(square)
        

if __name__ == '__main__':
    from pprint import pprint
    variables: list[int] = list(range(1,10))
    all_grid_locations: list[GridLocation] = [GridLocation(r,c)
                                             for r in range (3)
                                             for c in range (3)]
    
    domains: dict [int, list [GridLocation]] = {
        var: all_grid_locations for var in variables
    }
    
    csp: CSP[int,GridLocation] = CSP(variables,domains)
    csp.add_constraint(MagicPuzzleConstraint(variables))
    solution : Optional[dict[int,GridLocation]] = csp.backtracking_search()
    if solution:
        pprint(solution)
    else:
        print('Found no solution :(')