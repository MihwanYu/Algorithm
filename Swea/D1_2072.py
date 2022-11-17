
T = int(input())
for test_case in range(1, T + 1):
    # numbers = map(int, input().split()) 
    numbers = [int(i) for i in input().split() if int(i)%2==1]
    print("#%d %d"%(test_case, sum(numbers)))