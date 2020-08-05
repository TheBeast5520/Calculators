import math
ans=0
phi = ( 1 + math.sqrt(5) ) / 2
def gcd(a, b):
	a = conv(a)
	b = conv(b)
	while (a != 0 and b != 0): 
		if (b>a): 
			(a,b)=(b,a)
		a %= b
	return str(b)

def conv(s):
	s=str(s)
	if (len(s)>=2 and s[-2::]==".0"):
		s=float(s)
		s=int(s)
	else:
		s=int(s)
	return s

def lcm(a, b):
	a=conv(a)
	b=conv(b)
	return str((a*b)/float(gcd(a,b)))

def num(s):
	base=True
	for i in s:
		if not (i.isnumeric() or i=='.'):
			base=False
			break
	return base

def split(s):
	ret = []
	counter = 0
	last=0
	for i in range(len(s)):
		if (s[i]=='('):
			counter += 1
		elif (s[i]==')'):
			counter -= 1
		if (counter == 0 and s[i]==','): 
			ret.append(s[last:i])
			last=i+1
	ret.append(s[last::])
	return ret

def fact(s):
	s=conv(s)
	prod=1
	for i in range(1,s+1):
		prod *= i
	return prod

def nCr(n, r):
	n=conv(n)
	r=conv(r)
	return str(fact(n)/fact(r)/fact(n-r))

def help():
	print("""- Type 'quit' to stop the program.
- To add two numbers, type "a+b".
- To subtract two numbers, type "a-b".
- To multiply two numbers, type "a*b".
- To divide two numbers, type "a/b".
- To take the sin of a number, type "sin(a)", will be done in radians.
    cos(a) for cos, tan(a) for tan.
- To take the lcm of a number, type "lcm(a,b,...)" as many arguments as you want.
- To take the gcd of a number, type "gcd(a,b,...)" as many arguments as you want.
- To use your previous answer, type 'ans'.
- NOTE: This program will not follow PEMDAS. Please us parentheses as much as possible to specify what you want.
- log(a, b) --> Log_a (b).
- sqrt(a) --> square root of a.
- a^b --> a to the power of b.
- a! --> a factorial.
- e --> value of e in math, 2.718...
- phi --> the value of phi in math
- nCr(n, r) --> returns n choose r
""")

def decode(s):
	stack = []
	m = {}
	if (num(s)):
		return str(s)
	for i in range(len(s)):
		if (s[i]=='('): 
			stack.append(i)
		elif (s[i]==')'): 
			m[i]=stack[-1]
			m[stack[-1]]=i
			stack.pop()
	while (True):
		if (num(s)):
			break
		if (s[0]=='('):
 			s = decode(s[1:m[0]])+s[m[0]+1::]
		elif (len(s)>=3 and s[0:3]=="lcm"):
			l = split(s[4:-1])
			cLCM=lcm(decode(l[0]), decode(l[1]))
			if (len(l)>2):
				for i in range(2, len(l)):
					cLCM=lcm(cLCM,l[i])
			s = cLCM
		elif (len(s)>=3 and s[0:3]=="nCr"):
			l = split(s[4:-1])
			s = str(nCr(decode(l[0]), decode(l[1])))
		elif (len(s)>=3 and s[0:3]=="gcd"):
			l = split(s[4:-1])
			cGCD=gcd(decode(l[0]), decode(l[1]))
			if (len(l)>2):
				for i in range(2, len(l)):
					cGCD=gcd(cGCD,l[i])
			s = cGCD
		elif (len(s)>=3 and s[0:3]=="sin"):
			s = str(math.sin(float(decode(s[4:-1]))))
		elif (len(s)>=3 and s[0:3]=="cos"):
			s = str(math.cos(float(decode(s[4:-1]))))
		elif (len(s)>=3 and s[0:3]=="tan"):
			s = str(math.tan(float(decode(s[4:-1]))))
		elif (len(s)>=2 and s[0:2]=="pi"): 
			s = str(math.pi)+s[2::]
		elif (len(s)>=3 and s[0:3]=="ans"):
			s = str(ans)+s[3::]
		elif (len(s)>=3 and s[0:3]=="phi"):
			s = str(phi)+s[3::]
		elif (len(s)>=1 and s[0]=="e"):
			s = str(math.e)+str[1::]
		elif (len(s)>=3 and s[0:3]=="log"):
			l = split(s[4:-1])
			s = str(math.log(float(decode(l[1])), float(decode(l[0]))))
		elif (len(s)>=4 and s[0:4]=="sqrt"):
			s = str(math.sqrt(float(decode(s[5:-1]))))
		elif (s[0].isnumeric()):
			counter=1
			while (s[counter].isnumeric() or s[counter]=='.'):
				if counter+1==len(s):
					return s
				counter += 1
			if s[counter]=='+':
				s = str(float(decode(s[0:counter])) + float(decode(s[counter+1::])))
			elif s[counter]=='*':
				s = str(float(decode(s[0:counter])) * float(decode(s[counter+1::])))
			elif s[counter]=='/':
				s = str(float(decode(s[0:counter])) / float(decode(s[counter+1::])))
			elif s[counter]=='-':
				s = str(float(decode(s[0:counter])) - float(decode(s[counter+1::])))
			elif s[counter]=='^':
				s = str(float(decode(s[0:counter])) ** float(decode(s[counter+1::])))
			elif s[counter]=='!':
				s = str(fact(decode(s[0:counter])))
		else:
			break
	return str(s)

print("Type 'help' for more information on how to use this.")

while (True):
	toDecode = input("Please enter your expression: ")
	toDecode=toDecode.replace(" ", "")
	if (toDecode=="help"):
		help()
	elif (toDecode=="quit"):
		break
	else:
	    ans=decode(toDecode)
	    print(ans)