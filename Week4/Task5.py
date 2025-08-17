# Write a program to find the shortest path in a graph using Dijkstra's algorithm.

import heapq

def dijkstra(graph, start):
    """
    Finds the shortest path from start to all other nodes in the graph using Dijkstra's algorithm.
    graph: dict where keys are nodes and values are dicts of neighbors and edge weights.
    Returns a dictionary of shortest distances from start to each node.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# Example usage:
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)
    print(f"Shortest paths from {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"{node}: {distance}")