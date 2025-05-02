#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 12:19:02 2025

@author: meeghageperera


32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of 
the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

"""
# the given string 
s="(()()"


'''

The same idea as paranthesis check problem. But here we calculate back the length
when the stack becomes empty, using (i-lst[-1])
'''

# creating the stack to store prarenthesis to check the valid order
lst=[]
lst.append(-1) # edge case elementr

# the valid length counter
max_len=0

length=len(s)

# if opening parenthesis, then push

for i in range(length):
    
    if s[i]=="(" :
        lst.append(i)
        

#if a closing paranthesis the pop from the stack.
        #case1: if the stack turned out to be empty after above pop,we need to add base
        #element.The validity can be continued  

        
        
    else:
        
        lst.pop()
        
          
        if len(lst)==0:
            lst.append(i)
            
        else:
# back calculate the valid length,          
          max_len=max(max_len, (i-lst[-1]))
          
            
print(max_len)
            
        
        
        
        
        
        
        
