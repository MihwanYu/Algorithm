
def solution():
    N,M = map(int, input().split())
    grid = []
    visited = [[-1]*M for _ in range(N)]
    for _ in range(N):
        grid.append(list(map(int, list(input()))))
    bfs(grid, visited)

def bfs(grid, visited):
    startX,startY = 0,0
    endX,endY = len(grid)-1, len(grid[0])-1
    visited[0][0] = 1 #첫 시작1

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    Q = [[startX,startY]]
    
    while Q:
        cur = Q.pop(0)
        if grid[cur[0]][cur[1]]==0: continue #중복된 값이 Queue에 많이 들어가면 시간 초과 발생
        grid[cur[0]][cur[1]] = 0 #한번 방문한 곳 더이상 방문 안하도록
        for i in range(4):
            newX = cur[0]+dx[i]
            newY = cur[1]+dy[i]
            if newX>=0 and newX<len(grid) and newY>=0 and newY<len(grid[0]):
                if grid[newX][newY]==1:
                    visited[newX][newY] = visited[cur[0]][cur[1]]+1
                    Q.append([newX,newY])
                    if newX==endX and newY==endY: break

    print(visited[endX][endY])
    # for v in visited:
    #     print(v)


if __name__=="__main__":
    solution()