numbers = [3,5,1,4,2]
a = []
for i in range(0, len(numbers)):
    numbers[i] = str(numbers[i])
    a.append(numbers[i])
b = ''.join(a)
c = []
for i in b:
    c.append(int(i))
c.sort()
e = []
for i in range(0, len(c)):
    c[i] = str(c[i])
    e.append(c[i])
print(int(''.join(e)))
        
