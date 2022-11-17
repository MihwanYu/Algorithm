T = int(input())
for test_case in range(1, T + 1):
    prices = map(int, input().split())
    #최대 이익 출력
    idx = 0

    def buy(day, consumed, earned):
        print(prices[day])

    buy(0,0,0)