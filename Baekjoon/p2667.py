
def solution():
    N = int(input())
    grid = [list(map(int, list(input())))   for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    houses = []
    for i in range(N):
        for j in range(N):
            #집 있는데 방문은 안했을 경우 -> bfs로 방문 후 단지 수 리턴
            if grid[i][j]==1 and visited[i][j]==False:
                cnt = bfs(grid, visited, i, j)
                houses.append(cnt)
    # print('-'*30)
    print(len(houses))
    houses.sort()
    for c in houses:
        print(c)

def bfs(grid, visited, i, j):
    count = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    Q = [[i,j]]
    while Q:
        cur = Q.pop(0)
        if visited[cur[0]][cur[1]]==True: continue
        visited[cur[0]][cur[1]] = True #현위치 방문 처리
        count +=1 #현위치 카운트
        for i in range(4):
            newX = cur[0]+dx[i]
            newY = cur[1]+dy[i]
            if newX>=0 and newX<len(grid) and newY>=0 and newY<len(grid):
                #인접 x,y에 집이 있고 방문한 적 없을 때 -> Queue에 추가
                if grid[newX][newY]==1 and visited[newX][newY]==False:
                    Q.append([newX, newY])
    # print('i: %d, j: %d, count: %d'%(i,j,count))
    return count

if __name__=="__main__":
    solution()