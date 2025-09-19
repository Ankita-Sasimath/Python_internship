#length of longest palindrome
s=input()
m=0
for c in range(len(s)):
  #odd length
    l,r=c,c
    while l >=0 and r<len(s) and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
    #even length
    l,r=c,c+1
    while l >=0 and r<len(s) and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1

#functions
def qwer():
    print("hi")
    asd()
def asd():
    print("hello")
    qwer()
qwer()
print(2)#(1000 is max depth in python for recursion)

def qwer(x):
    print(x,"hi")
    return 30
c=qwer(10)+600
print(c)

#set limit
import sys
sys.setrecursionlimit(2000)
def qwer(x):
    print("hi",x)
    qwer(x+1)
qwer(1)

#return-exit the function call
def qwer(x):
    if (x==6):
        return
    print(x)
    qwer(x+1)
qwer(1)

#square of number
def sq(n):
    print(n*n)
sq(16)

#lambda :square
s=lambda n:n*n
n=int(input())
res=s(n)
print(res)

s=lambda a,b:a+b
n=int(input())
m=int(input())
res=s(n,m)
print(res)

#filter
def even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(even,nums))
print(evens)

#filter,lambda
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)

#map with function
def update(n):
    return n*2
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(update,evens))
print(doubles)

#map without function
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
print(doubles)

# from functools import reduce
def add_all(a,b):
       return a+b
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
nums=reduce(lambda a,b:add_all,doubles)
print(doubles)
print(nums)


#without function
from functools import reduce
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
nums=reduce(lambda a,b:a+b,doubles)
print(doubles)
print(nums)


#magic number with define function
def is_magic_number(n):
    while n > 9:
        sum = 0
        while n > 0:
            d = n % 10
            sum += d
            n //= 10
        n = sum
    if n == 1:
        return "magic number"
    else:
        return "not magic number"
print(is_magic_number(121))

#neon number with def function
def neon(n):
    sq = n * n
    total = 0
    while sq > 0:
        digit = sq % 10
        total += digit
        sq //= 10
    if n == total:
        print("neon")
    else:
        print("not neon")
neon(10)  


#composite number
def composite(n):
    count = 0
    if n <= 1:
        print("not composite")
        return
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
            count += 1
    print()  
    if count > 2:
        print("composite")
    else:
        print("not composite")
composite(11)  

#perfect number
def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
           sum=sum+i
    if n==sum:
        print("perfect number")
    else:
        print("not perfect number")
perfect_number(145)

#googly number
def googly(n):
    sum=0
    while n!=0:
        d=n%10
        sum=sum+d
        n=n//10
        flag=0
        for i in range(2,sum):
            if sum%i==0:
                flag+=1
            if flag==0:
                print("googly")
            else:
                print("not googly")
googly(13)

#tail recursion(printing before function call)
def nums(n):
    if n==0:
        return 
    print(n,end="")
    nums(n-1)
n=int(input())
nums(n)

#head recursion(printing after function call)
def nums(n):
    if n==0:
        return 
    nums(n-1)
    print(n,end="")
n=int(input())
nums(n)

def nums(n):
    if n==0:
        return 
    if n==1:
        print(n,end="")
        return 
    print(n,end="")
    nums(n-1)
    print(n,end="")
n=int(input())
nums(n)

#find factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
       return factorial(n-1)*n
n=int(input())
print(factorial(n))


#palindrome
def palindrome(n,rev=0,temp=None):
    if temp is None:
        temp=n
    if n==0:
        return temp==rev
    return palindrome(n//10,rev*10+n%10,temp)
num=int(input())
print(palindrome(num))


#reverse integer using recursion
def reverse(n,res=0):
    if n==0:
        return res
    last_digit=n%10
    res=res*10+last_digit
    return reverse(n//10,res)
num=int(input())
print(reverse(num))
 
#perfect square
def perfect_sq(n):
    if n<0:
        return False
    root=int(n**0.5)
    return n==root*root
num=int(input())
print(perfect_sq(num))


#power of 2 or not
def power_of_two(n):
    if n==1:
        return True
    if n==0 or n%2!=0:
        return False
    return power_of_two(n//2)

num=int(input())
print(power_of_two(num))


#find power of two number
def power(a,b):
    if b==0:
        return 1
    return  a*power(a,b-1)
num1=int(input())
num2=int(input())
print(power(num1,num2))


