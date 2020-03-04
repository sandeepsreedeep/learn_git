from itertools import chain
col_arr =[]
def collatz(num):
	if num == 1:
		return 1
	else:
		if num%2 == 0:
			new_num = num/2
			col_arr.append(int(new_num))
			return collatz(new_num)
		else:
			new_num = 3*num + 1
			col_arr.append(int(new_num))
			return collatz(new_num)


collatz(int(input("Enter the number")))
print((col_arr))
