#module import test

import simpleset


print(dir())
print(simpleset)


a = [1,2,3]
b = [3,4,5]

print(simpleset.union(a,b))
print(simpleset.intersect(a,b))

