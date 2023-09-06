T = int(input()) 
for i in range(T):
    i = input().split(' ')
    x, y = int(i[0]), int(i[1])
    if 0 <= x < y < 2**31:
        d = y-x   # 거리 계산
        #print(f"distance : {d}")
        temp, temp_sum = 0, 0
        m = 0
        for l in range(1, d+1):
            temp = 2*l
            temp_sum = temp_sum+temp
            #print(f"temp : {temp}, temp_sum : {temp_sum}")
            if temp_sum >= d:
                if d <= temp_sum-l:
                    m = 2*l-1
                else:
                    m = 2*l
                break
        #print(f"작동 횟수 : {m}")
    print(m)