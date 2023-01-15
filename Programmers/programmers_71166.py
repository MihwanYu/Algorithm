# 다음과 같이 import를 사용할 수 있습니다.
import sys
# import itertools

def solution(arr, K):
    # 여기에 코드를 작성해주세요.
    #arr중 K개 뽑아서 그중 가장큰 - 가장작 값이 최소
    # nCk했을 때 그 리스트 max() - min()
    answer = sys.maxsize
    arr.sort()
    for i in range(len(arr)-K+1):
        partial = arr[i:i+K]
        if answer>max(partial)-min(partial):
            answer = max(partial)-min(partial)
    '''
    itertools 웬만하면 시간초과되니까 사용x
    arrays = itertools.combinations(arr,K)
    for array in arrays:
        # print(array)
        if answer>max(array)-min(array):
            answer = max(array)-min(array)
    '''
    
    
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")