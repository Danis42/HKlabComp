print("Please select the third Cipher Text (c3.txt)")
fileind = input("file path: ")

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
i=0

while i<len(alpha):
	txt = open(fileind)
	print(i)
	print()
	while (True):
		c = txt.read(1)
		if (not c) or (c=="!"):
			break
		try:
			if((int(alpha.index(c))+i)<len(alpha)):
				test=int(alpha.index(c)+i)
				print(alpha[test],end="")
			else:
				test=int(alpha.index(c)+i)-len(alpha)
				print(alpha[test],end="")
		except ValueError:
			print(" ",end="")
	i=i+1


print("Content of c3.txt")
print("")
txt = open(fileind)
while (True):
	c = txt.read(1)
	if not c:
		print("end")
		break
	print(c,end="")


#Solution: The Cesar cipher is moved by 16 
