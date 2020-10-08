#  ASSIGNMENT-1
# Question 4

list1 = [10, 45, 3, 5, 1, 40, 13]
list1[0], list1[-1] = list1[-1],list1[0]
print(list1)


#----------Method 2 ----------


def swap_list(list1):
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1


list1=[]
num = int(input("Enter number of elements you want in list: "))
for i in range(1, num+1):
  value = int(input("Enter Values:"))
  list1.append(value)
print(list1)
print(swap_list(list1))



