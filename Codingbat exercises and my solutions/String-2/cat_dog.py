""" Return True if the string "cat" and "dog" appear the same number of times in the given string.

Examples:
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True """

#My solution:

def cat_dog(str):
  if str.count("cat") == str.count("dog"):
    return True
  else:
    return False