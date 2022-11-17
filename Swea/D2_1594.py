T = int(input())
for test_case in range(1, T + 1):
    print("#%d"%test_case)
    N = int(input())
    maxN = N**2
    # board = [[0]*N]*N #이렇게 하면 board[0][0]=1 넣었을 때 모든 row의 0번째 column에 1이 들어가게 된다
    # https://stackoverflow.com/questions/13157961/2d-array-of-zeros
    board = [[0]*N for _ in range(N)] #numpy 안쓰고 배열 만드려면 이렇게 해야함
    row= col = 0
    #1:right 2:down 3:left 4:right
    def fill(idx, dir):
        global board, row, col
        if idx>maxN: return
        if dir==1:
            # print('오른쪽 채우기, row=%d, col=%d'%(row, col))
            while col<N:
                board[row][col]=idx
                col += 1
                idx += 1
                if col==N or board[row][col]!=0:
                    col -=1
                    row +=1
                    break
                

        elif dir==2:
            # print('아래 채우기')
            while row<N:
                board[row][col]=idx
                row +=1
                idx +=1
                if row==N or board[row][col]!=0:
                    row -=1
                    col -=1
                    break

        elif dir==3:
            # print('왼쪽 채우기')
            while col>0:
                board[row][col]=idx
                col -= 1
                idx += 1
                if col==-1 or board[row][col]!=0:
                    col +=1
                    row -=1
                    break
        else:
            # print('위 채우기')
            while row>0:
                board[row][col]=idx
                row -=1
                idx +=1
                if row==-1 or board[row][col]!=0:
                    row +=1
                    col +=1
                    break
        
        
        # print(row, col, idx)
        fill(idx, (dir+1)%4)

    fill(1, 1)
    for b in board:
        for element in b:
            print(element, end=' ')
        print()