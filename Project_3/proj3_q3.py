import heapq

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