def pibo(n):
    print('피보나치 함수 실행')
    if n<=0: return 1
    if n==1: return 1
    return pibo(n-1) + pibo(n-2)

def fun2(n):
    result = 0
    while n>0:
        print('반복')
        n = n//2
        result += 1
    print(result)

print('--------------------number: 1-------------------')
ans = fun2(1)
print(ans)

print('--------------------number: 2-------------------')
ans = fun2(2)
print(ans)

print('--------------------number: 3-------------------')
ans = fun2(3)
print(ans)

print('--------------------number: 4-------------------')
ans = fun2(4)
print(ans)


#피보나치 수열: 1 1 3 5 8 13 21....
for i in range(100):
    print('--------------------number: %d-------------------'%(i+1))
    fun2(i+1)