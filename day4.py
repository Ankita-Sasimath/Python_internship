#checking power of 2
n=int(input())
while n:
    if n==1:
        print("yes")
        break
    if n%2!=0:
        print("no")
        break
    n=n//2

#break statement
for i in range(1,5):
    for j in range(1,5):
        if j==3:
            break
        print(i,j)

for i in range(5):
    if i>3:
        break
    print(i)


    
count=0
while count<5:
    count+=1
    if count==3:
        break
    print(count)


#tuple remove
t=(1,2,3,4,5,6)
t=t[:5]+t[6:]
print(t)


#palindrome
n=int(input())
if n<0:
    return False
rev=0
original=n
while n:
    rev=rev*10+n%10
    n//=10
if original==rev:
    return True
else:
    return False

#dictionary
student_marks={'a':90,'b':80,'c':60,'d':50,'e':40}
stu_grade={}
for i in student_marks:
    marks=student_marks[i]
    if marks>=90:
       stu_grade[i]='A+'
    elif marks>=80:
       stu_grade[i]='A'
    elif marks>=60:
       stu_grade[i]='B+'
    elif marks>=50:
       stu_grade[i]='B'
    else:
       stu_grade[i]='C'
print(stu_grade)
        

