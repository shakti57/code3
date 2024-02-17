#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Day 31

def reverse_string(input_string):
    return input_string[::-1]

# Example usage:
original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
print("Original:", original_string)
print("Reversed:", reversed_string)


# In[2]:


def reverse_number(number):
    # Convert number to a string, reverse it, and convert it back to an integer
    reversed_number = int(str(number)[::-1])
    return reversed_number

# Example usage:
original_number = 12345
reversed_number = reverse_number(original_number)
print("Original number:", original_number)
print("Reversed number:", reversed_number)



# In[ ]:




