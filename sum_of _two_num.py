import time


breaker = False
l = range(1,100)
start_time = time.time()
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (l[i] + l[j]) == 10:
            print(l[i] , l[j])
            breaker = True
    if breaker:
        break
            
print("Time taken is : " + str(time.time()- start_time))

start_time = time.time()
temp = l
for i,each in enumerate(temp):
    if (10-each) in temp:
        print(each, 10-each)
        break
    elif i+1 == len(l):
        print("There are no such numbers in the list")


print("Time taken is : " + str(time.time()- start_time))

temp = sorted(l)
start_time = time.time()
i,j = 0,-1
while i<=len(l)/2:
    if l[i]+l[j]==10:
        print(l[i],l[j])
        break
    elif l[i]+l[j]<10:
        i += 1
    elif l[i]+l[j]>10:
        j -= 1
        
print("Time taken is : " + str(time.time()- start_time))        
