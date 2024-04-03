""" The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

Eaxmples
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True """

#My solution:

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  
  #That was the simpliest I could think of.
