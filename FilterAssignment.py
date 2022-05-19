import functools
#Q3
lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
lst2 = list(filter(lambda x:x<0,lst1))
for i in range(len(lst2)):
    lst2[i]=abs(lst2[i])
print(lst2)

#Q4

lis = [1, 3, 5, 6, 2, ]
print(functools.reduce(lambda a, b: a * b, lis))

#Q5
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
lst3=zip(lst1,lst2)
print(dict(lst3))
