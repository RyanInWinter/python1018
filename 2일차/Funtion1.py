""" 

def getBiggerThan20(i) : 
			return i > 20

iterL = filter(getBiggerThan20, lst)

for item in iterL : 
	print("Item:{0}".format(item))
 """
""" lst = [1,2,3,4,5]

for item in map(lambda i:i+10, lst): 
	print(item) """

lst = [10, 25, 30]
for item in map(lambda i:i>20, lst):
	print(item)
""" 
iterL = filter(lambda i:i>20, lst)
for item in iterL : 
	print("Item:{0}".format(item)) 
		

	
	
	
 """