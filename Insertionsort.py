#insertion  sort from introduction to algorithm CLRS


a=[1,23,45,22,34,56,3,77,54,6]
for j in range(2,len(a)):
    key =a[j]
    i = j-1
    while i >0 and a[i]>key:
        a[i+1]=a[i]
        i=i-1
    a[i+1]=key

print(a)


# New improved code with values of i and j
a=[9,6,5,2,1]
for i in range(len(a)):                           # outer loop variable i 
    for j in range(i+1,len(a)):                   # inner loop variable j
        if a[i]>a[j]:                             # comparison
            a[i],a[j]=a[j],a[i]                   # swapping
            print(a)
        print('i='+str(i  )+'   j='+str(j))
