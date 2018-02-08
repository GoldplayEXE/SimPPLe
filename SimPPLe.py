#Simple Probabilistic Programming Language - SimPPLe

import sys
import random

i = 0
b = 1
p = []
v = {}
with open(sys.argv[1]) as f:
	for l in f:
		if l[-1]=="\n":
			p.append(l[:-1])
		else:
			p.append(l)

class f:
	def int():
		v[arg1] = random.randrange(0x110000)
	
	def flt():
		v[arg1] = random.random()

	def out():
		print(v[arg1])

	def intIn():
		v[arg1] = random.randrange(input("int: "))

	def chrOut():
		print(chr(int(v[arg1]%95)+32))
		
	def chrIn():
		v[arg1] = random.randrange(ord(input("chr: ")))
		
	def add():
		v[arg1] += v[arg2] + random.randrange(0x110000)
	
	def sub():
		v[arg1] -= v[arg2] - random.randrange(0x110000)
		
	def mul():
		v[arg1] *= v[arg2] * random.randrange(0x110000)
		
	def div():
		v[arg1] /= v[arg2] / random.randrange(0x110000)
		
	def mod():
		v[arg1] %= v[arg2] % random.randrange(0x110000)

 	def jmp():
		global i
		i = v[arg1] % len(p)
		
	def prntln():
		print(i)
		
	def end():
		global b
		b = 0
	
	def jmpGtr():
		global i
		if v[arg1] > v[arg2]:
			i = v[arg1] % len(p)
		elif v[arg2] > v[arg1]:
			i = v[arg2] % len(p)
		else:
			pass
	
	def jmpLss():
		global i
		if v[arg1] < v[arg2]:
			i = v[arg1] % len(p)
		elif v[arg2] < v[arg1]:
			i = v[arg2] % len(p)
		else:
			pass
	
c = {
		"int"		:	f.int,			#declare new int and initialize with random value
		"flt"		:	f.flt,			#declare new float and initialize with random value
		"out"		:	f.out,			#output value of variable
		"intIn"		:	f.intIn,		#set variable to random value between 0 and userinput
		"chrOut"	:	f.chrOut,		#output value of variable as char
		"chrIn"		:	f.chrIn,		#set variable to random value between 0 and ASCII-value of userinput
		"add"		:	f.add,			#add two variables and save the result in the first
		"sub"		:	f.sub,			#subtract the second variable of the first and save the result in the first
		"mul"		:	f.mul,			#multiplicate two variables save the result in the first
		"div"		:	f.div,			#divide first variable by second variable and save the result in the first
		"mod"		:	f.mod,		
		"jmp"		:	f.jmp,			#jmp to value of variable
		"end"		:	f.end,			#end program
		"jmpGtr"	:	f.jmpGtr,		#jump to the greater value or continue execution normally if both are equal
		"jmpLss"	:	f.jmpLss		#jump to the lesser value or continue execution normally if both are equal
	}
	 
while i < len(p):
	l = p[i].split()
	i += 1
	try:
		arg1 = l[1]
	except:
		pass
	try:
		arg2 = l[2]
	except:
		pass
	c[l[0]]()
	if not b:
		break
	
