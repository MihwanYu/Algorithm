
def solution():
    M,N,K = map(int, input().split())
    grid = [[0]*N for _ in range(M) ] #MxN sized
    visited = [[False]*N for _ in range(M)]
    cabbages = []
    numworms = 0

    for _ in range(K):
        r, c = map(int, input().split())
        grid[r][c] = 1
        cabbages.append( (r,c) )
    
    for c in cabbages:
        if not visited[c[0]][c[1]]:
            # print(c)
            bfs(grid, visited, c)
            numworms +=1
            
    print('최소지렁이: ',numworms)

def bfs(grid, visited, c):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    Q = [c]
    while Q:
        cur = Q.pop(0)
        for i in range(4):
            newX = cur[0]+dx[i]
            newY = cur[1]+dy[i]
            #새로만든 좌표가 범위내에 있는데 양배추가 심겨져 있고 한번도 방문하지 않았다면
            if newX>=0 and newX<len(grid) and newY>=0 and newY<len(grid[0]):
                if grid[newX][newY]==1 and visited[newX][newY]==False:
                    visited[newX][newY] = True
                    Q.append( (newX, newY) )



if __name__=="__main__":
    testcase = int(input())
    for _ in range(testcase):
        solution()