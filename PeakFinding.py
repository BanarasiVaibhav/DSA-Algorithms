import random

arr=[]
for i in range(10000):
	arr.append(random.randint(0,99))
print(arr)

for i in range(1,9999):
	if i is 0:
		if arr[0]>arr[1]:
			print(arr[i],'is peak element at index ' ,i)
	if i is len(arr)-1:
		if arr[len(arr)-2]>arr[len(arr)-1]:
			print(arr[i],'is peak element at index ' ,i)		
	if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
		print(arr[i],'is peak element at index ' ,i)
