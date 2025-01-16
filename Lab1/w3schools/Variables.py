x = y = z = 'Hello World'

x, y, z = "Orange", "Banana", "Cherry"

fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)

print('Hello', 'World')

a = 'Hello'
b = 'World'
print(a + b)

a = 4
b = 5
print(a + b)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print('Python is ' + x)