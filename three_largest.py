import time
arr = [141,1,17,-7,-17,-27,18,541,8,7,7]

strt_time = time.time()
largest = arr[0]
sec_larg = arr[1]
third_largest = arr[2]
for each in arr:
	if each>largest:
		largest = each
	if third_largest < each < largest:
		sec_larg = each
	if third_largest < each < sec_larg:
		third_largest = each

print(sec_larg)

strt_time = time.time()
print(sorted(arr)[-1:-4:-1])
print(f'time: {time.time()-strt_time}')
