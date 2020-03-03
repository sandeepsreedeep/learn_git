import time


strt_time = time.time()

n = 10000000
sums = 0
for i in range(1,n):
	if i%3 == 0 or i%5 == 0:
		sums += i
print(sums)
print(f'time: {time.time()-strt_time}')
strt_time = time.time()

def func_s(num):
	for i in range(1,n):
		if i%3 == 0 or i%5 == 0:
			yield i

print(sum(func_s(n)))
print(f'time: {time.time()-strt_time}')

def sums_func(n,mult):
    num = n//mult
    return(mult*num*(num+1)/2)

strt_time = time.time()
print(int(sums_func(n-1,3)+sums_func(n-1,5)-sums_func(n-1,15)))
print(f'time: {time.time()-strt_time}')