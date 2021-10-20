#DemoFile.py

# 파일쓰기
""" f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번쨰라인\n두번째\n세번째\n")
f.close()
print(f.closed)

if f.closed == True :
	print("파일이 정상 종료")
else :
	f.close() """

""" f = open("c:\\work\\demo.txt", "rt", encoding='utf-8')
print(f.read())
print(f.tell())
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")
f.seek(0)
result = f.readlines()
print(result)
f.close()

for item in result : 
	print(item.replace("\n", ""))
 """
	
""" # 기존 파일에 첨부
f = open("c:\\work\\demo.txt", "a+", encoding='utf-8')
f.write("새로운 데이터\n")
f.close()

f = open("c:\\work\\demo.txt", "rt", encoding='utf-8')
print(f.read())
f.close() """

# 새로 덮어쓰기가 되기 떄문에 wt 사용에 조심
f = open("c:\\work\\demo.txt", "wt", encoding='utf-8')

print(f.read())
f.close()

