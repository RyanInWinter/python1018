#DemoDict.py
device = {"아이폰":5, "아이패드": 10, "윈도우":20}

print(device)
print(len(device))
print(device['아이폰'])
device['맥프레'] = 15
device['아이폰'] = 6
print(device)
del device['아이폰']

for item in device.items():
	print(item)

print('---key, value---')
for n, k in device.items():
	print(n, k)


phone = {'kim':1111, 'lee':2222}
p = phone
print(phone['kim'], phone['lee'])


# 교집합을 구하는 함수
def intersect(prelist, postlist):
	result = []
	for x in prelist :
		if x in postlist and x not in result : 
			result.append(x)
	return result

# 함수 호출
print(intersect("Ham", "Spam"))