
def solution():
    expression = input()
    #+만 있는 경우
    # if '-' not in expression:
    #     e = list(map(int, expression.split('+')))
    #     ans = sum(e)
    #     print(ans)
    #     return
    
    # '-' 뒤에 오는 식을 전부 뺄셈 처리하면 식의 값이 최소가 된다.
    expression = expression.split('-')
    partialsum = []
    for exp in expression:
        part = map(int, exp.split('+'))
        partialsum.append( sum(part) )
    ans = partialsum[0]-sum(partialsum[1:])
    print(ans)


if __name__=="__main__":
    solution()