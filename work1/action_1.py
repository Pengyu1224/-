#求2+4+6....+100的和
#方法1
s1=0
for i in range(2,101,2):
    s1+=i
print(s1)
#方法2
s2=sum(range(2,101,2))
print(s2)