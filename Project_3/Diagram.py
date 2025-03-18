
import math
import sys
import time
import heapq
#import resource
from itertools import groupby
from collections import defaultdict
def compute_scc(graph):
    # Step 1: DFS to fill the stack with vertices in order of finishing times
    def dfs_fill_stack(u, visited, stack):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs_fill_stack(v, visited, stack)
        stack.append(u)

    # Step 2: DFS on the reversed graph to find SCCs
    def dfs_reverse(u, visited, component, reversed_graph):
        visited.add(u)
        component.append(u)
        for v in reversed_graph[u]:
            if v not in visited:
                dfs_reverse(v, visited, component, reversed_graph)

    # Step 3: Reverse the graph
    reversed_graph = defaultdict(set)
    for u in graph:
        for v in graph[u]:
            reversed_graph[v].add(u)

    # Step 4: Find SCCs
    stack = []
    visited = set()
    for u in graph:
        if u not in visited:
            dfs_fill_stack(u, visited, stack)

    visited = set()
    sccs = {}
    while stack:
        u = stack.pop()
        if u not in visited:
            component = []
            dfs_reverse(u, visited, component, reversed_graph)
            sccs[u] = component

    return sccs


# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

#BFS_Paths.py example given off black board.
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                print(path + [next])
                yield path + [next]               
            else:
                queue.append((next, path + [next]))




if __name__ == "__main__":
    graphforquestionone = {'A': set(['B','F','E']),
                           'B': set(['A','F','C']),
                           'C': set(['B','G','D']),
                           'D': set(['C','G']),
                           'E': set(['A','F','I']),
                           'F': set(['E','A','B','I']),
                           'G': set(['C','D','J']),
                           'H': set(['K','L']),
                           'I': set(['E','F','J','M']),
                           'J': set(['I','G']),
                           'K': set(['H','L','O']),
                           'L': set(['K','H','P']),
                           'M': set(['I','N']),
                           'N': set(['M']),
                           'O': set(['K']),
                           'P': set(['L'])}
    #Question1-A & B & C
    One = list(dfs_paths(graphforquestionone,'A','F'))
    print("DFS Paths:","\n",One)
    print("\nBFS paths:")
    One = list(bfs_paths(graphforquestionone,'A','F'))
    print(One,"\n\n")
###################################################################
    start = time.time()
    Graphforquestiontwo = {'1': set(['3']),
                           '2': set(['1']),
                           '3': set(['2','5']),
                           '4': set(['1','2','12']),
                           '5': set(['8','6']),
                           '6': set(['8','10','7']),
                           '7': set(['10']),
                           '8': set(['9','10']),
                           '9': set(['5','11']),
                           '10': set(['9','11']),
                           '11': set(['12']),
                           '12': set([])}
    
    # Start timing
    start_time = time.time()

    # Compute SCCs
    sccs = compute_scc(Graphforquestiontwo)

    # End timing
    end_time = time.time()
    execution_time = end_time - start_time

    # Print SCCs
    print("Strongly connected components are:")
    for key in sccs:
        print(sccs[key])

    # Find the top 5 largest SCCs
    top_5 = heapq.nlargest(5, sccs, key=lambda x: len(sccs[x]))
    result = []
    for i in range(5):
        try:
            result.append(len(sccs[top_5[i]]))
        except:
            result.append(0)
     

    
    