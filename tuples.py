#Immutable
mytuple=("Max",28,True,28)
print (mytuple)

name, age, honest, age = mytuple #number of variables should be equal to length of tuple
print(age)

i,*j,k= mytuple
print(i) #first element :Max
print(j) #all elements in the middle :[28, True]
print(k) #last element : 28

tppl=("ABCG")
print(type(tppl)) #string
#but
tppl=("ABCG",) #with comma
print(type(tppl)) #now type is tuple


item=tppl[0]
print(item)

if 28 in mytuple:
    print("yes")

print(len(mytuple)) #staarts from 1

print(mytuple.count(28)) #counts no.of times 28 occurs in the tuple

print(mytuple.index(28)) #gives the index of first occurence

#list to tuple
tppl1=tuple(["Max",28,False])
print(tppl1)


#tuple to list
mylist=list(tppl1)
print(mylist)

# tppl1=mytuple[:1]
# print(tppl1)

a=(1,2,3,4,5,6,7,8,9,10,11)

b=a[2:7]#excludes the last index
print(b) #(3, 4, 5, 6, 7)

b=a[::-1] #reverses the tuple
print(b)

#Conclusion: You can completely change a tuple but cannot ad to or sunsract from it 

import sys,timeit
my_list=[0,1,2,"hello",True]
my_tuple=(0,1,2,"hello",True)
print(sys.getsizeof(my_list),"bytes") #104 bytes
print(sys.getsizeof(my_tuple),"bytes") #80 bytes

print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000)) #took 0.03576870000688359 seconds to make this list 1000000 times

print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000)) #took 0.007316900009755045 seconds to make this tuple 1000000 times

#Conclusion: working with tuple is more memory and tiime efficient