def solution(array, commands):
    answer = []
    for command in commands:
        # tempArr = array.copy()
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1]) 
    
    return answer