# 9x9 스도쿠
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print("#%d "%test_case, end="")
    sdoku=[]
    result=True
    #입력 받으면서 row 마다 겹침유무 확인
    for _ in range(9):
        row = list(map(int, input().split()))
        if result==False: continue
        #중복일때 바로 break걸었다가 뒤 input 짤려버려서 틀렸었음 -> 이미 false인 sdoku여도 input9개 받도록 continue 설정
        if len(set(row)) != 9:
            result=False
        sdoku.append(row)

    if result==False:
        print(0)
        continue

    #col별 겹침유무 확인
    for c in range(9):
        col = [row[c] for row in sdoku]
        if len(set(col))!=9:
            result=False
            break
    if result==False:
        print(0)
        continue
    #grid별 겹침유무 확인
    for r in range(0,9,3):
        for c in range(0,9,3):
            grid = sdoku[r][c:c+3]+sdoku[r+1][c:c+3]+sdoku[r+2][c:c+3]
            if len(set(grid))!=9:
                result=False
                break
        if result==False:
            break
    if result==False:
        print(0)
    else:
        print(1)
        
