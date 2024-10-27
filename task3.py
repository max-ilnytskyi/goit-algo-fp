import heapq
import networkx as nx


def dijkstra(graph, start):
    shortest_distances = {node: float("inf") for node in graph.nodes}
    shortest_distances[start] = 0

    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > shortest_distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return shortest_distances


distances = {
    ("Paris", "London"): 343,
    ("Paris", "Madrid"): 1054,
    ("Paris", "Berlin"): 878,
    ("Paris", "Milan"): 639,
    ("London", "Berlin"): 930,
    ("Madrid", "Milan"): 1185,
    ("Berlin", "Milan"): 842,
}

G = nx.Graph()
for (start, end), weight in distances.items():
    G.add_edge(start, end, weight=weight)

start_node = "Madrid"
shortest_paths = dijkstra(G, start_node)

print(f"Shortest paths from city '{start_node}':")
for city, distance in shortest_paths.items():
    print(f"To city '{city}': {distance} km")
