INF = int(1e9)

# 노드의 개수 와 간선의 개수
n = int(input())
m = int(input())

# 그래프를 표현할 2차원 인접 행렬
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0 으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a ==b:
            graph[a][b] = 0

# 간선 정보 입력 a에서 b로가는 비용 c
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()


