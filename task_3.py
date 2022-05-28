import json


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def parents(data):
    graph = {i['name']: set(i['parents']) for i in data}
    ans = {i: 0 for i in graph}
    for key in graph.keys():
        for vertex in dfs(graph, key):
            ans[vertex] += 1

    return ans


def main():
    json_data = json.loads(input())
    ans = parents(json_data).items()
    for i in sorted(ans):
        print(f"{i[0]} : {i[1]}")


if __name__ == '__main__':
    main()




