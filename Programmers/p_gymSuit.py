# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 18:08:56 2021

@author: sally
"""

#programmers
#https://programmers.co.kr/learn/courses/30/lessons/42862

#전체 학생수 n에 대해서, 2<=n<=30, 중복번호 없음
#lost: 체육복을 도난당한 학생 번호 리스트
#reverse: 여벌의 체육복 가져온 학생 번호 리스트
# return: 체육수업 들을수있는 최대 학생 수

#조건1)학생은 바로앞 or 바로뒤 번호 학생에게만 체육복 빌려줄수있다
#조건2)여벌 체육복 가져온 학생이 도난당하면->다른학생에게 빌려줄수없음

#lost,reverse의 숫자는 학생 번호임(1부터시작)
#test case1) n=5, lost=[2,4], reverse=[1,3,5], output=5
#test case3) n=3, lost=[3],reverse=[1], output=2



def solution(n, lost, reserve):
    #출석가능 학생 번호-도난당한 사람 빼고
    lost.sort()
    reserve.sort()
    attend = [i for i in range(1,n+1) if i not in lost]
    #빠짐없이 모두 도난 x일때
    if len(lost)==0:
        return n
    
    #여벌 있는 사람이 도난당할때
    for i in lost:
        if i in reserve:
            attend.append(i)
            reserve.remove(i)
    lost=[i for i in lost if i not in attend]
            
    #도난당한사람 중 체육복 빌리면 attend에 추가
    for i in lost:
        if i-1 in reserve: #앞사람이 여벌 있을때
            print(i, i-1)
            attend.append(i)
            reserve.remove(i-1)
        elif i+1 in reserve: #뒷사람이 여벌 있을때
            print(i, i+1)
            attend.append(i)
            reserve.remove(i+1)
    answer = len(attend)
    return answer
        
#첫 풀이-테스트 12,13에서 틀림
solution(8,[1,4,6],[7])
#test 13: lost, reserve 중 배열이 오름차순이 아닐 경우
#test 12: solution(3,[1,2],[2,3])
#여벌 있는데 도난당할때, 자기한테 먼저 줘야함-if문이 for문 루프에 들어가면 안됐다

#12,13맞추니까 1,6,7에서 실패....
#solution(8, [1, 2, 4, 6], [1, 2, 4, 6])->6나옴,,