""" Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
 """
#My solution:

def not_string(str):
  if str[:3] == "not":
    return str
  else:
    new_str = "not " + str
    return new_str