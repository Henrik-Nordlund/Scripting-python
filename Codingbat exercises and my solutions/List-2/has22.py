""" Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
 """
#My solution:

def has22(nums):
  for i in range(0, len(nums) -1 , 1):
    if nums[i] == 2 and nums[i+1] ==2: 
        return True
    
  return False