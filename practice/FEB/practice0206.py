
graph =[]



visited = [False] * 7 

start = 0
stack =  [start]
visited[start] = True

while stack:
    cur = stack.pop()
    for adj in graph[cur]:
        if not visited[adj]:
            visited[adj] = True
            stack.append(adj)
# 함수로 만들기
def dfs(start):
    stack =  [start]
    visited[start] = True

    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)