#Write a function that reverses a string. The input string is given as an array of characters S
# Example
# Input s = ["h", "e", "l", "l", "o"]
# Ouput : [ "o", "l", "l", "e", "h"]

def reverseString(s):
  reverseList = []
  for i in range(len(s)): 
    reverseList.append(s[-1])
    s = s[:-1]
  print(reverseList)

    

reverseString("Hello")