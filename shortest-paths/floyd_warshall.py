import sys


def floyd_warshall(adj):
    """
    Returns a matrix where element i, j contains the minimum distance
    between vertex i and vertex j using the Floyd-Warshall algorithm.

    dist[i][j] is sys.maxsize if there is no path from i to j.

    Assumes that no distance is larger than sys.maxsize.

    Good choice when the given graph is dense. Running time is O(|V|^3).
    Works with negative weights, as long as there are no negative cycles.
    """
    n = len(adj)

    # Initialize dist matrix: O(n^2)
    dist = [
        [sys.maxsize for _ in range(n)] for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            dist[i][j] = adj[i][j]
    
    # Vertices have 0 distance to themselves: O(n)
    for i in range(n):
        dist[i][i] = 0
    
    # O(n^3)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Can check for negative cycles by checking if any vertex now
    # has a negative distance to itself (dist[i][i] < 0)
    
    return dist