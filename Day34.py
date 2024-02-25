#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Day 34.

def main():
    # Define a list of fruits
    fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']

    # Iterate over the list of fruits and print each fruit along with its index
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")

if __name__ == "__main__":
    main()


# In[2]:


def main():
    # Define a list of numbers
    numbers = [10, 20, 30, 40, 50]

    # Use enumerate to double each number in the list
    for index, number in enumerate(numbers):
        numbers[index] = number * 2

    # Print the modified list
    print("Modified list:", numbers)

if __name__ == "__main__":
    main()


# In[3]:


def main():
    # Define a list of characters
    characters = ['a', 'b', 'c', 'd', 'e']

    # Use enumerate to reverse the list
    reversed_characters = [char for _, char in reversed(list(enumerate(characters)))]

    # Print the reversed list
    print("Reversed list:", reversed_characters)

if __name__ == "__main__":
    main()


# In[4]:


def main():
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Use enumerate to filter even-indexed numbers
    filtered_numbers = [num for index, num in enumerate(numbers) if index % 2 == 0]

    # Print the filtered list
    print("Filtered list:", filtered_numbers)

if __name__ == "__main__":
    main()


# In[5]:


def main():
    # Define a list of fruits
    fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']

    # Define the fruit to search for
    search_fruit = 'orange'

    # Use enumerate to find the index of the search fruit
    for index, fruit in enumerate(fruits):
        if fruit == search_fruit:
            print(f"The index of '{search_fruit}' is {index}")
            break
    else:
        print(f"'{search_fruit}' not found in the list")

if __name__ == "__main__":
    main()

    


# In[ ]:




