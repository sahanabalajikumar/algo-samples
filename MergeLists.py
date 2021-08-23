#Question:
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


def mergesortarray(list1, list2, m1, m2):
  kamnaisgaga = []
  if len(list1) < m1:
    m1 = len(list1)
  if len(list2) < m2:
    m2 = len(list2)
  for i in range(m1):
    kamnaisgaga.append(list1[i])
  for i in range(m2):
    kamnaisgaga.append(list2[i])
  print(kamnaisgaga)

mergesortarray([1, 2, 3], [1, 2, 3, 4, 5], -1, -1)