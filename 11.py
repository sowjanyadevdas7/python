def listfun():
	print("Methods in the list")
	list1=['apple', 'banana', 'orange', 'grapes', 'pineapple', 'mango']
	print("Elements in list1 ",list1)
	list1.append('avacado')
	print("Appending 'avacodo' to the list",list1)
	list1.insert(2,'cherry')
	print("Inserting 'cherry' at second position",list1)
	list2=['tomato', 'potato', 'onion', 'chilli', 'beetroot', 'carrot']
	print("Elements in list2 ",list2)
	list2.extend(list1)
	print("Extending the list by adding to another list",list2)
	print("Counting in list",list1.count('orange'))
	print("Length of the list", len(list1))
	print("Element at the index of 5",list1.index('grapes'))
	print("Sorting lists",list1.sort())
	list1.remove('banana')
	print("Removing an element from list",list1)

def tuplefun():
        print("Methods in tuples")
	tuple1=('apple', 'banana', 'orange', 'grapes', 'pineapple', 'mango')
	print("Elements in the tuples1",tuple1)
	tuple2=('tomato', 'potato', 'onion', 'chilli', 'beetroot', 'carrot')
	print("Elements in the tuples2",tuple2)
	print("Concatenation of two tuples",tuple1+tuple2)
	tuple3 = (tuple1,tuple2)
	print("Nesting of tuples",tuple3)
	tuple4=('welcome to supermarket')*5
	print("Repetition in tuples",tuple4)
	print("Slicing in tuples",tuple1[::-1])
	print("Slicing in tuples",tuple1[2:4])
	print("Length of tuple3",len(tuple3))
	list1=[0,1,2]
	print("Printing the list elements",list1)
	print("Converting list into tuple",tuple(list1))
listfun()      
tuplefun()
