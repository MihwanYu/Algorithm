def solve():
    caseN = int(input()) #num of test cases
    #각 테스트 케이스는 8개의 줄로 구성
    #각 테스트 케이스에서 -> 8개의 룩이 있는가? AND 같은 열or 같은 행에 존재하지 않는가?
    cases=[]
    for i in range(caseN):
        case=[]
        for line in range(8):
            lineIn = input().split()
            case+=(lineIn)
        cases.append(case)
    
    for i,c in enumerate(cases):
        print("case %d: "%i, c)

    for c in cases:
        #한줄당 O가 1개씩인지확인
        cols=[]
        for i, line in enumerate(c):
            if line.count('O') == 1 and line.index('O') not in cols:
                cols.append(line.index('O'))
            else:
                print('no')
                break
        if len(cols)==8:
            print('yes')

def solveswea():
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        # ///////////////////////////////////////////////////////////////////////////////////
        case=[]
        for line in range(8):
            lineIn = input()
            case.append(lineIn)
        cols=[]
        # print('case: ',case)
        for i, line in enumerate(case):
            if line.count('O') == 1 and i not in cols:
                cols.append(i)
            else:
                print('#%d no'%test_case)
                break
        if len(cols)==8:
            print('#%d yes'%test_case)

solveswea()
