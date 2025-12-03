import copy

# Pseudo code:
# initialize max_flow to 0
# while there is an augmenting path:
#   add augmenting path's min residual capacity to max_flow
# return max_flow


# graph is given adjaency matrix of size n and 0 <= source != target < n
# while there  is an augmenting path
#   m <- capacity of smallest edge along the augmenting path
#   max_flow <- max_flow + m
#   add m flow to every edge along the augmenting path
def ford_fulkerson(graph, source, target):
    residual = copy.deepcopy(graph)
    max_flow = 0
    path = find_path(residual, source, target)
    while path is not None:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        min_capacity = min(residual[u][v] for u, v in edges)
        max_flow += min_capacity
        for u, v in edges:
            residual[u][v] -= min_capacity
        path = find_path(residual, source, target)
    return max_flow


# 12345678901234567890123456789012345678901234567890123456789012345678901234567890
def find_path(graph: list[list[int]], source: int, target: int):
    """Return a path -- any path -- from source to target in the graph"""

    # Initialize return item
    path: list[int] = None

    # Make sure inputs are ok
    if graph is not None:
        n: int = len(graph)
        if n > 0 and (0 <= source < n) and (0 <= target < n):

            # Initialize DFS tools
            no_edge: int = graph[0][0]  # absence of edge
            marked: list[int] = [source]  # vertices already processed
            found: bool = False  # Flags detection of path

            # What vertex to explore next and what is the path
            # to it. The information is stored as a tuple in
            # the form:
            #  (vertex, path_to_this_vertex)
            # with path_to_this_vertex being a list of the
            # vertices alonγ the path.
            stack: list[(int, list[int])] = [(source, [source])]

            while len(stack) > 0 and not found:
                # Explore the next vertex from the stack
                (u, path_from_source_to_u) = stack.pop()
                found = u == target
                if found:
                    # u is the end of the path, so we got what we are
                    # looking for
                    path = path_from_source_to_u
                else:
                    # Explore the neighbors of u, hopefully one of them
                    # will get us a stop closer to the target vertex.
                    v: int = n - 1
                    while v >= 0:
                        if graph[u][v] != no_edge and v not in marked:
                            marked.append(v)
                            stack.append((v, path_from_source_to_u + [v]))
                        v -= 1
    return path


G = [  #  A   B   C   D   E
    [0, 20, 0, 0, 0],  # A
    [0, 0, 5, 6, 0],  # B
    [0, 0, 0, 3, 7],  # C
    [0, 0, 0, 0, 8],  # D
    [0, 0, 0, 0, 0],  # E
]

print(ford_fulkerson(G, 0, 4))
