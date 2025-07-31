numlst = [] # intially assuming this as a list
timesoftuple = int(input("Enter the number of numbers that you have in you tuple : "))

for i in range(timesoftuple):
    nums = int(input("Enter the numbers that you have in your tuple : "))
    numlst.append(nums)

numtup = tuple(numlst) # converting the list to tuple
print("The tupple is ",numtup)

multiply = 1

for i in numtup : # here range is not needed in the for loop as we are mentioning it to get inside and access the numbers inside the tuple
    multiply *= i
print("The product of the tuple is ",multiply)    