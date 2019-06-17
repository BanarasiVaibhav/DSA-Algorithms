l1=[1,2,3,4,5,6,7,8]
l2=[5,6,6,7,8,9,10,12,34,353,356,357,358]
i1=0
i2=0
arr=[]
while i1<len(l1) and i2<len(l2):
	if l1[i1]<=l2[i2]:
		arr.append(l1[i1])
		i1+=1
	else:
		arr.append(l2[i2])
		i2+=1
while (i1<len(l1)):
	arr.append(l1[i1])
	i1+=1
while (i2<len(l2)):
	arr.append(l2[i2])
	i2+=1

print(arr)
