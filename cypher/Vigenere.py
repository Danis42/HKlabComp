import collections
import string

#fileind = input("file path: ")
fileind = "c1.txt"

#alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
print("Alphabet:")
alpha = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/'
alpha = list(alpha)
org=[]
beta=[]
gama=[]
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


print("Cipher Text:")
print(beta ,"\n")

rang = len(beta)
a=5
print("split the civer text into ", a ," to find duplicates")
sear=""
for d in range(0,rang-a,1):
	for x in range(0,a):
		sear=sear+str(beta[d+x])	
	gama.append(sear)
	sear=""

dupes=[item for item, count in collections.Counter(gama).items() if count > 1]
print(dupes)


print("\n",a,"char groups")
print(gama)


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
