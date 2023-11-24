#Implicit conversion
a = 2
b = 3.125
c = 1+3j
d = 35
print(a+b , type(a+b))
print(a+c , type(a+c))
print(a+d , type(a+d))

#Explicit Conversion
e = '14.254'
e = float(e)
print(e+d , type(e+d))

#Operators
#f += b
#print(f) #an error occurerd not defined
f = d*a #arthimetic oparators
g = a+c #arthimetic oparators
print(g) #arthimetic oparators
print(f)
h = f/d #arthimetic oparators
print(h, type(h))
i = g**h #arthimetic oparators
print(i, type(i))
j = f//h #arthimetic oparators
print(j, type(j))
print(a>b) #comparision operators
print(j==i) #comparison operator (false)
print(a==h) #compasion operator (true)
a += h #additional operator = a + h
print(a) 
h -= a  #subtractional operator = h - a
print(h, type(h))
print(a<b) #logical operator used to make decision (true or false output.)
g *= 3  #multiplication assignment operator = g * 3
f /= g #division assignment operator = f / g
print(g)
print(f , type(f)) # (3.888888888889 - 3.8888888889j) <class complex) answer to cell 37
k = 20000
l = '50'
l= int(l)
m = k / l
print(m, type(m)) # m = 400.0 <class float)
m = int(m)
n = m + l
print(n, type(n))

print(o, type(o))

print(p , type(p))
print(n)
print(min(50,100,120))
#o = input('name of the company') #adding input in a variable
#p = input('time of stay since employment')