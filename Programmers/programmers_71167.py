
#구름에선 그냥 넘겼는데 programmers에서 푸니까 테케 박살나버림 ..
def solution(K, words):
    answer = 1
    idx = 0
    row = ''
    while idx<len(words):
        w = words[idx]
        if len(row)==0:
            row += w
        elif len(row)+1+len(w)<=K: #K를 10이라고 넣었던게문제
            row = row+'_'+w
        else:
            # print(row)
            row=w
            answer +=1
        idx +=1
    # print(row)
		
	
    return answer



def solution2(K, words):
    # 여기에 코드를 작성해주세요.
    answer = 1
    currentLine = 0
    while words:
        #현재 줄에 단어가 없으면 하나 추가
        if currentLine == 0:
            # print(words[0], end=' ')
            currentLine = len(words.pop(0))
        
        #현재 줄에 하나 이상 단어가 있고 그 단어 뒤에 다음 단어 추가할 공간 있으면 단어 추가
        elif currentLine != 0 and currentLine + 1 + len(words[0])<=K: 
            # print(words[0], end=' ')
            additional = len(words.pop(0))
            currentLine = currentLine+1+additional #뒤에 단어 추가하기
        
            if currentLine==10: #단어 추가하고서 10자 딱맞으면 줄바꿈
                answer += 1
                currentLine = 0
                # print()
        else: #단어 추가 못하면 줄바꿈
            answer +=1
            currentLine = 0
            # print()
    
    
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
words = ["a", "b", "c", "drama", "elephant", "am", "tomato", "are", "keyboard", "a"]
words = ["a","a","a","a","a","a","a"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")