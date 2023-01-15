def solution(today, terms, privacies):
    answer = [] #파기해야 할 개인정보 번호
    firedate = []
    policies = {}
    for term in terms:
        terminfo = term.split()
        policies[terminfo[0]] = int(terminfo[1])
        
    for i,privacy in enumerate(privacies):
        privacyinfo = privacy.split()
        duration = policies[privacyinfo[1]]
        # print('%s + %s: '%(privacyinfo[0],  policies[privacyinfo[1]]))
        if addDate(privacyinfo[0], duration, today):
            # print(': fire(%d)'%(i+1))
            answer.append(i+1)
    
    return answer

def addDate(date, addmonth, today):
    #date에 addmonth 만큼 더한후 today와 비교 -> fire면 True리턴
    year, month, day = map(int, date.split('.'))
    month += addmonth
    if month>12:
        addyear = month//12
        year += addyear
        month = month%12
    # date + addmonth 된 날짜 = 파기 시작하는 날짜
    
    #12월이 0월로 되는 문제 해결
    #2022.11.20 + 13개월 -> 2023.12.20으로 만들기 위해 필요
    if month == 0:
        year -=1
        month = 12
    tyear, tmonth, tday = map(int, today.split('.'))
    if tyear>year: return True
    elif tyear<year: return False
    elif tmonth>month: return True
    elif tmonth<month: return False
    elif tday>=day: return True
    else: return False
    #날짜가 같으면 파기해야 하는거
    
