### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card):
    #single equals should be double equals as we are looking for equality, not assigning a variable
    if card.value = 1:
      return True
    #else is missing a colon after it
    else
      return False
   
  #typo when defining function dif should be def
  #missed comma between card1 and card2 parameters
  dif highest_card(self, card1 card2):
  #if/else statement should be indented one tab more
  if card1.value > card2.value:
    #card has not been assigned, should return card1
    return card
  else:
    return card2
  


def cards_total(self, cards):
  #total variable has not been defined, should be total = 0
  total
  for card in cards:
    total += card.value
    #return statement is indented incorrectly. Should be indented one tab less so it runs after the loop has finished
    #can't concatenate a string with an integer value, use an f string instead and put total inside of curly brackets
    return "You have a total of" + total
  
```
