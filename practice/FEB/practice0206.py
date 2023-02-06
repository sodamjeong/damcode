
# graph =[]



# visited = [False] * 7 

# start = 0
# stack =  [start]
# visited[start] = True

# while stack:
#     cur = stack.pop()
#     for adj in graph[cur]:
#         if not visited[adj]:
#             visited[adj] = True
#             stack.append(adj)
# # 함수로 만들기
# def dfs(start):
#     stack =  [start]
#     visited[start] = True

#     while stack:
#         cur = stack.pop()
#         for adj in graph[cur]:
#             if not visited[adj]:
#                 visited[adj] = True
#                 stack.append(adj)


def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9

dfs(graph,1,visited)