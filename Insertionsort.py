#insertion  sort from introduction to algorithm CLRS
import random

def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]<key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr 

arr=[]
for i in range(0,100):
    arr.append(random.randint(0,100))
print(arr)
insertionSort(arr)
=========================================================================================================================================

