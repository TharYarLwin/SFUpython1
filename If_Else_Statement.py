If_Else_Statement.py

#Boolean Expression -> True or False

print(20 > 10)
print(20 == 10)
print(bool("Hello World"))
print(bool(20))

Python Conditions

Equals                    -> x == y
Not Equals                -> x != y
Less than                 -> x <  y
Less than or equal to     -> x <= y
Greater than              -> x > y
Greater than or equal to  -> x >= y
Boolean OR                -> x or y , x | y 
Boolean AND               -> x and y, x & y
Boolean NOT               -> not x

if -
else -

#If Statement

x = 70
y = 60

if x > y:
	print("x is greater than y")

>>> if x > y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is greater than y
>>> if x < y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is not greater than y

#Elif

x = 70
y = 70

>>> if x > y:
...     print("x is greater than y")
... elif x >= y:
...     print("x is greater or equal to y")
... elif y < x:
...     print("y is smaller than x")
... else:
...     print("x is nothing")
...
x is greater than y

#Short Hand If

if x > y: print("x is greater than y")


>>> x = 50
>>> y = 150
>>> if x > y: print("x is greater than y")
... elif x == y: print ("x and y are equal")
... else: print("x is less than y")
...
x is less than y
>>>


print(x) if x > y else print(y)

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y and z > x:
...     print("All Conditions are True")
...
All Conditions are True
>>> if x < y and z > x:
...     print("All conditions are True")
... else:
...     print("Some conditions are false")
...
Some conditions are false


#Nested if is if statements in if statements
 x = 50

 if x > 10:
 	print("x is ten")
 	if x > 20:
 		print("x is greater than 20")
 	else:
 		print("No,x is not greater than 20")

 if x > 10 and x != 10 or x > 20:
 	print("x is greater than 10 and 20")
 else:
 	print("x is not greater than 10 & 20")

if student
	if batch
		if gender
else 
	not

student = "SFU"
	batch = "3"
		gender = "male"