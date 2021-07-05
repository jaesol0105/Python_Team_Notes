import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수와 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 그래프 정보를 담을 인접 리스트
graph=[[] for _ in range(n+1)]
# 최단거리 테이블
distance = [INF] *(n+1)

# 간선의 정보 a에서 b까지 비용 c
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))

    while q:
        # python의 경우 최소힙기반의 우선순위큐 라이브러리
        # 큐 안에서 dist가 최소인 노드를 반환
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드일 경우
        if dist > distance[now]:
            continue

        # 인접 노드들을 큐에 삽입, 최단거리 테이블 갱신
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range (1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])