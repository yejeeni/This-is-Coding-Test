"""
1. 시작 노드 처리

탐색을 시작할 노드를 큐에 넣는다(append)
시작 노드의 방문 목록에 체크를 한다(visited[start] = True)

2. 큐가 빌 때까지 반복

큐의 맨 앞에서 노드 하나를 꺼낸다(popleft) 이 노드가 현재 탐색의 기준 노드가 된다.
현재 노드와 간선으로 직접 연결된 모든 이웃 노드를 하나씩 확인한다.

만약 이웃 노드를 아직 방문하지 않았다면 (if not visited[neighbor]:)
그 이웃 노드를 큐에 넣는다 (append)

방문 목록에 체크를 한다 (visited[neighbor] = True)

(최단 거리 문제의 경우) 현재 노드까지의 거리에 1을 더해 기록한다
"""


from collections import deque

def bfs(graph, start, visited):
    # 시작노드를 큐에 추가
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    while queue: # 큐가 빌 때까지 반복
        # 큐에서 원소 하나 pop
        v = queue.popleft()
        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트로 표현
visited = [False] * 9

bfs(graph, 1, visited)