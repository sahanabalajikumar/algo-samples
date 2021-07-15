#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true

#Example 2:
#Input: s = "rat", t = "car"
#Output: false

''''
def reverseString(s):
  reverseList = []
  for i in range(len(s)): 
    reverseList.append(s[-1])
    s = s[:-1]
  print(reverseList)

    

reverseString("Hello")
'''

def anagram(s, t):
  reverse = []
  for i in range(len(s)):
    reverse.append(s[-1])
    s = s[:-1]
  listoft = []
  for each in t:
    listoft.append(each)
  if listoft == reverse:
    return True
  else:
    return False

print(anagram("cat", "tacr"))
