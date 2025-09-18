#running sum of 1d array
nums=[1,2,3,4]
sum=0
for i in nums:
    sum+=i
    l1=sum
print(sum)


#largest elemnet
a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            max=a[i]
print(max)


#even odd withou modulus remainder
num=int(input())
if num&1==0:
    print("even")
else:
    print("odd")



#swap without temp
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a,b)

#xor operation n=10 1^2^3^4^.....
def xor(n):
   if n%4==0:
     return n
   if n%4==1:
     return 1
   if n%4==2:
      return n+1
   if n%4==3:
      return 0
n=int(input())
print(xor(n))

#left to right xor operation
def xor(n):
     if n%4==0:
       return n
     if n%4==1:
       return 1
     if n%4==2:
       return n+1
     if n%4==3:
       return 0
l,r=map(int,input().split())
a=xor(r)
b=xor(l-1)
print(a^b)
