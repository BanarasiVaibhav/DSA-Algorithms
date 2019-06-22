def maxSubarray(arr):
    max_sum=max(arr)
    max_current=max_global=arr[0]


    for i in range(0,len(arr)):
        
        max_current=max(arr[i],max_current+arr[i])
        
        if max_current>max_global:
            max_global=max_current
   
    print(max_global)
    return
