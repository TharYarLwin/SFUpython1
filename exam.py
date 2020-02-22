x = int(input("Please enter exam result: "))

if x < 101 and x > 89 or x == 100:
	print("A")

if x < 89 and x > 79 or x == 90:
	print("B")

if x < 79 and x > 59 or x == 80:
	print("C")

if x < 59 and x > 49 or x == 60:
	print("D")

if x < 49 or x == 49:
	print("F")