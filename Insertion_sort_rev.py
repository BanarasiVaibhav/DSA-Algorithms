#insertion  sort from introduction to algorithm CLRS


a=[1,23,45,22,34,56,3,77,54,6,54,2,3,221,3123,5,23,34,24545,654,4,87]
#a.sort()
print(a)
for j in range(1,len(a)):
    key =a[j]
    i = j-1
    while i >=0 and a[i]<key:
        a[i+1]=a[i]
        i=i-1
    a[i+1]=key

print(a)
a.sort()
print(a)
