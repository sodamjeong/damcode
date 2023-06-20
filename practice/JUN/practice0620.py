#24480

import sys
sys.setrecursionlimit(10**6)
#만약 재귀를 사용해서 풀어야 하는 문제라면, 위 코드를 상단에 쓰는 것은 선택이 아닌 필수이다. 
#파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다. 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데, 문제는 코딩테스트 환경에서는 에러 메시지를 볼 수 없다는 것이다.
input = sys.stdin.readline

n, m, num = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
cnt = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(start):
  global cnt
  cnt += 1
  visit[start] = cnt   
  for i in sorted(graph[start],reverse=True):
    if not visit[i]:
            dfs(i)

dfs(num)
print(*visit[1:],sep='\n')