n=int(input("Dame un numero: "))
#for i in range(n):
#	print("*", end="")
#print()

#for i in range(n):
#	s=n-i
#	for i in range(s):
#		print("*", end="")
#	print()

for i in range(n-1):
	s=i+1
	for i in range(s):
		print("*",end="")
	print()
for i in range(n):
	s=n-i
	for i in range(s):
		print("*", end="")
	print()