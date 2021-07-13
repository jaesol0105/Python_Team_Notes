n,m = map(int,input().split())

# 간선, 부모테이블
edges = []
parent = [0] * (n+1)

# 부모노드 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i] = i

# 간선 정보 입력 받기
for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

# cost 기준 오름차순 정렬
edges.sort()
result = 0

# cost, a , b = edge
for edge in edges:
    # 사이클이 발생하지 않을 경우에만 union 연산 수행
    if find_parent(parent,edge[1]) != find_parent(parent, edge[2]):
        union_parent(parent,edge[1],edge[2])
        result += edge[0]

print(result)