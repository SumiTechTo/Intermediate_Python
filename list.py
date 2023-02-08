#                          STRING LIST 
mylist=["banana","cherry","apple"]
print(mylist)
mylist2=[5,True,"apple"] #list can contain items of various types 
print(mylist2)

item=mylist[1] #to access the item in a list 
#list begins with 0
item=mylist2[-1] #refers to last item in a list 
item=mylist[-2] #second last element

#iterations in a list 
for i in mylist:
    print(i)

#in syntax for list
if "cherry" in mylist: #even if you put "cherry  " it will give you a no
    print("yes")
else:
    print("no")

print(len(mylist)) #counting starts from 1

#to add item in a list
mylist.append("guava")

#to add to a perticular position 
mylist.insert(0,"lemon")

print(mylist)

a=mylist.pop() #gives the last element and also removes it from the list
a=mylist.remove("cherry") #removes a specific element
#if element is not present it gives a value error
print(mylist)

mylist.clear()
print(mylist)


#                       INTEGER LIST
num=[5,-4,-3,0,9]
# item=num.sort() #sorts in ascending order


#if you son't want to sort the actual list
item=sorted(num)
print(num) #[5, -4, -3, 0, 9]
print(item) #[-4, -3, 0, 5, 9]

#shortcut
item=[0]*5
print(item)

item2=[8,4,7,3,7,9,6]
new_list=item+item2 #concatenates the lists
print(new_list)

#slicing
mylist=[1,2,3,4,5,6,7,8,9,10]
item=mylist[1:5] #these are indexes which starts from 0
#it excludes the element in the last index
#so if you want to print from index 5 to 9 give
#item =mylist[5:10]

item=mylist[:5:2] #[start_index:stop_index:skips]

#reversing a list using indexes
item=mylist[::-1]

#how to not copy a list
list_copy=mylist
#if you do this noth the variables point to the same memory locations
#that means that modifying ;ist_copy will also modify mylist

#thus copy like this
list_copy=mylist.copy()
#or
list_copy=list(mylist)
#or 
list_copy=mylist[:]


#                         LIST COMPREHENSION
mylist=[1,2,3,4,5,6]
b=[i*i for i in mylist]

print(mylist) #[1, 2, 3, 4, 5, 6]
print(b) #[1, 4, 9, 16, 25, 36]

