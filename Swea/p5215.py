

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 제한 칼로리 이내에 가장 높은 점수
for test_case in range(1, T + 1):
    print("#%d "%test_case, end='')
    ingreN, maxCal = [int(i) for i in input().split()]
    ingreDict = {'scores':[], 'calories':[]}
    currentScore = 0
    currentCal = 0

    for i in range(ingreN):
        score, cal = [int(k) for k in input().split()]
        ingreDict['scores'] .append(score) 
        ingreDict['calories'] .append(cal)
            #재료 idx, 현재 쌓인 score, 현재 쌓인 칼로리
    def addIngre(idx, score, calories):
        global currentCal, currentScore
        #방금 들어온 재료를 킵고일 할지 여부
        print('currentCal: %d'%currentCal)
        
        if(calories > maxCal): return
        else:
            if score >currentScore:
                currentCal = calories 
                currentScore = score 
        if idx==ingreN: return

        addIngre(idx+1, score+ ingreDict['scores'][idx], calories+ ingreDict['calories'][idx])
        addIngre(idx+1, score, calories)
    
    addIngre(0,0,0)
    print(currentScore)


'''

# 높은 점수 순
def dfs(ingreN, ingreDict):
    global currentScore, maxCal, currentCal
    if len(ingreDict['calories'])==0: return
    highScore = max(ingreDict['scores'])
    scoreIdx = ingreDict['scores'].index(highScore)
    cal = ingreDict['calories'][scoreIdx]
    # print('currentScore: %d, highScore: %d, currentCal: %d, cal: %d'%(currentScore, highScore, currentCal, cal))
    #현재 칼로리 + 가장 점수가 높은 score의 칼로리 > maxCal
    if currentCal+cal>maxCal: return
    else:
        currentScore += highScore
        currentCal += cal
        ingreDict['scores'].remove(highScore)
        ingreDict['calories'].remove(cal)
        # 가장 큰 스코어 + currentScore -> currentScore
        # currentScore를 ingredient 리스트에서 삭제
        # currentScore의 calories도 삭제
        dfs(ingreN-1, ingreDict)

#낮은 칼로리 순
def dfs_lowerCal(ingreN, ingreDict):
    global currentScore, maxCal, currentCal
    if len(ingreDict['calories'])==0: return
    lowCalorie = min(ingreDict['calories'])
    # highScore = max(ingreDict['scores'])
    scoreIdx = ingreDict['calories'].index(lowCalorie)
    score = ingreDict['scores'][scoreIdx]
    # print('currentScore: %d, lowCalorie: %d, currentCal: %d, score: %d'%(currentScore, lowCalorie, currentCal, score))
    #현재 칼로리 + 가장 낮은 칼로리 > maxCal
    if currentCal+lowCalorie>maxCal: return
    else:
        currentScore += score
        currentCal += lowCalorie
        ingreDict['scores'].remove(score)
        ingreDict['calories'].remove(lowCalorie)
        # 가장 낮은 칼로리의 스코어 + currentScore -> currentScore
        # 재료 칼로리와 score를 ingredient 에서 삭제
        dfs_lowerCal(ingreN-1, ingreDict)
            
'''