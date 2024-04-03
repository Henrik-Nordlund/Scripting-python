""" Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
 """
#My solution:

def has23(nums):
  for i in nums:
    if i == 2:
      return True
      
    elif i == 3:
      return True
      
    elif nums[-1] == 2 or nums[-1] == 3:
      return True
    
    else:
        return False
    

