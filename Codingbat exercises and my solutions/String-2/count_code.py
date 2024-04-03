""" Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

Examples:
count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2 """

#My solution:

#Thoughtprocess. We cannot just count the word code because of the d letter.
#Instead we count the count the letter "co" followed by "e" after one char between them.

def count_code(str):
  
  count_code = 0
  
  for i in range(0, len(str) - 3, 1):
    
    if str[i:i+2] =="co" and str[i+3] == "e":
      
      count_code = count_code + 1
      
  return count_code


