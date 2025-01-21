#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:40:58 2025

@author: meeghageperera

Given an array and an integer K, find the maximum for each and every contiguous 
subarray of size K.

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
Output: 3 3 4 5 5 5 6
Explanation: Maximum of 1, 2, 3 is 3
            Maximum of 2, 3, 1 is 3

"""

# Returns maximum sum in
# a subarray of size k.
def maxSum(arr, k):


    
    # Compute sum of first
    # window of size k
    res = 0
    for i in range(k):
        res += arr[i]

    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of 
    # current window.
    curr_sum = res
    for i in range(k, len(arr)):
    
        curr_sum += arr[i] - arr[i-k]
        res = max(res, curr_sum)

    return res

# Driver code
arr = [1, 4, 2, 10, -2, 3, 1, 0, 5]
k = 4
print(maxSum(arr,k))

