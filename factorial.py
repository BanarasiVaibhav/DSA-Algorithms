def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(10))

n=int(input('enter the number to be factorial:  '))
sum=1
for i in range(1,n+1):
    sum=sum*i
    i+=1
    print(sum)
print(sum)
