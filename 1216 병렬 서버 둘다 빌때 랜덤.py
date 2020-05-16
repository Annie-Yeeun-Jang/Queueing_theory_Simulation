# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:39:02 2019

@author: User
"""
#일단 잘못된게 wait time이 마이너스가 나옴  #응 사소한 오타야 ㅋㅋㅋㅋㅋ
#M/M/2 queue

import numpy as np

# Interval Time , Service time 변수

lamb= 5  #단위시간당 평균 도착 수, 단위 시간 = 1시간
mu_1 = 3
mu_2 = 4  #단위 시간당 몇명 처리하는지 rate

wait=0  #대기시간
Wait_time=[]  #대기시간 담은 리스트 (나중에 평균내려고)

arrival=[]   #도착시간
arr2=[]

#arr1=[]
#arr2=[]
#service_start=[]   #서비스 시작시간
start1 = []  #mm2에서는 이게 서버별로 서버 시작시간
start2 = []

finish1 =[]  #서버 1로 간 고객들이 끝나는 시간
finish2 =[]  #서버 2로 간 고객들이 ~~

count1=0    #각 서버에 몇명 있는지
count2=0

for i in range(10000):   #고객 몇명인지는 i가 알려줌. 현재 i+1번째 고객.
    
    
    #제일 처음 고객 인덱스가 0.
    #IAT=Inter Arrival time, ST= service duration time
    IAT = np.random.exponential(1/lamb)   
    ServiceTime_1 = np.random.exponential(1/mu_1)  #1번 서버가 이번에 얾마나 걸릴지
    ServiceTime_2 = np.random.exponential(1/mu_2)
    #이거 역수 맞는지 확인 꼭!!!!!!!!!!!!!!!!!

    
    #도착시각 (처음 고객일때랑 아닐때랑 다름)   #여기 인덱스 잘 이루어지고 있는지 꼭 확인!!!!
    
    #arrival까지는 mm1이랑 다를게 없음
    if i == 0:
        arrival.append(IAT)
                
    else:
        arrival.append(arrival[i-1]+IAT)
        
    #서버 배정  
      #finish2가 처음에 아무것도 없네
    if i == 0:
        server=np.random.randint(1,3)
        count1+=1   #서버1에 몇명있는지
        arr=IAT
        s1=IAT  #s1은 1번 서버로 배정됐을 때 현재 고객의 서비스 시작 시간 #서비스 바로 시작
        start1.append(s1)   #처음 온 고객은 바로 시작하니까
        finish1.append(s1+ServiceTime_1)
    
    elif arrival[i] >= max(f1,f2) or f1==f2:
        server=np.random.randint(1,3)
        if server==1:
            count1+=1  #서버 안에 몇명갔는지 세기 (나중에 인덱싱 돕기 위해... max나 -1인덱싱 해도 되겠지만)
            arr=arrival[-1]  #현재 이 고객의 도착타임
            #arr1.append(arr)
            s1=max(arr,f1)  
            #arrival은 전체 수 또 세어주기 귀찮아서 맨뒤 고객 (arrival 맨뒤가 지금 고객 도착타임)
            start1.append(s1)
            finish1.append(s1+ServiceTime_1)
            
            #진행과정 수행 완료. 이제 wait time만 계산하면됨 
            wait=s1-arr
        else:
            count2+=1
            arr=arrival[-1]
            arr2.append(arr)
            s2=max(arr,f2) #-1맞는지 확인    #인덱싱 복잡하고 귀찮아서 임시 변수 쓴것
            start2.append(s2)
            finish2.append(s2+ServiceTime_2)
            wait=s2-arr
        
    elif f1 < f2 and arrival[i] <= max(f1,f2):  #첫 고객이 아닌데 1번서버가 더 빨리끝나면  => 그럴려면 직전고객들 비교
        server=1
        count1+=1  #서버 안에 몇명갔는지 세기 (나중에 인덱싱 돕기 위해... max나 -1인덱싱 해도 되겠지만)
        arr=arrival[-1]  #현재 이 고객의 도착타임
        #arr1.append(arr)
        s1=max(arr,f1)  
        #arrival은 전체 수 또 세어주기 귀찮아서 맨뒤 고객 (arrival 맨뒤가 지금 고객 도착타임)
        start1.append(s1)
        finish1.append(s1+ServiceTime_1)
        
        #진행과정 수행 완료. 이제 wait time만 계산하면됨 
        wait=s1-arr
        
        
    elif f1 > f2 and arrival[i] <= max(f1,f2):  #첫 고객이 아닌데 2번서버가 더 빨리끝나면
        server=2  #2번 서버
        count2+=1
        arr=arrival[-1]
        arr2.append(arr)
        s2=max(arr,f2) #-1맞는지 확인    #인덱싱 복잡하고 귀찮아서 임시 변수 쓴것
        start2.append(s2)
        finish2.append(s2+ServiceTime_2)
        wait=s2-arr
        
        
        
    Wait_time.append(wait)
    server=0 #서버 초기화, 오류 나는지 체크하려고
    
    #다음 반복 시 finish time 비교 위해서
    if finish1:  #1번서버에서 끝나는 시간   #finish[i] 해도 될듯
        f1=finish1[-1] 
    else: f1=0
    
    if finish2:    #2번 서버에서 끝나는 시간   #2번 서버에 아직 아무도 안갔으면 f2=0
        f2=finish2[-1]
    else:
        f2=0

#리스트 내 최댓값은 np.max(arrival)
         
print('평균 대기 시간:   ', np.mean(Wait_time))
#1만번 돌리니까 0.08시간정도..


#체크리스트
#서버 배정할때 첫번째 들어가는 애 따로 if문 만들어줘야 하는지 => 해야할듯
# ===> 서버지정 if else문을 따로 뺴고 server = 1 이런식으로만 한다음에
#그 밑에다가 if server ==1 , if server==2 이렇게 할까봐 
#finish time 합친것이 필요한가??? 서버별로 따로따로 해도 되나.. 몇번쨰 손님인지 모르니까..


####max() 부분 인덱싱 -1 맞는지 확인!!!!

import pandas as pd
#dictt={'start1':start1,'finish1':finish1, 'start2':start2, 'finish2':finish2}
#df=pd.DataFrame(dictt)





