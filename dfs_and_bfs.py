from collections import deque

'''(BFS) DEQUE 사용'''
def bfs(x):
    q = deque([x])
    visited[x] = True

    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

'''(DFS) 재귀 사용'''
def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


n, m, start = map(int, input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
dfs(start)
print()
visited = [False] * (n + 1)
bfs(start)


'''
[입력예시]
4 5 1 (노드의 개수, 간선의 개수, 시작위치)
1 2
1 3
1 4
2 4
3 4

grape=[[2,3,4],
       [1,4],
       [1,4],
       [2,3]
      ]

[출력]
1 2 4 3 
1 2 3 4
'''
