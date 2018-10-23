import sys


def matrix_to_edge_list(adj):
    """
    Converts an adjacency matrix to a list of edges.
    """
    edges = []
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if adj[i][j] != sys.maxsize:
                edges.append((i, j, adj[i][j]))  # (i, j, weight)
    return edges


def bellman_ford(adj, src):
    """
    Bellman-Ford algorithm for single-source shortest paths.

    Returns a list where element i contains the shortest possible distance
    from the src vertex to vertex i.

    Can be used to detect negative cycles.
    """
    # Convert adjacency matrix to a list of edges
    edges = matrix_to_edge_list(adj)

    n = len(adj)
    d = [sys.maxsize for _ in range(n)]
    d[src] = 0

    # Relax edges up to n - 1 times: O(|V|*|E|)
    for _ in range(n - 1):
        changed = False

        for edge in edges:
            u = edge[0]
            v = edge[1]
            weight = edge[2]

            if d[u] + weight < d[v]:
                d[v] = d[u] + weight
                changed = True

        if not changed:
            break
    
    # If we do one more iteration of relaxations and there is a change,
    # we know that there is a negative cycle.
    for edge in edges:
        u = edge[0]
        v = edge[1]
        weight = edge[2]

        if d[u] + weight < d[v]:
            # Do what you want to do when there is a negative cycle
            pass

    return d