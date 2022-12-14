a="hello"
b="world\n welcome"
dict = {104:110}

def fun(a,b):
	print(a.zfill(10))
	print(a.upper())
	print(a.translate(dict))
	print(b.title())
	print(b.swapcase())
	print(b.strip())
	print(a.startswith("he"))
	x=a.strip()
	print("welcome to",x,"world")
	txt = "Thank you for the music\nWelcome to the jungle"
	x = txt.splitlines()
	print(x)
	x=a.rstrip()
	print("hi welcome to",x,"python")
	txt = "cprog, python, c++"
	x = txt.rsplit(", ")
	print(x)
	txt = "I am learning python all day, python is one of the language"
	x = txt.rpartition("python")
	print(x)
	x = a.rjust(20)
	print(a, "is my favorite prog.")
	x=b.rindex("lco")
	print(x)
	x=b.find("welcome")
	print(x)
	x=b.replace("welcome","new")
	print(x)



fun(a,b)




