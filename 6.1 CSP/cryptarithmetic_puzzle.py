#----------------------------------------------------------
# Lab #5: Cryptarithmetic with CSP
# General cryptarithmetic puzzle solver.
#
# Date: 13-Oct-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01746219 Eric Navarro
#----------------------------------------------------------


from csp import Constraint, CSP
from typing import Optional, Dict,List

class cryptoarithmetic_puzzle_Constraint(Constraint[str,int]):
    
    def __init__(self, letras:List[str], palabras: List[str], respuesta: str, maxLen : int) -> None:
        super().__init__(letras)
        self.letras: List[str] = letras
        self.palabras: List[str] = palabras
        self.respuesta: str = respuesta
        self.maxLen: int = maxLen
                
    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if len(set(assignment.values())) < len(assignment):
            return False
        
        if len(assignment) == len(self.letras):
            sumSumandos: int = 0
            for i in range (self.maxLen):
                for palabra in self.palabras:
                    if i < len(palabra):
                        indice : int = (len(palabra) -1 -i)
                        sumSumandos += (assignment[palabra[indice]]) * pow (10,i)    
            sumResultado : int = 0
            for i in range(len(self.respuesta)):
                indice2: int = (len(self.respuesta) -1 -i)
                sumResultado += (assignment[self.respuesta[indice2]]) * pow (10,i)
            return sumSumandos == sumResultado
        return True

def solve_cryptarithmetic_puzzle(addends: list[str],answer: str) -> Optional[dict[str, int]]:
    maxLen : int = 0
    for pal in addends:
        if len(pal) > maxLen:
            maxLen = len(pal)
    letras : List[str] = []
    temporal = addends.copy()
    temporal.append(answer)
    juntos = ''.join(elem for elem in temporal)
    for letra in juntos:
        if letra not in letras:
            letras.append(letra)
    letras.sort()
    valores_posibles : Dict[str,List[int]] = {}
    for letra in letras:
        valores_posibles[letra] = [0,1,2,3,4,5,6,7,8,9]
    csp : CSP[str,int] = CSP(letras,valores_posibles)
    csp.add_constraint(cryptoarithmetic_puzzle_Constraint(letras,addends,answer,maxLen))
    solucion : Optional[dict[str,int]] = csp.backtracking_search()
    if solucion is None:
        return None
    else:
        solFinal = {key.upper(): val for key, val in solucion.items()}
        return solFinal


if __name__ == '__main__':
    print(solve_cryptarithmetic_puzzle(['i','luv','u'],'yes'))
    