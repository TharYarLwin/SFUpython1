#Loops

loop.py

-While Loops
-for Loops

Condition is true, while loop execute a set of statements

x = 1
while x < 7:
 	print(x)
 	x += 1


 
while loop require variable ready.

x = 50
while x < 100:
	print(x)
	if x == 5:
		break
	x += 5

For Loops

#for loop is iterating over a sequence

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)

#Looping in a String

for x in "pineapple":
	print(x)

#The break Statement

#stop after condition

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)
	if x == "pineapple":
		break

-------

#stop before condition

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	if x == "pineapple":
		break
	print(x)

#the continue statement - stop the current iteration

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	if x == "pineapple":
		continue
	print(x)

#the range () function - a set of code a specified number of times

for x in range(10):
	print(x)

for x in range(10, 100):
	print(x)

for x in range(10, 100, 5):
	print(x)

#Nested loops

NumberA = [1,2,3,4,5]
NumberB = [1,2,3,4,5]
NumberC = [1,2,3,4,5]

for x in NumberA:
	for y in NumberB:
		for z in NumberC:
			print(x,y,z)

#Pass

for x in [1, 2, 3, 4, 5]:
	if x == 3:
		pass
	print(x)

-------

words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))

-----

for n in range(2, 21):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equal', x, '*', n//x)
			break
	else:
		#loop fell through without finding a factor
		print(n, 'is a prime number')

-----

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
		num +=10
		print("Number is", num)
	print("Found a number", num)

-----

