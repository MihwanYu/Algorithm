
#runtime error 주구장창 뜨더니만 test case number T 쓸 필요 없는 거였음
# https://swexpertacademy.com/main/talk/solvingTalk/boardCommuView.do?searchCondition=COMMU_DETAIL-COMMU_TITLE-NICK_NAME_TAG&commuId=AYKGSXs66kMDFASv&searchKeyword=%EB%9F%B0%ED%83%80%EC%9E%84&orderBy=RECOMMEND_DESC&pageSize=30&pageIndex=1        
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    output=[]
    for n in range(1, N+1):
        clap=str(n).count('3')+str(n).count('6')+str(n).count('9')
        if clap:
            output.append('-'*clap)
        else:
            output.append(n)

    for o in output:
        print(o, end=' ')