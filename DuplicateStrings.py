#Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

#Example 1:

#Input: s = "bcabc"
#Output: "abc"
#Example 2:

#Input: s = "cbacdcbc"
#Output: "acdb

def removeduplicateletters(word):
  finalword = ""
  finaldict = {}
  for s in word:
    if s not in finaldict:
      finaldict[s] = s
      finalword += s
  return finalword

print(removeduplicateletters("abcccbbbb"))
