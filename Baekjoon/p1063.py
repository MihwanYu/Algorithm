
def solution():
    K, S, N = list(input().split())
    Kr = int(K[1])
    Kc = ord(K[0])-64

    Sr = int(S[1])
    Sc = ord(S[0])-64

    N = int(N)

    for _ in range(N):
        dr, dc = 0,0
        d = input()
        if d=="R": dc = 1
        elif d=="L": dc = -1
        elif d=="B": dr = -1
        elif d=="T": dr = 1
        elif d=="RT": dr,dc = 1,1
        elif d=="LT": dr,dc = 1,-1
        elif d=="RB": dr,dc = -1,1
        elif d=="LB": dr,dc = -1,-1
        # print("K: (%d, %d)"%(Kr, Kc))
        
        #K가 범위 안에 있을 때
        if Kr+dr>=1 and Kr+dr<=8 and Kc+dc>=1 and Kc+dc<=8:
            #K를 움직였을 때 돌도 움직여야 할 때
            # print("S: (%d, %d)"%(Sr, Sc))
            if Kr+dr==Sr and Kc+dc==Sc:
                # print('K==s')
                #움직인 돌 범위 확인
                if Sr+dr>=1 and Sr+dr<=8 and Sc+dc>=1 and Sc+dc<=8:
                    Kr += dr
                    Kc += dc
                    Sr += dr
                    Sc += dc
                    # print('움직임완료')
            #돌 움직x, K만 움직
            else:
                Kr += dr
                Kc += dc
    print(chr(Kc+64)+str(Kr))
    print(chr(Sc+64)+str(Sr))


        


if __name__=="__main__":
    solution()