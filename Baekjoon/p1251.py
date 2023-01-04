    #임의의 두 부분 골라 단어 쪼개기
    #각 파트를 앞뒤 뒤집어서 원래 순서대로 합치기
    #사전순으로 가장 앞에 있는 단어를 출력
def solution():
    word = input()
    alpha1 = sorted(list(word[:-2]))[0]
    
    #part1: 기존 단어에서 적어도 뒤 2개를 제외한 후 앞에서부터 만들 수 있는 단어 중 뒤집었을 때 알파벳 상 가장 빠른 단어
    part1 = wordDivision(word[:-2], alpha1)
    
    word = word[len(part1):]
    alpha2 = sorted(list(word[:-1]))[0]

    #part2: 앞선 part1을 제외한 단어에서 적어도 뒤 1개를 제외한 후 앞에서부터 만들 수 있는 단어 중 뒤집었을 때 알파벳 상 가장 빠른 단어
    part2 = wordDivision(word[:-1], alpha2)

    #part3: part1과 part2가 제외되고 남은 부분
    part3 = word[len(part2):]
    print(part1+part2+part3[::-1])

def wordDivision(word, standW):
    numStandW = word.count(standW)
    if numStandW==1:
        part = word[:word.index(standW)+1]
        part = part[::-1]
    else:
        # 알파벳 중복 있을 경우
        # 중복 단어 앞까지 잘라낸 후 뒤집은 단어 리스트 만들어서
        # 그 중 가장 알파벳 상 앞선 것 선택
        wordlist = []
        wordCopy = word[:]
        newIdx = wordCopy.index(standW)
        for i in range(numStandW):
            preWord = word[:newIdx+1]
            wordlist.append(preWord[::-1])
            wordCopy = wordCopy[:newIdx]+wordCopy[newIdx+1:]
            newIdx = wordCopy.find(standW)+i+1
        
        part = sorted(wordlist)[0]
    return part

if __name__=="__main__":
    solution()