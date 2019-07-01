graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):
    q = []
    q.append(s)
    seen = []
    while q:
        vertex = q.pop(0)
        seen.append(vertex)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen and node not in q:
                q.append(node)
    return seen


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = []
    while stack:
        vertex = stack.pop()
        seen.append(vertex)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen and node not in stack:
                stack.append(node)

    return seen


if __name__ == "__main__":
    print(DFS(graph, "A"))