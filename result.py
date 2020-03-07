import studentx
import maryo

x = studentx.a["code"]
y = studentx.b["code"]
z = studentx.a["student"]
print(x, ' ', y, ' ', z, ' ')

i = studentx.a["age"]
print(i)

k = studentx.a["mother"]
print(k)

l = studentx.b["student"]
print(l)

j = studentx.b["father"]
print(j)

for i in range(len(maryo.a)):
	print(i, maryo.a[i])