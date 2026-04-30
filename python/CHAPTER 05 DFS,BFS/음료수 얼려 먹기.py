# n*m 얼음틀에서 구멍이 뚫린 부분은 0, 칸막이가 있는 부분은 1. 뚫린 부분 끼리 상하좌우로 붙어있는 경우 서로 연결되어 있는 것으로 간주
# 얼음틀 모양이 주어졌을 때 생성되는 총 아이스크림의 수?

# 성공조건: 값이 0인 칸
# 종료조건: 값이 1인 칸, 틀 범위 이탈

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y): # x, y: 현재 노드 좌표
    # 범위를 벗어난 경우 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    # 현재 노드가 아직 방문하지 않은 노드인 경우
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상하좌우 탐색
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True # 탐색 끝나면 아이스크림 하나
    
    return False # 빈 공간 아님

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)