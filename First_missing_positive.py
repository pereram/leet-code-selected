
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

# the following code will solve this with nlog(n) time complexity

num=[10,22,-1,1,2,3,5,4,6,8]

num.sort()  # O(nlog(n))


for i,val in enumerate(num):
    if (val-num[i-1])>1 and (num[i-1]>0): # if prev element is positive and 
                                          # the diff between current and prev is 2          
     print('The missing first positive is',num[i-1]+1)
     break

