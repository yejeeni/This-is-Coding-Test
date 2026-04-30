from collections import deque

# 1이 통로고 지나다니는 1의 합 최솟값 구하기

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 행렬 상하좌우 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque() # 큐 생성
    queue.append((x, y)) # 큐에 탐색할 첫 위치 노드 추가

    while queue: # 큐가 빌 때까지
        # 큐에서 꺼내기
        x, y = queue.popleft()

        # 현재 위치 기준으로 상하좌우를 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 0인 부분에 들어온 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 노드의 값이 1이면 아직 방문하지 않았다는 것
            # 해당 노드를 처음 방문한 경우에 최단 거리를 기록
            if graph[nx][ny] == 1:
                # 이전 위치(x, y)까지의 최단 거리에 1칸을 더해 다음 위치(nx, ny)의 거리로 저장
                graph[nx][ny] = graph[x][y] + 1
                 # 다음 탐색을 위해 갱신된 위치를 큐에 추가
                queue.append((nx, ny))

    # 탐색이 모두 끝난 후 도착 지점(가장 오른쪽 아래)에 적힌 최단 거리를 반환 (인덱스가 0부터 시작하므로 n-1, m-1이 도착 지점임)
    return graph[n-1][m-1]

print(bfs(0, 0))