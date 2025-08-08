"""name=["ranbir","anil","amithab","dharmenthra"]
sal=[20000,50000,100000,150000]
dic={}
for i in range (len(sal)):
    k=sal[i]+sal[i]*15/100
    dic[name[i]]=k
print(dic)"""    
#task2
"""name=["milkymist","leys","sunfist","goodday","wondercake"]
food=[]
for i in range (len(name)):
    if len(name[i])>=6:
         food.append(name[i])
print(food)"""         
#task3
"""s={111,2222,33333,5555,55}
dic={}
lst=list(s)
for i in range(len(s)):
    dic[i]=len(str(lst[i]))
print(dic)"""    
#list comprihension
"""print([i for i in range (1,11)])"""
#square comprihension
"""n=[1,2,4,5,6]
for i in n:
    print(i**2)    
m=([i**2 for i in n])    
print(m)"""
#only for and if condition
"""l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
print(l1)"""
#if..else..for
#normal type
"""l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i**2)
    else:
        l1.append(i**3)
print(l1)"""        
        #or
"""l=[1,2,3,4,5,6,7,8,9,10]
print([i**2 if i%2==0 else i**3 for i in l])"""
#nested list coprihension
#normal type
"""m=[]
for i in range (5):
    m.append([])
    for j in range (5):
        m[i].append(j)
print(m)"""        
        #or
    
"""m=[[j for j in range (5)] for i in range(5)]
print(m)"""
#nested if coprihension
"""l=[-1,-2,-3,1,2,3,4,5,6]
b=[]
for i in l:
    if i>0:
        if i%2==0:
            b.append(i)
print(b) """          
            #or
        
l=[-1,-2,-3,1,2,3,4,5,6]
print([i for i in l if i>0 if i%2==0])
