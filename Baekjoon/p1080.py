
def solution():
    N, M = map(int, input().split())
    #3x3 크기 행렬만큼만 뒤집어서 mat1 -> mat2 똑같이 만들기
    #알고리즘 분류: 그리디
    mat1=[]
    mat2=[]
    count = 0
    
    for _ in range(N):
        mat1.append(list(map(int, list(input())))) # 0, 0, 0, 0 식으로 인풋
    
    for _ in range(N):
        mat2.append(list(map(int, list(input()))))

    if N<3 or M<3:
        # 3x3 사이즈보다 작지만 완전히 똑같다면 0<--생각못했던반례
        if mat1==mat2:
            print(0)
        else:
            print(-1)
        return 
    
    for i in range(N-2):
        for j in range(M-2):
            # print(mat1[i][j], end=' ')
            if mat1[i][j] != mat2[i][j]:
                mat1 = reverse_mat(i,j,mat1)
                count +=1
            '''mat1==mat2로 나중에 확인할수있었던것,,
            if j==M-3:
                isSame = mat1[i][j+1]==mat2[i][j+1] and mat1[i][j+2]==mat2[i][j+2]
                if not isSame:
                    print(-1)
                    return
            if i==N-3:
                isSame = mat1[i+1][j]==mat2[i+1][j] and mat1[i+2][j]==mat2[i+2][j]
                if not isSame:
                    print(-1)
                    return

    # 마지막 2x2 격자판도 모두 같은지 확인
    isSame = mat1[N-2][M-2]==mat2[N-2][M-2] and mat1[N-2][M-1]==mat2[N-2][M-1] and mat1[N-1][M-2]==mat2[N-1][M-2] and mat1[N-1][M-1]==mat2[N-1][M-1]
    if not isSame:
        print(-1)
        return
    '''

    if mat1==mat2:
        print(count)
    else:
        print(-1)
            
def reverse_mat(i,j,mat):
    #i부터 i+1, i+2
    #j부터 j+1, j+2 값 바꿔서 리턴
    for r in range(i,i+3):
        for c in range(j,j+3):
            mat[r][c] = abs(mat[r][c]-1)
    return mat


if __name__=="__main__":
    solution()
        