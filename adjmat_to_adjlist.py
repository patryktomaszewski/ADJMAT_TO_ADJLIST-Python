# Patryk Tomaszewski, 302930

import random
from timeit import timeit
import sys
sys.setrecursionlimit(1500)
from typing import List, Dict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    dct = {}
    lst = []
    for row_num, row in enumerate(adjmat,1):
        for indx, val in enumerate(row,1):
            if val!=0:
                lst += [indx]*val

                dct[row_num] = lst[:]
        lst.clear()
    return dct






def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    return dfs_added(G, s)


def dfs_added(G: Dict[int, List[int]], s: int, visited = None) -> List[int]:
    if visited is None:
        visited = []
    visited.append(s)
    for x in (G[s]):
        if x not in visited:
            dfs_added(G, x, visited)

    return visited




def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack = [s]
    visited = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for x in reversed(G[v]):

                    stack.append(x)
    return visited








def is_acyclic_added(G: Dict[int, List[int]], s: int) -> bool:
    stack = [s]
    visited = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for x in reversed(G[v]):
                if x not in visited:
                    stack.append(x)
                elif G[x]:
                    return False

    return True




def is_acyclic(G: Dict[int, List[int]]) -> bool:
    keys = list(G.keys())
    for x in keys:
        if is_acyclic_added(G,x) is False:
            return False
    return True

