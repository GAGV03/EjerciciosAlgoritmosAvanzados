#----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 17-Nov-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01777771 Erickx Navarro
#----------------------------------------------------------

WeightedGraph = dict[str, set[tuple[str, float]]]


def dijkstra_spt(initial: str,graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    
    visited: set[str]
    univisited: set[str]
    cost_dict: dict[str,int]= {}
    resulting_spt: WeightedGraph = {}
    
    for i in graph:
        print(i)
    
    
    
    # The function's code goes here
    ...
    return ({},{})