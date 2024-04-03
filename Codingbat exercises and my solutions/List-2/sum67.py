""" Return the sum of the numbers in the array,
except ignore sections of numbers starting with a 6
and extending to the next 7 (every 6 will be followed by at least one 7).
Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
 """
#My solution:

def sum67(nums):
  
  total = 0
  found_a_6 = False
  
  if len(nums) == 0:
    return 0
  else:
  
    for i in range(len(nums)):
      if nums[i] == 6:
        
        found_a_6 = True
      
      if not found_a_6: 
        
        total = total + nums[i]
      
      if found_a_6 and nums[i] == 7:
        
        found_a_6 = False
        
  return total