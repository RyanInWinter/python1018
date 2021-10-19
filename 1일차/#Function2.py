#Function2.py

#def change(x):
#	x[0] = "H"

wordlist = ["J","A","M"]
#change(wordlist)
#print(wordlist)


def change(x):
	x1 = x[:]
	x1[0] = "H"

	print(f"함수 내부 : {x}")

change(wordlist)
print(wordlist)
