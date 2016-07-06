# base64

#fileind = input("file path: ")

fileind="c2.txt"   # File def

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
binStr=[]
encod=""

print("")			
txt = open(fileind)		# open File
while (True):			# read and print File
	c = txt.read(1)
	if not c:
		break
	print(c,end="")

#--------------------- Encryption ----------------


txt = open(fileind)
while(True):
	c=txt.read(1)				#read file one by one
	if not c or c=="=":
		break

	binStr+=bin(alpha.index(c))[2:].zfill(6) #take 1 char and get its index from alpha and make it 6Bit binary


print("-----")
while not len(binStr) % 8 == 0:			#Fill up the missing 0 at the end
	binStr+="0"
	
for i in range(0,len(binStr),8):		# go though array and read binary string
	trs=""
	for j in range(0,8):
		trs+=binStr[i+j]	
	encod=int(trs,2)
	
	if encod >= 125 or encod <= 32:		# Filter for readable Stuff
		break 
	else:
		#print(str(binStr[i:i+8])+"  "+str(trs)+"  "+str(encod))
		print(chr(encod),end="")





