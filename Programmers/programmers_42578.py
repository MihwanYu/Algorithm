def solution(clothes):
    answer = 0
    #하루 최소 1개 의상
    closet = {}
    for cloth in clothes:
        if closet.get(cloth[1]) == None:
            closet[cloth[1]] = 1
        else:
            closet[cloth[1]] += 1
    
    combination=1
    for key in closet.keys():
        combination *= (closet[key]+1)
    
    return combination -1