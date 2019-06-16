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

# New improved code with values of i and j
# I have no idea wich sort is this
a=[9,6,5,2,1]
for i in range(len(a)):                           # outer loop variable i 
    for j in range(i+1,len(a)):                   # inner loop variable j
        if a[i]>a[j]:                             # comparison
            a[i],a[j]=a[j],a[i]                   # swapping
            print(a)
        print('i='+str(i  )+'   j='+str(j))
