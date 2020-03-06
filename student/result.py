
import student
import mary

x = student.a["code"]
y = student.b["code"]
z = student.a["student"]
print(x, ' ', y, ' ', z, ' ')

i = student.a["age"]
print(i)

k = student.a["mother"]
print(k)

l = student.b["student"]
print(l)

j = student.b["father"]
print(j)

for i in range(len(mary.a)):
	print(i, mary.a[i])



