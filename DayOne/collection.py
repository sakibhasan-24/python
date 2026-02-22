#collection is a container that stores multiple items in a single variable

#list is a collection which is ordered and changeable. Allows duplicate members.

#tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#set is a collection which is unordered and unindexed. No duplicate members.

#dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#list
thislist = ["apple", "banana", "cherry"]


#access item
print(thislist[1])

#change item
thislist[1] = "blackcurrant"


#length
print(len(thislist))

#add item
thislist.append("orange")
print(thislist)

mixed=[1,"ad",True]
print(mixed)


letters=list("python")
print(letters)


#slice
print(thislist[2:5])