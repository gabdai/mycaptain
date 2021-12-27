print('choose the operation you want to perfrom :')
print('1. addition \n2. substraction .\n3. power of \n4. multiplication\n5. division')
n=int(input('enter your choice'))
if n == 1 :
    a = float(input('please enter the first number a :'))
    b = float(input('please enter the second number b :'))
    z = a + b
    print("sum of a and b is :",z)
elif n == 2 :
    a = float(input('please enter the base number a :'))
    b = float(input('please enter the exponent number b :'))
    z = a - b
    print("substraction of a and b is :",z)
elif n == 3 :
    a = float(input('please enter the first number a :'))
    b = float(input('please enter the second number b :'))
    z = a ** b
    print("power of a raised to b is :", z)
elif n == 4 :
    a = float(input('please enter the first number a :'))
    b = float(input('please enter the second number b :'))
    z = a * b
    print("multiplication of a and b is :", z)
elif n==5 :
    a = float(input('please enter the first number a :'))
    b = float(input('please enter the second number b :'))
    z = a/b
    print("division of a a divided by b is :", z)
else:
    print("sorry! I'm incapable doing this task!")
print('thank you for using me.')
