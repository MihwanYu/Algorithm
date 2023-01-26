
def find_parents(u, parents):
    if u==parents[u]:
        return u
    u = find_parents(parents[u], parents)
    return u

def merge(u,v, parents):
    p1 = find_parents(u, parents)
    p2 = find_parents(v, parents)
    if p1<p2:
        parents[p2] = p1
        #p2를 parent로 가지는 모든 애들을 p1으로 변경
        for i in range(len(parents)):
            if parents[i]==p2:
                parents[i] = p1
    else:
        parents[p1] = p2
        for i in range(len(parents)):
            if parents[i]==p1:
                parents[i] = p2

def solution():
    C = int(input())# #of computers
    N = int(input())# #of pairs
    parents = [i for i in range(C+1)]

    #1번 컴퓨터 바이러스 -> 연결된 모든 노드
    for _ in range(N):
        u,v = map(int, input().split())
        merge(u,v, parents)
    
    print(parents.count(1)-1)



if __name__=="__main__":
    solution()