from collections import deque

# 노드의 수, 간선의 수
n, m = map(int, input().split())

# 각 노드에 대한 진입차수
indegree = [0] * (n+1)

# 간선 정보를 담을 인접 리스트
graph = [[] for _ in range(n+1)]

# 간선 정보 입력받기, 진입차수 계산
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q=deque()
    result = []

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i,end=' ')

topology_sort()