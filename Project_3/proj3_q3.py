import heapq

# Project 3 Question 3
# NOTE TO SELF: 'self'.whatever is like 'this'.whatever

class Graph:
    def __init__(self):  # Constructor
        self.nodes = set()  # Variable to store nodes
        self.edges = {}  # Dictionary to store edges
    
    def add_edge(self, u, v, weight):  # Add edge to digraph
        self.nodes.update([u, v])  # Add nodes to the set
        self.edges.setdefault(u, []).append((v, weight))  # Store edges
        self.edges.setdefault(v, []).append((u, weight))  # Undirected Graph
    
    def dijkstra(self, start):  # Dijkstra's algorithm
        shortest_paths = {node: float('inf') for node in self.nodes}  # Set all nodes to infinity weight (unreachable by default)
        shortest_paths[start] = 0  # Set start node weight to 0
        priority_queue = [(0, start)]  # Initialize min-heap with starting node at distance 0
        predecessors = {}  # Empty dictionary to store shortest path tree
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > shortest_paths[current_node]:  # Skip if a shorter path is already found
                continue
            
            # Ensure consistent order when iterating through neighbors
            for neighbor, weight in sorted(self.edges.get(current_node, [])):
                distance = current_distance + weight
                if distance < shortest_paths[neighbor]:  # Found a shorter path
                    shortest_paths[neighbor] = distance
                    predecessors[neighbor] = current_node  # Track the shortest path tree
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return shortest_paths, predecessors  # Return shortest path distances and the path tree
    
    def prim(self):  # Prim's Algorithm for Minimum Spanning Tree (MST)
        if not self.nodes:  # If no nodes, return empty list
            return []
        
        start = min(self.nodes)  # Always pick the lexicographically smallest node for consistency
        mst = []  # List to store the MST
        visited = set([start])  # Set to keep track of visited nodes
        edges = [(weight, start, neighbor) for neighbor, weight in sorted(self.edges[start])]  # Initialize priority queue with edges from start node
        heapq.heapify(edges)  # Convert edges to a min-heap
        
        while edges:
            weight, u, v = heapq.heappop(edges)  # Get edge with smallest weight
            if v not in visited:  # If the node has not been visited, add to MST
                visited.add(v)  # Mark node as visited
                mst.append((u, v, weight))  # Add edge to MST
                for next_node, next_weight in sorted(self.edges[v]):  # Iterate neighbors in sorted order
                    if next_node not in visited:
                        heapq.heappush(edges, (next_weight, v, next_node))  # Push next edge to heap
        
        # If not all nodes were visited, the graph is disconnected
        if len(visited) != len(self.nodes):
            print("Warning: The graph is disconnected. Prim's algorithm only found an MST for one component.")

        return mst  # Return the list of edges in the MST

# Graph provided
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
print("Shortest Path Tree:", dict(sorted(shortest_paths.items(), key=lambda x: x[1])))  # Sort output by shortest path distance for consistency

# (b) Prim's Algorithm
mst = g.prim()
print("Minimum Spanning Tree:", mst)  # Output consistent MST
