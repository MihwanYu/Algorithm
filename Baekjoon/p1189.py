import copy
# list 깊은복사 -> copy.deepcopy(배열)
def solution():
    R,C,K = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    visited = [[-1]*C for _ in range(R)]
    han = [R-1, 0]
    # home = [0, C-1]
    cntK = 0
    cntK = dfs(grid, visited, K, cntK, han, 1)
    print(cntK)

def dfs(grid, visited, K, cntK, han, count):
    visited[han[0]][han[1]] = count #현재 위치 count값 넣어주기
    # print('count: %d'%count)
    # for v in visited:
    #     print(v)
    # print('\n-------------------\n')
    #현위치==목적지일 때, 그동안의 거리가 K와 같으면 K거리 가짓수에 +1
    if han[0]==0 and han[1]==len(grid[0])-1:
        if visited[han[0]][han[1]]==K:
            cntK +=1
            # print('-')
        return cntK
        # return

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    # print('cur: ',han)
    # print('len(grid): %d, len(grid[0]: %d'%(len(grid), len(grid[0])))
    for i in range(4):
        
        newX = han[0]+dx[i]
        newY = han[1]+dy[i]
        # print('new: (%d,%d)'%(newX,newY))
        if newX>=0 and newX<len(grid) and newY>=0 and newY<len(grid[0]):
            # print('-')
            if grid[newX][newY]=='.' and visited[newX][newY]==-1:
                # print(';')
                #(newX,newY) 좌표에 길 있고 방문한 적 없으면 방문
                newvisited = copy.deepcopy(visited)
                cntK = dfs(grid, newvisited, K, cntK, [newX,newY], count+1)
    
    return cntK

if __name__=="__main__":
    solution()
        