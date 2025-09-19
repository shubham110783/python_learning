print('Shubham is my name', 'My age is 42.')
#print("My age is 42.")
fruits = ["apple", "banana", "grapes",3]
print(type(fruits))
x,y,z ,a = fruits
print(x,y,z,a)
print(type(x))

x = 'awesome'
def myfunc():
    x = 'fantastic'
    print("Python is " + x)

myfunc()
print("Python is " + x)


x = ('apple','banana')
print(type(x))

x = {"name": "john", "age": 36}
print(type(x))

x = True
print(type(x))

x = complex(1j)
print(type(x))


x = "Hello World"
print(x[-5])
for i in x:
    print(i)

print(len(x))

txt = "The best things in life are free!"
print("Free" in txt)

if "Free" in txt:
    print("Yes, free is available")
elif "free" not in txt:
    print("No")


b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-1])
print(b[-5:-2])

a = "Welcome"
print(a[3:5])