# program for all methods in list

numbers = [10, 20, 30, 40, 20]

print("Original List:", numbers)

# 1. append()
numbers.append(50)
print("Append:", numbers)

# 2. insert()
numbers.insert(1, 15)
print("Insert:", numbers)

# 3. extend()
numbers.extend([60, 70])
print("Extend:", numbers)

# 4. remove()
numbers.remove(20)
print("Remove:", numbers)

# 5. pop()
numbers.pop()
print("Pop:", numbers)

# 6. sort()
numbers.sort()
print("Sort:", numbers)

# 7. reverse()
numbers.reverse()
print("Reverse:", numbers)

# 8. count()
print("Count:", numbers.count(20))

# 9. index()
print("Index:", numbers.index(30))

# 10. copy()
new_list = numbers.copy()
print("Copy:", new_list)

# 11. clear()
new_list.clear()
print("Clear:", new_list)
