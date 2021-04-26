# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Mike
organize his grocery shopping list.
"""

# @TODO: Create a list of groceries

groceries = ["water", "butter", "eggs", "apples", "cinnamon", "sugar", "milk"]

# @TODO: Find the first two items on the list

print(groceries[0:2])


# @TODO: Find the last five items on the list

print(groceries[-5:])


# @TODO: Find every other item on the list, starting from the second item

print(groceries[1::2])


# @TODO: Add an element to the end of the list

groceries.append("chicken_wings")
print(groceries)



# @TODO: Changes a specified element within the list at the given index

groceries[3] = "gala_apples"
print(groceries)



# @TODO: Calculate how many items you have in the list

print(len(groceries))


# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name

print(groceries.index("cinnamon"))



# @TODO: Remove an element from the list based on the given element name

groceries.remove("sugar")
print(groceries)



# @TODO: Remove an element from the list based on the given index

milk_index = groceries.index("milk")
groceries.pop(milk_index)
print(groceries)




# @TODO: Remove the last element of the list

groceries.remove("{-6}")
print(groceries)



print("You continue on your journey purchasing groceries...")
