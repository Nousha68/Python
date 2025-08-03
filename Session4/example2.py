a=[2,5,8,4,3,6,12,98]
print(a)
print(type(a))
print(a[0])
print(a[7])
print(a[-2])
print(a[:3])
print(a[0:3])

print(a[3:])

print(a[2:5])
print(a[::2])
print(a[::3])
print(a[1::2])
print(a[-1::-1])
a.append(12)
print(a)
a.remove(12)
print(a)
b=a.pop()
print(a)
print(b)
del a[2]
print(a)
a.insert(5,80)
print(a)
print(a.index(80))
if 10 in a:
    print(a.index(10))
else:
    print("10 is not available in a")
a.sort(reverse=True)
print(a)
a.reverse()
print(a)
a.clear()
del a
print(a)