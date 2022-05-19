#Q1

l=[[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

for i in l:   #getting each individusal list
    #print(l1)
    new_dict, new_list = {}, {}

    for j in i:
        if not j in new_dict:
            new_dict[j] = 1
        else:
            new_dict[j] += 1
    for key, values in new_dict.items():
        if values > 1:
            new_list[key]=values
    print(new_list)

#Q2
lst1=["Hello","take"]
lst2=["Dear","Sir"]
lst3=[]
for i in range(len(lst1)):

    for j in range(len(lst2)):
        lst3.append(lst1[i]+lst2[j])

print(lst3)

#Q3
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2=["h", "i", "j"]
for i in range (len(list2)):
    list1[2][1][2].append(list2[i])

print(list1)

#Q4
keys = ["Ten","Twenty","Thirty"]
value = [10,20,30]
dicts={}
if (len(keys)==len(value)):
    for i in range(len(keys)):
        dicts[keys[i]] = value[i]
    print(dicts)

#Q5
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3={}
dict3 = dict1.copy()
dict3.update(dict2)

print(dict3)

#Q6
sampleDict = {  "name": "Kelly",  "age":25, "salary": 8000, "city": "New york" }
sampleDict.pop("city")
dict={"Location":"New york" }
sampleDict.update(dict)
print(sampleDict)

#Q7
color_dict = {"HuEx":[1, 3, 4], "is": [7, 6], "best": [4, 5]}
result = []
for key, val in color_dict.items():
    result.append([key] + val)

print(result)