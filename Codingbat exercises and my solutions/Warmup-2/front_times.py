""" Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
or whatever is there if the string is less than length 3.
Return n copies of the front;

Examples:
front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc' """

#My solution:
#Just copy the three first letters. 
#When I write :3 it is actually the same as 0:3, and the last part is not included.


def front_times(str, n):
  front = str[:3]
  return n * front
