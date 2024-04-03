""" Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values,
it does not count towards the sum.

Examples:
lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
 """
#My solution:

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  elif a != b and a !=c and b!=c:
    return a+b+c
  elif a==b:
    return c
  elif a==c:
    return b
  else:
    return a