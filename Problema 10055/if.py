n=int(input("Cual es tu edad?: "))
print("Tu edad es",n)
if n <= 5:
	print("Eres un bebe")
elif n <= 12:
	print("Eres un niño")
elif n <= 19:
	print("Eres un adolecente")
else:
	print("Eres un adulto")