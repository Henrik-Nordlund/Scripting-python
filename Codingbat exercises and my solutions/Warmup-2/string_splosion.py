""" Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
 """
#My solution:

def string_splosion(str):
  result=""
  for i in range(len(str)):
    if len(str) <= 1:
      return str
    #in case the string is only 1 letter
    else:
      result = result + str[:i+1]
    #return the character that is in the loop and the one that comes immediately after it
      # you could also write str[0:i+1] I believe.
  return result
