import math
# fin = open("primes.txt","r")
# primes = [int(i) for i in fin.readlines()]
primes = [2]
current = primes[-1]

def isPrime(n):
	global current
	global primes
	for i in range(current+1, n+1):
		p = True
		for j in primes:
			if (j > math.sqrt(n)):
				break
			if (i%j==0):
				p = False
				break
		if p:
			primes.append(i)
	current = n
	return (n in primes)

def factor(n):
	global primes
	p = {}
	if n==1:
		p[1]=1
		return p
	isPrime(n)
	for i in primes:
		if (i > math.sqrt(n) or n==1):
			break
		while (n%i==0):
			if (i in p.keys()):
				p[i] += 1
			else:
				p[i] = 1
			n /= i
	return p

def find():
	c = 0
	f = 0
	for i in range(100, 1001):
		x = factor(i)
		if (2 in x.keys()):
			prod = 1
			for j in x.keys():
				if j==2:
					continue
				prod *= (x[j]+1)
			prod2 = 1
			for j in x.keys():
				if j==2:
					prod2 *= x[j]
					continue
				prod2 *= (x[j]+1)
			if (prod2 == prod):
				c += 1
			else:
				f += 1
		else:
			f += 1
	print(c) 

find()

# fout = open("primes.txt","w")
# for i in primes:
# 	fout.write(str(i)+"\n")
# fout.close()