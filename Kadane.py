def maxSubarray(arr):
    max_sum=max(arr)
    max_current=max_global=arr[0]


    for i in range(0,len(arr)):
        
        max_current=max(arr[i],max_current+arr[i])
        
        if max_current>max_global:
            max_global=max_current
   
    print(max_global)
    return
# Another code copied from https://github.com/SrGrace/Algorithms_Example/blob/master/Kadane's/Python/Kadane.py

def kadane(A):
	max_so_far = max_ending = 0
	for x in A:
		max_ending = max(0, max_ending + x)
		max_so_far = max(max_so_far, max_ending)
	return max_so_far

A = [-2, -3, 4, -1, -2, 1, 5, -3]
print "Maximum contiguous sum is", kadane(A)
