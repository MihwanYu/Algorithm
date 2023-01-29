
def solution():
    N = int(input())
    grid = [input() for _ in range(N)]
    if len(set(tuple(grid)))==1:
        if grid[0].count('0')==N:
            print(0)
        elif grid[0].count('1')==N:
            print(1)
        return

    string = dfs(grid)
    print(string)

def dfs(grid):
    if len(set(tuple(grid)))==1:
        if grid[0].count('0')==len(grid):
            return "0"
        elif grid[0].count('1')==len(grid):
            return "1"

    string = "("
    for i in range(0,len(grid),len(grid)//2):
        half = grid[i:i+len(grid)//2]
        for j in range(0,len(grid),len(grid)//2):
            quarter = [h[j:j+len(grid)//2] for h in half]
            # print(quarter)
            string += dfs(quarter)
    string += ")"     
    return string


if __name__=="__main__":
    solution()