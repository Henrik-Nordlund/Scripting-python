#Given a string, return a string where for every char in the original, there are two chars.

#Examples below:
#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'

#My solution


def double_char(str):
  total = ""
  for i in range(len(str)):
    total = total + str[i] + str[i]
  
  return total 
