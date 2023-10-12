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
from typing import Optional

class cryptoarithmetic_puzzle_Constraint(Constraint[str,int]):
    
    def __init__(self, letras:list[str], palabras: list[str], respuesta: str) -> None:
        super().__init__(letras)
        self.letras: list[str] = letras
        self.palabras: list[str] = palabras
        self.respuesta: str = respuesta
                
    def satisfied(self, assignment: dict[str, int]) -> bool:
        if len(set(assignment.values())) < len(assignment):
            return False
        
        if len(assignment) == len(self.letras):
            a: int = assignment["A"]
            b: int = assignment["B"]
            c: int = assignment["C"]
            d: int = assignment["D"]
            e: int = assignment["E"]
            f: int = assignment["F"]
            g: int = assignment["G"]
            h: int = assignment["H"]
            i: int = assignment["I"]
            j: int = assignment["J"]
            k: int = assignment["K"]
            l: int = assignment["L"]
            m: int = assignment["M"]
            n: int = assignment["N"]
            o: int = assignment["O"]
            p: int = assignment["P"]
            q: int = assignment["Q"]
            r: int = assignment["R"]
            s: int = assignment["S"]
            t: int = assignment["T"]
            u: int = assignment["U"]
            v: int = assignment["V"]
            w: int = assignment["W"]
            x: int = assignment["X"]
            y: int = assignment["Y"]
            z: int = assignment["Z"]
            #Aqui se deben mandar las palabras y sumar
            for palabra in self.palabras:
                ...
            return False
        return True

def solve_cryptarithmetic_puzzle(addends: list[str],answer: str) -> Optional[dict[str, int]]:
    temp = addends
    temp.append(answer)
    letrasTemp = set()
    a = ''.join([str(item).upper() for item in temp])
    for letrita in a:
        letrasTemp.add(str(letrita))
    letras  = list(a)
    letras.sort()
    valores_posibles : dict[str,list[int]] = {}
    for letra in letras:
        valores_posibles[letra] = [0,1,2,3,4,5,6,7,8,9]
    csp : CSP[str,int] = CSP(letras,valores_posibles)
    csp.add_constraint(cryptoarithmetic_puzzle_Constraint(letras,addends,answer))
    solucion : Optional[dict[str,int]] = csp.backtracking_search()
    if solucion is None:
        print('No hay solución')
        return None
    else:
        print('La solución es: ')
        return solucion


if __name__ == '__main__':
    solve_cryptarithmetic_puzzle(['hola','buenos','dias'],'no')