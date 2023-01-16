from sys import stdin
input = stdin.readline

def solution():
    N, M, V = map(int, input().split())
    points = {}
    for _ in range(M):
        p1, p2 = map(int, input().split())
        if points.get(p1)==None:
            points[p1] = [p2]
        else:
            points[p1].append(p2)

        if points.get(p2)==None:
            points[p2] = [p1]
        else:
            points[p2].append(p1)
    
    #반례: start point에 연결된 점이 하나도 없을 때 + dfs, bfs 각각 출력해야되니까 v 2번 출력해야함
    if not points.get(V):
        print(V)
        print(V)
        return

    for key in points.keys():
        points[key].sort()

    # for key in points.keys():
    #     print('key: %d, values: '%key, points[key])

    ret1 = dfs(points, [V], V, N)
    # print(ret1)
    print(' '.join([str(v) for v in ret1]))

    ret2 = bfs(points, [V], V, N)
    print(' '.join([str(v) for v in ret2]))

def bfs(points, visited, V, N):
    if len(visited)==N:
        return visited
    
    ret = [V]
    count = 0
    while visited:
        # print(visited)
        current = visited.pop(0)
        for v in points[current]:
            if v not in ret:
                visited.append(v)
                ret.append(v)
        # print(ret)
    return ret


def dfs(points, visited, V, N):
    if len(visited)==N:
        # print(visited)
        return visited
    
    visited #[1] -> [1,2]
    for v in points[V]: #(2, 3)  (1,4)
        if v not in visited:
            visited = dfs(points, visited+[v], v, N) #visited = [1,2,4], v=2

    return visited
    

if __name__=="__main__":
    solution()