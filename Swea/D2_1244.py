
T = int(input())

for test_case in range(1, T+1):
    numbers, maxN = input().split()
    maxN = int(maxN)
    currentN = 0
    possibleMax = ''.join(sorted(list(numbers))[::-1])
    # print('possibleMax: ',possibleMax)
    numbers = list(map(int, list(numbers)))

    s=''

    # print(numbers)

    def exchange(count, numbers):
        global maxN, s, currentN, possibleMax
        if count == maxN:
            s+=''.join(map(str,numbers))
            if currentN<int(s): currentN=int(s)
            # print('s=', s)
            s=''
            return

        idxes = [i for i, v in enumerate(numbers) if v == max(numbers)][::-1]
        if 0 in idxes: idxes.remove(0)
        if len(idxes)==0:
            s+=str(numbers[0])
            # print('s=%s, count=%d, numbers=' % (s, count), numbers)
            if len(numbers)==1:
                #서로 다른 애들로만 존재하는데 exchange 수가 홀수(결국 완벽히 작은 숫자를 결과로 못낼 때)
                # print('s set: ',len(set(s)),', s: ',len(s))
                # print(len(set(s.split()))==len(s))
                # print(True and True)
                if len(set(s))==len(s) and (maxN-count)%2==1:
                    # print('작은거끼리 교환')
                    #가장 작은 값 끼리 교환해서 리턴
                    # sLast = possibleMax[-1]
                    # possibleMax[-1] = possibleMax[-2]
                    # possibleMax[-1] = sLast
                    # >>>>TypeError: 'str' object does not support item assignment
                    possibleMax = possibleMax[:-2]+possibleMax[-2:][::-1]

                # 똑같은거 2개이상일경우
                # 서로 다른 애들로만 존재하지만 exchange 가능 수가 짝수일 경우 그대로 최댓값 리턴
                currentN = int(possibleMax)
                s=''
                return
            else:
                exchange(count, numbers[1:])
        else:

            for idx in idxes:
                numbersCopy=numbers.copy()
                firstN = numbersCopy[0]
                numbersCopy[0] = numbersCopy[idx]
                numbersCopy[idx] = firstN
                # print('numbers: ', numbersCopy)
                s+= str(numbersCopy[0])
                # print('s=%s, count=%d, numbers='%(s,count), numbersCopy)
                exchange(count+1, numbersCopy[1:])

    count=0

    exchange(0, numbers.copy())
    print('#%d %d'%(test_case, currentN))