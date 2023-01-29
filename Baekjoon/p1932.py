# 제일 아래층부터 위층으로 올라가면서
# arr[i][j]와 arr[i][j+1] 둘 중에 큰 값을
# arr[i-1][j]에 누적시키는 것을 반복하면 제일 꼭대기층 arr[0][0]이 정답이 된다.
# 역순 접근방식이라는걸 떠올리기가 어려웠음

def solution():
    N = int(input())
    layers = [ list(map(int, input().split())) for _ in range(N) ]
    
    for i in range(N-1, 0, -1):
        #i: 몇번째 layer인지
        for j in range(len(layers[i])-1):
            if layers[i][j]>layers[i][j+1]:
                layers[i-1][j] += layers[i][j]
            else:
                layers[i-1][j] += layers[i][j+1]
    print(layers[0][0])
    

if __name__=="__main__":
    solution()
