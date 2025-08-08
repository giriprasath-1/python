
"""def function(n):
    k=('a','e','i','o','u')
    for i in range(len(n)):
        if n[i][0] in k and n[i][-1] in k:
            yield i,n[i]
print(tuple(function(('apple','ball','ego'))))"""
"""a=(list(input().split()))
def fun(a):
    for i in range(len(a)):
        if a[0][0] in'aeiou'and a[0][-1] in 'aeiou':
            yield (i,a[i])
print(tuple(fun(a)))"""        
a=[1,2,3,4,5]
def fun(a):
    for i,j in enumerate(a):
        yield j**i
print(list(fun(a)))            
