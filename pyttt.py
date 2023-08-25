Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=4
y=7
print(x+y)
11
print(x-y)
-3
print(x*y)
28
print(x/y)
0.5714285714285714
print(x&y)
4
print(x**y)
16384
print(x//y)
0
print(x%y)
4

#ASSIBNMENT OPERATORS

x=5
x +=3
print(x)
8
x=5
x -=3
print(x)
2
x=5
x *=3
print(x)
15
x=5
x /=3
print(x)
1.6666666666666667
x=5
x %=3
print(x)
2
x=5
x //=3
print(x)
1
x=5
x **=3
print(x)
125
x=5
x |=3
print(x)
7
x=5
x ^=3
print(x)
6
x=5
x <<=3
print(x)
40
x=5
x >>=3
print(x)
0

#COMPARSION OPERATORS

x=3
y=5
print(x==y)
False

print(x !=y)
True

print(x>y)
False
 print(x<y)
 
SyntaxError: unexpected indent
print(x<y)
True

print(x<-y)
False

print(x<=y)
True

print(x>=y)
False

#LOGICAL OPERATORS

X=4

x=4
print(x>3 and x<9)
True
print(x>3 and x<3)
False

print(x>3 or x<9)
True
print(x>3 or x<3)
True

print(not(x>3 and  x<5))
False
>>> 
>>> #IDENTITY OPERATORS
>>> 
>>> x=["tree","root"]
>>> y=["tree","root"]
>>> z=x
>>> print(x is y)
False
>>> print(x is z)
True
>>> print(y is z)
False
>>> 
>>> print(x is not y)
True
>>> print(x is not z)
False
>>> print(y is not z)
True

#MEMBERSHIP OPERATORS

x=["free"]
print("free" in x)
True

x=["green","red"]
print("yellow" in x)
False

print("green" is x)
False

print("red" in x)
True

print("red" not in x)
False
print("blue" not in x)
True

#BITWISE OPERATORS

print(6&3)
2
print(6|3)
7
print(6^3)
5
print(6~3)
SyntaxError: invalid syntax
print(~3)
-4
print(3<<2)
12
print(6>>2)