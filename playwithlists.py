L = [2, 4, 6, 7, 8, 3, 6]
print("Original List : ",L)

# varriable to store the sum of the list
count = 0

# finding the sum
for i in L:
    count += i

# divide the total elements by number of elements
avg = count/len(L)

print("Sum = ",count)
print("Average = ",avg)

# sorting the elements of the list 
# sort will by default print the elements in ascending order
L.sort()

# printing the first element
print("Smallest element is :", L[0])

#print the last element
print("Largest element is:", L[-1])

#print the second last element
print("Second last element", L[-2])