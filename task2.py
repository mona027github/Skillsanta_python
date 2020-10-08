#  ASSIGNMENT-1
# Question 2

list1 = [10, 45, 3, 5, 1, 40, 13]
print("Second largest number in the list is: ",sorted(list1)[-2])





# --------Method 2-----------
list1 = []
num = int(input("Enter number of elements in list: "))

for i in range(1, num+1):
  value = int(input("Enter Values:"))
  list1.append(value)
print("Second largest number in the list is: ",sorted(list1)[-2])