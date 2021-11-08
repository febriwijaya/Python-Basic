# Python Lists
print("\nPython Lists")
primary_colors = ['Red', 'Green', 'Blue']
even_numbers_berofre_ten = [2, 4, 6, 8]
event_a = ['Surabaya', 1300]
print(str(type(even_numbers_berofre_ten)) +' '+ str(type(event_a)))
event_b = ['Manado', 1450]
events = [event_a, event_b]
print(events)

# Modifying & Access List Value
print("\nModifying & Access List Value")
events = [
    primary_colors,
    even_numbers_berofre_ten
]
print(events[0][1]) # Must be green
print(event_a[-1]) # Must be 1300
print(len(event_a))
print("A single value in a list can be replaced by indexing and simple assignment:")
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-1] = 20
print(a)

# Slice list
print("What if you want to change several contiguous elements in a list at one time? Python allows this with sliceassignment, which has the following syntax:")
print(a[1:4])

# Modify using slice
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)

#Other operation
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine') # Count value in list
fruits.index('banana') # Find index list.index(x[, start[, end]])
fruits.index('banana', 4)  # Find next banana starting a position 4 
fruits.reverse() # Reverse list
fruits.append('grape') # Add value in list
fruits.sort() # list.sort(*, key=None, reverse=False)
fruits.pop() #list.pop([i]) Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
fruits.clear() # remove all items from list