#!/usr/bin/env python

from collections import defaultdict
from functools import lru_cache

def length(a, b, nbrs=None, cache=None, depth=0):
    vis = '|... '
    a, b = sorted([a, b])

    print(vis*depth + f'called: a={a}, b={b}')
    if (a, b) in cache: 
        ans = cache[a, b]
        if ans is not None:
            print(vis*depth + f'already in cache: a={a}, b={b}, cached={ans}')
            return ans
        else:
            return float('inf')
    cache[a,b] = None

    if a in nbrs[b]: 
        ans = 1
    else:
        subprobs = [1+length(a, nbr, nbrs=nbrs, cache=cache, depth=depth+1) 
                    for nbr in nbrs[b] 
                    if ((a, nbr) not in cache or cache[a, nbr] is not None)]
        subprobs += [1+length(b, nbr, nbrs=nbrs, cache=cache, depth=depth+1) 
                     for nbr in nbrs[a]
                     if ((a, nbr) not in cache or cache[a, nbr] is not None)]
        print(vis*depth, subprobs)
        ans = min(subprobs)
                
    print(vis*depth + f'a={a}, b={b}, ans={ans}')

    cache[a, b] = ans
    return ans


while True:
    try:
        n = int(input())
    except EOFError:
        exit()
    
    nbrs = defaultdict(set) 
    cache = dict()

    for i in range(n-1):
        a, b = map(int, input().split())

        nbrs[a].add(b)
        nbrs[b].add(a)

    distances = {(start,end): 1+length(start, end, nbrs=nbrs, cache=cache) 
                 for start in range(1, n//2+1)
                 for end in range(start*2, n+1, start)}
    
    print(distances, sum(distances.values()))
