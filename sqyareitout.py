"""low = int(input("Enter the lower bound of the number range that you want to generate as square numbers : "))
up = int(input("Enter the upper bound of the number range that you want to generate as square numbers : "))

for i in range (low, up + 1):
    print("The number is", i)"""

numlst = []

for i in range (5):
    nums = int(input("Enter the five numbers of a list : "))
    numlst.append(nums)
print("The list is", numlst) 

# squaring the numbers
squnum1 = numlst[0] * numlst[0]
squnum2 = numlst[1] * numlst[1]
squnum3 = numlst[2] * numlst[2]
squnum4 = numlst[-2] * numlst[-2]
squnum5 = numlst[-1] * numlst[-1]

sqalist = [squnum1, squnum2, squnum3, squnum4, squnum5]
print("The squared list is ",sqalist)

oddlst = [] # list to store the odd numbers
evenlst = [] # list to store the even numbers

# seperating the odd and even numbers
if (squnum1 % 2 == 0):
    evenlst.append(squnum1)
else:
    oddlst.append(squnum1) 

if (squnum2 % 2 == 0):
    evenlst.append(squnum2)
else:
    oddlst.append(squnum2) 
           
if (squnum3 % 2 == 0):
    evenlst.append(squnum3)
else:
    oddlst.append(squnum3) 
               
if (squnum4 % 2 == 0):
    evenlst.append(squnum4)
else:
    oddlst.append(squnum4) 
                   
if (squnum5 % 2 == 0):
    evenlst.append(squnum5)
else:
    oddlst.append(squnum5) 

print("The list containing even numbers is", evenlst)      
print("The list containing odd numbers is", oddlst)                      