#count of digits and alphabets
s=input()
ca=0
cd=0
for i in s:
    if i.isalpha():
        ca+=1
    if i.isdigit():
        cd+=1
print(ca,cd)


#find the count of vowels and consonants in string
s=input()
v='a','e','i','o','u','A','E','I','O','U'
cv=0
cc=0
for i in s:
    if i in v:
        cv+=1
    if i not in v:
        cc+=1    
print(cv,cc)

#replace space with -
s=input()
s=s.replace(" ","-")
print(s)


#without replace
s=input()
s1=""
for i in s:
    if i.isspace():
        s1+="-"
    else:
        s1+=i
print(s1)

#capitalize
s=input()
s=s.title()
print(s)

#without title
s=input()
s1=s.split()
res=''
for i in s1:
    cap=i[0].upper()+i[1:]
    res=res+" "+cap
print(res)
    
#reverse a string without slicing
s=input()
s1=""
for i in s:
    s1=i+s1
print(s1)



#length of longest word in a sentence
s=input()
l=s.split() 
length=0
lword=""
for i in l:
    if len(i)>length:
        length=len(i)
        lword=i
print(length)
print(lword)


#palindrome
s=input()
if s==s[::-1]:
    print("palindrome")
else:
    print("not")

#most frequent character in word
s=input()
max_char=""
max_c=0
for char in s:
    count=s.count(char)
    if count>max_c:
        max_c=count
        max_char=char
print(max_c,max_char) 

#or
s=input()
freq={}
for char in s:
    if char not in freq:
        freq[char]=1
    else:
        freq[char]+=1
m=max(freq.values())
for i in freq:
    if freq[i]==m:
        print(i)


# #remove duplicates
s=input()
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)

#password validate(how many condidtions are not satisfied)
p=input()
l=len(p)
uc,lw,lwc,dc,spc,cc=1,1,1,1,1,0
freq=0
sp_count=0
sc='@','$','#','%','^'
for i in range(len(p)):
    if len(p)>=6 and len(p)<=22:
        lwc=0
    if p[i].isupper():
        uc=0
    if p[i].islower():
        lw=0
    if p[i].isdigit():
        dc=0
    if i+1<l and p[i]==p[i+1]:
        cc=1
    if p[i] in sc:
        sp_count+=1
    if sp_count>=2:
        spc=0
freq+=uc+lw+lwc+dc+cc+spc
print(freq)

#palindrome
s="malayalam"
i,j=0,len(s)-1
while i<=j:
    if s[i]!=s[j]:
        print("false")
        break
    i+=1
    j-=1
else:
    print("True")
              
    
