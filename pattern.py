num =  int(input("Enter a number "))
for i in range(num+1):
	for j in range(num+1):
		if j<=i:
			print("* ", end ="")
		else:
			print("  ", end ="")
	print()
print("The notpad is working")