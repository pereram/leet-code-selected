#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:45:34 2025

@author: meeghageperera
"""


'''
first missing poisitive 
-------------------------

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

'''


num=[10,22,-1,9,2,3,4,6,8,1]

 
length=len(num) # get tyhe length of the list


for i in range(length):
    # only store positive values in exact index. index 0 is 1, index 1 is 2 etc etc
 
# swap current element num[i]

    while 0<num[i]<length and num[i]!=i+1:
    # only swap the positive and numbers in list's length
    #swaping the current element and the element in it's supposed to be index.
        new_ind=num[i]-1 
        old_ind=i
        
        num[old_ind],num[new_ind]=num[new_ind],num[old_ind]
        
    
for ind,ele in enumerate(num):
    if ele!=ind+1:
        print("The missing smallest positive is ", ind+1)
        break;
    
 
 

