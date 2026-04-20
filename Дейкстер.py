

def my_func(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    
    while len(visited) < len(graph):
        current = None
        min_distance = float('inf')
        
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current = node
        
        if current is None:
            break
            
        visited.add(current)
        
        for neighbor, weight in graph[current]:
            new_distance = distances[current] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    
    return distances
  
graph = {
  'A': [('B', 5), ('C', 2)],
  'B': [('D', 3)],
  'C': [('B', 1), ('D', 6)],
  'D': []
}

result = my_func(graph, 'A')
print(result) 
