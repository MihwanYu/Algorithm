
def solution():
    X = int(input())
    sticks=[64]
    while sum(sticks) != X:
        shortStick = sticks.pop(-1)
        dividen = [shortStick//2]*2
        if sum(sticks)+dividen[0]>=X:
            dividen = dividen[:1]
        sticks += dividen
        # print('sticks: ',sticks)
    print(len(sticks))
if __name__=="__main__":
    solution()
        