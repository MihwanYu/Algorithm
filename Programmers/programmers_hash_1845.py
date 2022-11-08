def solution(nums):
    #포켓몬 갯수: nums//2
    
    answer = 0
    poketmons = {}
    for monster in nums:
        if poketmons.get(monster):
            poketmons[monster] +=1
        else:
            poketmons[monster] = 1
    if len(poketmons.keys()) >= (len(nums)//2):
        answer = len(nums)//2
    else:
        answer = len(poketmons.keys())
    return answer