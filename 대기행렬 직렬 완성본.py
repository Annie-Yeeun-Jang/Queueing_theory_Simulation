# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:08:11 2019

@author: User
"""

#M/M/2 직렬

import numpy as np
# Interval Time , Service time 변수

lamb= 5  #1시간당 평균 도착 수, 단위 시간 = 1시간
mu_1 = 8  #1시간당 처리하는 사람 수 (service time rate)
mu_2 = 6   #람다보다 커야됨....그래야 대기시간이 안길어짐

wait=0  #대기시간
Wait_time1=[]  #대기시간 담은 리스트 (나중에 평균내려고)

arrival1=[]   #처음에 도착시간
service_start=[]   #서비스 시작시간
finish1 =[]  #끝나는 시간

cumtime1=0
cumtime2=0
cumtimelist1=[]
cumtimelist2=[]


for i in range(100000):
    #제일 처음 고객 인덱스가 0.
    #IAT=Inter Arrival time, ST= service duration time
    IAT = np.random.exponential(1/lamb)   
    ServiceTime_1 = np.random.exponential(1/mu_1)  #1번 서버가 이번에 얾마나 걸릴지
   
    
    if i == 0:
        arrival1.append(IAT)        #첫고객이니까 
        service_start.append(IAT)   #서비스 바로시작               #여기 두줄만 이후 고객이랑 다름
        finish1.append(service_start[i]+ServiceTime_1)
        
    else:
        arrival1.append(arrival1[i-1]+IAT)  #이전사람 arrival time + inter arrival time
        service_start.append(max(arrival1[i],finish1[i-1])) #앞에사람 끝나는시간 vs 현재고객 도착시간
        finish1.append(service_start[i]+ServiceTime_1)
        
        
    #진행과정 수행 완료. 이제 wait time만 계산하면됨    
    wait=service_start[i]-arrival1[i]
    Wait_time1.append(wait)   #서버 1 에서의 대기시간
    #cumtime1+=wait/(i+1)
    #cumtimelist1.append(cumtime1)

#서버 2
Wait_time2=[]         #서버2에서의 대기시간
arrival2=finish1      #서버1의 finish time이 서버2의 arrival time임
#서버1과 다른점은 arrival이 하나씩 생성되지 않고 리스트에 이미 다 들어있다는점
service_start2=[]
finish2=[]

#여기서는 for문 들어가고 나서 초기설정 안해줘도 되는거 맞냐
#ㄴㄴ 똑같이 짜야됨. append만 빼고.

for i in range(100000): 
    ServiceTime_2 = np.random.exponential(1/mu_2)
    
    if i==0:
        service_start2.append(arrival2[i])   #첫 고객은 바로 서비스 받으니까
        finish2.append(service_start2[i]+ServiceTime_2)
    
    else:
        service_start2.append(max(arrival2[i],finish2[i-1]))   
        finish2.append(service_start2[i]+ServiceTime_2)
        
    wait2=service_start2[i]-arrival2[i]
    Wait_time2.append(wait2) 
    #cumtime2+=wait2/(i+1)
    #cumtimelist2.append(cumtime2)



def vector_add(v,w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]
def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]
            
total_dur=vector_subtract(finish2,arrival1)
print('서버 1 평균 대기 시간:   ', np.mean(Wait_time1))   #평균 0.2 (12분)    #단위 다 시간. 
print('서버 2 평균 대기 시간:   ', np.mean(Wait_time2))   #평균 0.8 (48분)
print('개인별 평균 총 대기시간:  ',np.mean(vector_add(Wait_time1,Wait_time2)))  #평균 1시간
print('개인별 총 소요시간:   ',np.mean(total_dur))    #평균 1.3


