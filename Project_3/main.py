import heapq
import math
import sys
import time

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

#Project 3 Question 3
#NOTE TO SELF: 'self'.whatever is like 'this'.whatever

class Graph:
    def __init__(self): #Constructor
        self.nodes = set() #variable to store nodes
        self.edges = {} #dictionary to store edges
    
    def add_edge(self, u, v, weight): #add edge to digraph
        self.nodes.update([u, v])
        self.edges.setdefault(u, []).append((v, weight))
        self.edges.setdefault(v, []).append((u, weight))  #Undirected Graph
    
    def dijkstra(self, start): #Djikstra's algorithm
        shortest_paths = {node: float('inf') for node in self.nodes} # set all nodes to infinity weight and therefore unreachable by default until weight is known
        shortest_paths[start] = 0 #set start weight to 0
        priority_queue = [(0, start)] #initialize min-heap for dijkstra's with 0 distance from starting node of zero weight
        predecessors = {} #empty dictionary
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > shortest_paths[current_node]: #if current distance exceeds shortest path of the current node, skip this path
                continue
            
            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight
                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return shortest_paths, predecessors
    
    def prim(self): #
        if not self.nodes: #if no nodes, return empty array
            return []
        
        start = next(iter(self.nodes))  # Arbitrary starting point
        mst = []
        visited = set([start])
        edges = [(weight, start, neighbor) for neighbor, weight in self.edges[start]]
        heapq.heapify(edges)
        
        while edges:
            weight, u, v = heapq.heappop(edges)
            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                for next_node, next_weight in self.edges[v]:
                    if next_node not in visited:
                        heapq.heappush(edges, (next_weight, v, next_node))
        
        return mst

#Graph provided
g = Graph()
g.add_edge('A', 'B', 22)
g.add_edge('A', 'C', 9)
g.add_edge('A', 'D', 12)

g.add_edge('B', 'C', 35)
g.add_edge('B', 'F', 36)
g.add_edge('B', 'H', 34)

g.add_edge('C', 'D', 4)
g.add_edge('C', 'E', 65)
g.add_edge('C', 'F', 42)

g.add_edge('D', 'E', 33)
g.add_edge('D', 'I', 30)

g.add_edge('E', 'F', 18)
g.add_edge('E', 'G', 23)

g.add_edge('F', 'G', 21)
g.add_edge('F', 'H', 24)

g.add_edge('G', 'H', 25)
g.add_edge('G', 'I', 21)

g.add_edge('H', 'I', 19)


# (a) Dijkstra's Algorithm
shortest_paths, predecessors = g.dijkstra('A')
print("Shortest Path Tree:", shortest_paths)

# (b) Prim's Algorithm
mst = g.prim()
print("Minimum Spanning Tree:", mst)
