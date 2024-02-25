#!/usr/bin/env python
# coding: utf-8

# In[1]:

#day 33.
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping 
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# In[2]:


# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
	
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))


# In[3]:


# Python len()
li = [10, 20, 30]
n = len(li)
print("The length of list is: ", n)


# In[4]:


lst=[ 1, 6, 3, 5, 3, 4 ] 
#checking if element 7 is present
# in the given list or not
i=7
# if element present then return
# exist otherwise not exist
if i in lst: 
	print("exist") 
else: 
	print("not exist")


# In[5]:


star = [6, 0, 4, 1]
print('star before clear:', star)

# Clearing list
star.clear()
print('star after clear:', star)


# In[ ]:




