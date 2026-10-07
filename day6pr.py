#palindrome
list1 =[1,2,3,2,1,5]
copy_list1 = list1.copy()
copy_list1.reverse()
if(list1 == copy_list1):
     print("the list is palindrome")
else:
     print("list is not palindrome")