w = input("input weight vector: " )
w = [ float(weight) for weight in w.split(" ") ]
print(w)


x = input("input x vector: " )
x =  [ float(i) for i in x.split(" ") ]
print(x)

#n = float(input("input eta values"))
n = .1

y = float(input("guess gotten"))
t = int(input("t wanted"))


for i in range(0,len(w)):
	if(t == 1):
		neww = w[i] - n*(y - t)*x[i]
	else:
		neww = w[i] + n*(y - t)*x[i]
		
	print(neww)

