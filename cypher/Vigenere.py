import string
#fileind = input("file path: ")
fileind = "c1.txt"

#alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
alpha = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/'
alpha = list(alpha)
org=[]
beta=[]
gama=[]
delta=[]
solution=[]

txt = open(fileind)
print(alpha)

while (True):
	c = txt.read(1)
	if not c:
		print()
		break
	org.append(c)
	for i in alpha: 
		if i==c: 
			beta.append(i)


print(beta ,"\n")

rang = len(beta)
a=3
print("split the civer text into ", a ," to find duplicates")
sear=""
grou=""
for d in range(0,rang-a,1):
	for x in range(0,a):
		sear=sear+str(beta[d+x])	
		grou=grou+str(beta[d+x])	
	delta.append(grou)	
	gama.append(sear)
	sear=""
	grou=""

for h in range(0,len(gama)):
	count=0
	for i in range(h+1,len(gama)):
		if gama[h]==gama[i]:
			count=count+1
			print(gama[h]," ",count," ", i-h)


print("\n",a,"char groups")
print(delta)


pw=['b','d','a','e']
pw=pw*(int(len(beta)/len(pw))+1)	

#print(pw)

for k in range(0,len(beta)):
	indd= alpha.index(beta[k])-alpha.index(pw[k])
	if indd < 0:
		indd+=len(alpha)
	solution.append(alpha[indd])


print("\n")
print(''.join(org))
#print(org)
print("decrypted text with spaces:\n")
for i in range(0,len(org)):
	if org[i]=="'":
		solution.insert(i,"'")
	if org[i]==".":
		solution.insert(i,".")
	if org[i]=="\n":
		solution.insert(i,"\n")
	if org[i]==" ":
		solution.insert(i," ")
print(''.join(solution))
