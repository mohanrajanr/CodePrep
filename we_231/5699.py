import collections
import heapq
from typing import List


def countRestrictedPaths(n: int, edges: List[List[int]]) -> int:

    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append((edge[2], edge[1]))
        graph[edge[1]].append((edge[2], edge[0]))

    print(graph)


countRestrictedPaths(1, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]])



def dijkstras_adj_matrix():
    VERTICES = 4
    graph_vertices = []
    graph_edges = [[]]

    visited = [False] * VERTICES
    distance = [float('inf')] * VERTICES
    distance[0] = 0

    def minimumdist(dist, vis):
        minimum = float('inf')
        min_index = 0
        for i in graph_vertices:
            if distance[i] < minimum and visited[i] == False:
                minimum = distance[i]
                min_index = i

        return min_index

    for _ in graph_vertices:

        shortest_edge = minimumdist(distance, visited)

        for vert in graph_vertices:
            if graph_edges[shortest_edge][vert] > 0 and visited == False and \
                    distance[vert] > distance[shortest_edge] + graph_edges[shortest_edge][vert]:
                distance[vert] = distance[shortest_edge] + graph_edges[shortest_edge][vert]


def dijkstras_adj_list():
    graph = collections.defaultdict(list)

    VERTICES = 4
    minHeap = [(0, VERTICES)]

    distance = [float('inf')] * (VERTICES + 1)
    distance[VERTICES] = 0

    while minHeap:
        d, u = heapq.heappop(minHeap)

        # Old data not needed.
        if d != distance[u]:
            continue

        for w, v in graph[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                heapq.heappush(minHeap, (distance[v], v))

    return distance