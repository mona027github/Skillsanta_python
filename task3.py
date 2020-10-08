#  ASSIGNMENT-1
# Question 3


list1=['Python','Machine Learning','Data Science']
list2=['Skillsanta','Web Development','Learning platform']
merged_list = list1 + list2
merged_list.sort()
print(merged_list)



# ----------  Method 2 ----------------

def merge(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return(merged_list)

list1=[]
list2 =[]
num1 = int(input("Enter number of elements in list1: "))
num2 = int(input("Enter number of elements in list2: "))
for i in range(1, num1+1):
  value1 = int(input("Enter values in first list:"))
  list1.append(value1)
for i in range(1, num2+ 1):
  value2 = int(input("Enter values in second list:"))
  list2.append(value2)
print("Final sorted list is:" ,merge(list1, list2))