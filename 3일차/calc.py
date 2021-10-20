class myclass:
	def __init__(self, *ar):
		mylist = []

		for n in ar:
			mylist.append(n)
		
		self.mylist = mylist

	def sumdata(self):
		sum_result = 0

		for n in self.mylist:
			sum_result += n

		return sum_result


b = myclass(4, 2, 3)
print(b.mylist)
print(b.sumdata())