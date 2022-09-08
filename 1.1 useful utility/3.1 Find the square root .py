# Find square root of real or complex numbers
# Importing the complex math module
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
# In this program, we use the sqrt() function in the cmath (complex math) module.

# Notice that we have used the eval() function instead of float() to convert complex numbers as well. Also, notice the way in which the output is formatted.

# Look here for more about string formatting in Python.