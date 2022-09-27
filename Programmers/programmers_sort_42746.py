# solution: https://school.programmers.co.kr/questions/24627

# ** 다시 풀어야 할 문제**
from itertools import permutations

def solution(numbers):
    answer = 0
    cases = list(permutations(numbers, len(numbers)))
    firstN = max([int(str(num)[0]) for num in numbers])
    # print('firstN: ',firstN)
    for case in cases:
        if str(case[0])[0]==str(firstN)[0]:
            # print('cases: ',case)
            num = ''.join([str(num) for num in case])
            if answer<int(num): answer = int(num)
    return str(answer)

def solutionFailed(numbers):
    #중도실패
    answer = ''
    #[9, 8, 96]-> 9 96 8
    #[9, 8, 96, 967]-> 9 96 967 8
    #[9, 8, 96, 969]-> "9 969 96 8" vs 9 96 969 8
    #[3, 30, 34, 5, 9]-> 9 5 34 3 30
    
    # 자릿수 대로 정렬 -> [9, 8] [96] [967] -> 9 96 967 8
    #                   [9, 8], [96], [969] -> 9 96 969 8
    byDigits = {'ones':[], 'tens':[], 'thous':[]}
    for n in numbers:
        if n//100>0:
            byDigits['thous'].append(n)
        elif n//10>0:
            byDigits['tens'].append(n)
        else:
            byDigits['ones'].append(n)
            
    for key in ['ones', 'tens', 'thous']:
        byDigits[key].sort()
        byDigits[key].reverse()
    
    maxIdx = max([len(byDigits[key]) for key in list(byDigits.keys())])
    idx = 0
    while idx<=maxIdx:
        print('---idx: %d---'%idx)
        for key in ['ones', 'tens', 'thous']:
            print('key array: ',byDigits[key])
            if len(byDigits[key])-1>=idx:
                answer += str(byDigits[key][idx])
        
        idx += 1
    
        
    print(byDigits)
    print('answer:',answer)
    return answer