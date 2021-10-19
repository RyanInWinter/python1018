#Function1.py

# 함수를 먼저 정의
def setValue(a):
	x = a
	print(x)

# 함수를 호출
result = setValue(5)
print(result)

def swap(x, y):
	return y, x

print(swap(5, 6))


#
def union(*ar):
	# 지역변수 
	result = []

	# 단어 슬라이싱
	for items in ar:
		
		# 각 글자를 슬라이싱
		for x in items:
			if x not in result:
				result.append(x)
	return result

#
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))