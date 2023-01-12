
#dfs 리컬젼에러땜에 다른 솔루션 봤는데 c++은 재귀 되나보더라,,,부럽,,
class Point:
    def __init__(self, x,y, color ):
        self.x = x
        self.y = y
        self.color = color

#p랑 똑같은 color들을 모두 visited 해버리기
def dfs(p, depth):
    global grid, visited
    # if depth>100: return []
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    nearlist=[]
    abnormalNearlist = []
    visited[p.x][p.y]=1 #일단 visited 처리

    #grid 좌표 값 안에 있는 것들 중에
    #위,아래,왼,오 색상 같은 것들 -> 그 주변에 색상 같은 애 있나 찾기
    #색상 다른 것 -> nearlist에 (x,y) 추가
    for i in range(4):
        if p.x+dx[i]<0 or p.x+dx[i]+1>len(grid) or p.y+dy[i]<0 or p.y+dy[i]+1>len(grid):
            continue
        if visited[p.x+dx[i]][p.y+dy[i]]==1: continue
        if p.color == grid[p.x+dx[i]][p.y+dy[i]]:
            nList = dfs(Point(p.x+dx[i], p.y+dy[i], p.color), depth+1)
            nearlist += nList
        else:
            nearlist.append( (p.x+dx[i], p.y+dy[i]) )
    #색상 다른 주변 좌표 리스트 리턴
    return list(set(nearlist))

def bfs(initP):
    global grid, visited
    # print('bfs calling: (%d,%d)'%(initP[0], initP[1]))
    normal = 0
    colorCount = 0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    Q=[initP]
    
    while Q:
        curr = Q.pop(0)
        if visited[curr[0]][curr[1]]==1: continue
        else: visited[curr[0]][curr[1]]=1
        for i in range(4):
            newX = curr[0] + dx[i]
            newY = curr[1] + dy[i]
            if newX>=0 and newX<len(grid) and newY>=0 and newY<len(grid) and visited[newX][newY]==0:
                #범위 내에 있고 한번도 보지 방문하지 않은 좌표 -> 색상 같을 때만 Q에 추가
                if grid[newX][newY] == grid[curr[0]][curr[1]]:
                    Q.append((newX,newY))

    return



N = int(input())
grid = []
visited = [[0]*N for _ in range(N)]
# visited2 = visited.copy()
for _ in range(N):
    grid.append(list(input()))

# normal = bfs((0,0))
normal = 0
for r in range(N):
    for c in range(N):
        if visited[r][c]==0:
            bfs((r,c))
            normal += 1


for r in range(N):
    for c in range(N):
        if grid[r][c]=="G":
            grid[r][c]="R"


visited = [[0]*N for _ in range(N)]
# abnormal = bfs((0,0))
# print('next: abnormal')
abnormal = 0
for r in range(N):
    for c in range(N):
        if visited[r][c]==0:
            bfs((r,c))
            abnormal += 1

print('%d %d'%(normal, abnormal))