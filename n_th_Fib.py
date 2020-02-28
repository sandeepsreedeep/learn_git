import time

################################################################################
#						NAIVE RECURSION
################################################################################

str_time = time.time()
def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)


print(fib(20))
print(f'{time.time()-str_time}')

##############################################################################
#						MEMOIZE RECURSION
#############################################################################


str_time = time.time()
def mem_fib(n, memoize = {1:0,2:1}):
	if n in memoize:
		return memoize[n]
	else:
		memoize[n] = mem_fib(n-1,memoize) + mem_fib(n-2,memoize)
		return memoize[n]

print(mem_fib(20))

print(f'{time.time()-str_time}')

############################################################################
#						ITERATIVE METHOD
############################################################################

str_time = time.time()
def it_fib(n, memoize = {1:0,2:1}):
	a = 0
	b = 1
	sums = 0
	if n == 1:
		return a
	else:
		for i in range(2,n):
			sums = a+b
			a = b
			b = sums
	return sums

print(it_fib(20))

print(f'{time.time()-str_time}')