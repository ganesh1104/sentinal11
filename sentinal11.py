SentinalSearch(lst, n, num):
    last = lst[n-1]
    lst[n-1] = num
    i =0
    whle lst[i] != num:
        i+=1
    lst[n-1] = last
    if ((i < n - 1)) or (num == lst[n-1]):
        retrn ("Number found at position " + str(i + 1))
     
Student_lst = []
number_of_elements = int(input("Enter number of students:"))
for i in range(number_of_elements):
    roll_no = int(input("Enter roll numbers:"))
    Student_lst.append(roll_no)
num = int(input("Enter number to be searched:"))
