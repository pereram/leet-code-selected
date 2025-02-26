'''
Next Greater Element (NGE) for every element in given Array


Given an array arr[] of integers, the task is to find the Next Greater Element 
for each element of the array in order of their appearance in the array.
Note: The Next Greater Element for an element x is the first greater element o
n the right side of x in the array. Elements for which no greater element exist,
 consider the next greater element as -1. 
 
 
 Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since 
it doesn’t exist, it is -1.
 
 
 
'''





def nextGreater(lst):
    grt=[]  # creating an array for greater elements for each index
    size=len(lst)
    for i,val in enumerate(lst): # get the both value and index. Index is needed to 
                                # iterate through rest of the array.
        next=-1  # when the element has no greater value. use it as default
        temp=i   # current index as temp
        while (temp<size):   
            if lst[temp]>val: # check for a greater value in remainder of list
                next=lst[temp]
                break
            temp+=1
        #dict={str(val):str(next)}
        #grt.append(val)
        grt.append(next)

    return grt

grt=(nextGreater([2,1,5,7]))

for val in grt:

    print(val)