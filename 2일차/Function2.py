#Function2.py

def userURIBuilder(server, port, **user):
	strURL = "http://" + server + ":" + port + "/?"
	for key in user.keys():
		strURL += key + '=' + user[key] + '&'

	return strURL

print(userURIBuilder("naver.com", "80", id="kim", password="1234"))

print(globals())

#람다함수
g = lambda x, y : x*y
print(g(3, 4))
print((lambda x:x*x)(3))
print(globals())