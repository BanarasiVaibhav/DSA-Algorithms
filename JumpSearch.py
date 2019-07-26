import random
arr=[]
size_of_array=int(input("enter size of array:  "))
element_to_be_searched=int(input("enter element to be searched between 0 to 100:  "))
jump_number=int(input("enter jump number:  "))
for i in range(size_of_array):
  arr.append(random.randint(0,100))

arr.sort()
print(arr)


def linear_search(arr,element_to_be_searched):
  found=0
  for i in range(0,len(arr)):
    if element_to_be_searched==arr[i]:
      print("Item found from linear search ",element_to_be_searched,"on index ",i)
      found=1
      break
    if found !=1:
      print("element not found from linear search")




for i in range(0,size_of_array,jump_number):
  
  if arr[i]==element_to_be_searched:
    print("Element found at index:  ",i," from jump search")
    break
  
  if element_to_be_searched < arr[i] and element_to_be_searched > arr[i-jump_number]:
    print("linear search required")
    print(i-jump_number,i)
    linear_search(arr[i-jump_number:i],element_to_be_searched)
  else:
    print("item not found from jump search")




