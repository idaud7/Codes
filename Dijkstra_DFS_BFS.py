from collections import deque
import heapq
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
     current_distance, current_vertex = heapq.heappop(pq)
    if current_distance > distances[current_vertex]:
        continue
    for neighbor, weight in graph[current_vertex].items():
     distance = current_distance + weight
    if distance < distances[neighbor]:
     distances[neighbor] = distance
    heapq.heappush(pq, (distance, neighbor))
    return distances

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
    vertex = queue.popleft()
    if vertex not in visited:
    visited.add(vertex)
    queue.extend(graph[vertex] - visited)
    return visited

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
    vertex = stack.pop()
    if vertex not in visited:
    visited.add(vertex)
    stack.extend(graph[vertex] - visited)
    return visited

