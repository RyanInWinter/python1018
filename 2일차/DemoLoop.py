# DemoLoop.py

lst = list(range(1, 11))

for item in lst: 
	if item > 5 : 
		break
	print("item:{0}".format(item))

for item in lst : 
	if item % 2 == 1 : 
		continue
	print("item:{0}".format(item))


lst = list(range(1, 11))
print([i**2 for i in lst if i > 5])

d = {100:"apple", 200:"orange"}
print([v.upper for v in d.values()])