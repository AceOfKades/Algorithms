import sys
import math


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

    
    