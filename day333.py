h = open("demo.txt","r")
data = h.read()
print(data)

line1 =h.readline()
print(data)

line2 =h.readline()
print(line2)

data.colse()