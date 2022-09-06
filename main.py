def addNum():
	a = input("First Number: ")
	b = input("Second Number: ")
	try:
		print(int(a)+int(b))
	except:
		print("Enter a number pls")

def main():
	print("Hello!")
	addNum()

main()
