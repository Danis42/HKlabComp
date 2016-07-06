counter = 0
for i in object.__subclasses__():
	if i == file:
		print(counter)
		print(i)
	#print(counter,i)
	counter += 1



#print(object.__subclasses__())
