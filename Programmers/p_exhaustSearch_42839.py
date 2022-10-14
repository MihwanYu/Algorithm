def solution(numbers):
    numberCard = list(numbers)
    numberCard.sort()
    
    answer = 0
    numberComb = []
    
    def createList(numlist, digit):
        if digit==1: return [[num] for num in numlist]
        retLi=[]
        for num in numlist:
            tempLi = numlist.copy()
            tempLi.remove(num)
            retLi += [[num]+newLi for newLi in createList(tempLi, digit-1)]
        return retLi
    
    def isPrime(num):
        if num<2: return False
        opt = 2
        while opt<num:
            if num%opt==0: return False
            opt +=1 #완전 단순,,,무식..
        return True
    
    
    for digit in range(1,len(numbers)+1):
        numberComb += createList(numberCard, digit)
    numbers = set([int(''.join(num)) for num in numberComb])
    for num in numbers:
        if isPrime(num):
            answer +=1
    return answer