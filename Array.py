print("Hello data structure world")

array=[10, 3, 7, 5, 'Adam', -12] #in Python we can add mix type of items in array

print(array[1])


print(array[:])

print(array[0:2])

print(array[:-2])

#changing, adding and removing items from an array/list:
array[4] = 'Eva' #changes item "Adam" to "Eva"

print(array[4])

array.remove('Eva') #searches for and removes "Eva", then reorders the array/list

array.insert(2,33) #inserts 33 at index 2

array.append(-44) #adds -44 at the end of an array/list

del array[-1] #deletes the last item

array.pop(4) #removes the item at index 4

array2= [105, 505]

array.extend(array2) # extending array with array2

print(len(array)) # printing the number of elements in the array/list

print(array[:])

#linear search O(n):
max = array[0]
for num in array:
    if num>max:
        max=num
print (max)

#Reversing Array In-Place:
def reverse(nums):
    start_index=0
    end_index=len(nums)-1

    while end_index> start_index:
        nums[start_index], nums[end_index] = nums [end_index], nums[start_index]
        start_index = start_index+1
        end_index = end_index -1

reverse(array)
print(array[:])

sorted(array)
print(array[:])
