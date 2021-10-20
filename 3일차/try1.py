""" # try1.py

# 함수를 정의
def divide(a, b):
	return a/b

# 함수 호출
try : 
	result = divide(5, "aa")
	print("결과:{0}".format(result))
except ZeroDivisionError: 
	print("0으로 나누면 안됩니다.")
except TypeError : 
	print("숫자여야 연산이 됩니다.")
else : 
	print("결과:{0}".format(result))
finally : 
	print("무조건 실행")


print("전체 코드 실행 종료")
 """

# 함수를 정의
def mydivide(a, b):
	result = 0
	try : 
		result = a/b
	except ZeroDivisionError: 
		print("0으로 나누면 안됩니다.")
	except TypeError : 
		print("숫자여야 연산이 됩니다.")
	finally : 
		print("무조건 실행")
		print("결과:{0}".format(result))
	
mydivide(2, 0)

