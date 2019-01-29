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
