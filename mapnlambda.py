
#Q1
i = lambda x,a,b,c : a*pow(x,2)+b*pow(x,1)+c*pow(x,0)
print(i(5,4,3,2))

#Q2
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

def count1(x):
    count=0
    for i in range(len(lst1)):
        count=count+lst1[i].count(x)
    return (count)

a=list(map(lambda x:count1(x), ["A","a"]))
print(a)