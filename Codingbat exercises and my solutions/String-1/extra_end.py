""" Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
 """
#My solution:

def extra_end(str):
  
  new_str =str[-2] + str[-1] 
  
  return new_str*3
#Alt. return str[-2:]*3
