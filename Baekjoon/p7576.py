
def mature(Q):
    global grid, visited, day
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    dailyQ = [Q]
    while bool(dailyQ) :
        tomatoes = dailyQ.pop(0)
        # print('popped tomates: ',tomatoes)
        new_tomatoes = []
        for tomato in tomatoes:
            #리스트에서 빼낸 토마토 == 접근한 토마토 -> visited 표시해줌
            visited[tomato[0]][tomato[1]] = -1
            for i in range(4):
                new_t = (tomato[0]+dx[i], tomato[1]+dy[i])
                if new_t[0]>=0 and new_t[0]<len(grid) and new_t[1]>=0 and new_t[1]<len(grid[0]):
                    if grid[new_t[0]][new_t[1]]==0:
                        grid[new_t[0]][new_t[1]] = 1
                        new_tomatoes.append(new_t)
                        # print('new tomato: ',new_t)
                    
        # print('daily Q appends ',new_tomatoes)
        if new_tomatoes: dailyQ.append(new_tomatoes)
        day += 1   

    # 접근하지 못하는 토마토가 있을 경우
    for row in grid:
        if 0 in row:
            day = 0
            return
    return

M,N = map(int, input().split())
grid = []#격자
ones = []#익은것들 좌표

day = 0
for r in range(N):
    row = list(map(int, input().split()))
    ones += [(r,i) for i in range(M) if row[i]==1]
    grid.append(row)

visited = grid.copy()#방문좌표는 다 -1로 채울거임
mature(ones)
print(day-1)


# if __name__=="__main__":
#     solution()
        