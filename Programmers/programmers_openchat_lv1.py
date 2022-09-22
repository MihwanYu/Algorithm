def solution(record):
    answer = []
    name_dic = {}
    for r in record:
        r_li = r.split()
        if(r_li[0]=='Enter'):
            name_dic[r_li[1]]=r_li[2]
            answer.append("%s님이 들어왔습니다."%(r_li[2]))
        elif(r_li[0]=='Leave'): answer.append("%s님이 나갔습니다."%(name_dic[r_li[1]]))
        else:
            name_dic[r_li[1]]=r_li[2]
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
ans = solution(record)
print(ans)