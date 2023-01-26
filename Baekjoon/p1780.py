def isallsame(grid):
    if len(set([tuple(item) for item in grid]))>1: return False
    if len(set(grid[0]))>1: return False
    return True

def solution():
    N = int(input())
    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))
    if isallsame(paper):
        if paper[0][0]== -1: answer =  [1,0,0]
        elif paper[0][0]== 0: answer =  [0,1,0]
        elif paper[0][0]==1: answer =  [0,0,1]
        # answer = [paper[0].count(-1), paper[0].count(0), paper[0].count(1)]
    else:
        answer = dfs(paper)
    for ans in answer:
        print(ans)


def dfs(paper):
    if len(paper)==3: # 3x3 size일때
        if isallsame(paper):
            if paper[0][0]== -1: return [1,0,0]
            elif paper[0][0]== 0: return [0,1,0]
            elif paper[0][0]==1: return [0,0,1]
            # return [paper[0].count(-1), paper[0].count(0), paper[0].count(1)]
        flatten = []
        for p in paper:
            flatten += p
        return [flatten.count(-1), flatten.count(0), flatten.count(1)]

    nneg = 0
    nzero = 0
    npos = 0

    for i in range(0, len(paper), len(paper)//3):
        partial = paper[i:i+len(paper)//3]
        for j in range(0, len(paper), len(paper)//3):
            ngrid = [row[j:j+len(paper)//3] for row in partial]

            if isallsame(ngrid): #다 똑같을경우 한개 종이로 인정
                if ngrid[0][0]== -1: answer = [1,0,0]
                elif ngrid[0][0]== 0: answer = [0,1,0]
                elif ngrid[0][0]==1: answer = [0,0,1]
                # answer = [ngrid[0].count(-1), ngrid[0].count(0), ngrid[0].count(1)]
            else:
                answer = dfs(ngrid)
            # print(ngrid)
            # print(answer, end='\n----------------\n')
            nneg += answer[0]
            nzero += answer[1]
            npos += answer[2]
    # print(nneg, nzero, npos)
    return [nneg, nzero, npos]
            

if __name__=="__main__":
    solution()