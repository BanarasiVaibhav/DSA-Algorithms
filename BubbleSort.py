# this is bubble sort
a=[9,6,5,2,1]
for i in range(len(a)):                           # outer loop variable i 
    for j in range(i+1,len(a)):                   # inner loop variable j
        if a[i]>a[j]:                             # comparison
            a[i],a[j]=a[j],a[i]                   # swapping
            print(a)
        print('i='+str(i  )+'   j='+str(j))
