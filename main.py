# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class StringClass():
    # Use a breakpoint in the code line below to debug your script.

    def __init__(self):

        self.str1 = ""

    def getlen_String(self):
        self.str1 = "12314532"

        return len(self.str1)

    def Convert_list(self):
        li = list(self.str1)
        self.li=li

        return li

class PairsPossible(StringClass):
    def __init__(self):
        super().__init__()

    def storePairs(self):
        output = []
        self.li = str1.Convert_list()
        n=len(self.li)
        for i in range(0,n):
            for j in range(i,n):
                if (i != j):
                    output.append((self.li[i]+" "+self.li[j]))
            #output.append(self.li[i])
        return output
    def printPairs(self):
        self.output=pairs.storePairs()
        print("All possible pairs of list")
        print(self.output)

class SearchCommonElements():
    def common_elements(self):
        self.str2="456"
        self.list2=list(self.str2)
        self.d = {}
        self.li=str1.Convert_list()
        for index, value in enumerate(self.list2):
            self.d[index] = value
        print("Dictionary of the list :")
        print(self.d)
        res = [ele for ele in self.li if ele in self.d.values()]
        print("commmon elements : " + str(res))


class EqualSumPairs():
    def __init__(self):
        self.sum1 = []
        self.list1 = []
        self.uniquesum = []
        self.out = pairs.storePairs()
        for i in range(0,len(self.out)):
            self.list1=(self.out[i]).split()
            for j in range(0,len(self.list1)):
                self.list1[j] = int(self.list1[j])
            self.sum1.append(sum(self.list1))
        print("Sum of all possible pairs")
        print(self.sum1)
        count=0
        for i in range(len(self.sum1)):
            for j in range(len(self.sum1)):
                if(self.sum1[i]==self.sum1[j]):
                    count=count+1
            if(count==1):
                self.uniquesum.append(self.sum1[i])
            count=0
        #new_set = set(self.sum1)

        print("count of unique sum of pairs is:", len(self.uniquesum))



str1 = StringClass()
pairs = PairsPossible()
common= SearchCommonElements()
equalsum=EqualSumPairs()
print("length of the string")
print(str1.getlen_String())
print("String converted to list")
print(str1.Convert_list())
pairs.printPairs()
common.common_elements()
equalsum.__init__()




