#구슬 탈출
#직사각형 보드, 빨간구슬 & 파란구슬 하나씩 넣고 빨간 구슬을 빼낸다

#10번 이하로 움직여서 빨간 구슬을 빼낼 수 없으면 -1 출력
N, M = [int(i) for i in input().split()]
board = []
locations={}
for n in range(N):
    row = input()
    if 'O' in row:
        locations['O'] = (n,row.index('O'))
    if 'R' in row:
        locations['R'] = (n,row.index('R'))
    if 'B' in row:
        locations['B'] = (n,row.index('B'))
    board.append(row)

count = 0
# print('loc of hole and marbles: ',locations)

def ismatch():
    global locations
    if locations['O'][0]==locations['R'][0]:
        r=locations['O'][0]
        for i in range(min(locations['O'][1],locations['R'][1])+1, max(locations['O'][1],locations['R'][1])):
            if locations[r][i]!='.': return False
        return True
    if locations['O'][1]==locations['R'][1]:
        c=locations['O'][1]
        for i in range(min(locations['O'][0],locations['R'][0])+1, max(locations['O'][0],locations['R'][0])):
            if locations[i][c]!='.': return False
        return True
    return False


def search():
    pass
    #case left

    #case right

    #case up

    #case down


if ismatch():
    count += 1
    print('끝')
else:
    search()

print(count)