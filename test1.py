# variables
# Integer
from builtins import print

x = 2
print(x)
x = 3
print(x)
x = x + 6
print(x)

# -------------------------------------------------------

# Strings
a = 'pasindu'
abc = 60
print(type(abc))
done = True  # boolean
abc_number = 40
t = abc + abc_number
print(t)

# ------------------------------------------------------------

# get inputs
# name = input('What is your name : ')
# print(name)
# print('Hellooo ' + name)

# -----------------------------------------------------------------

# Strings
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(s[0])
print(s[-1])
print(s[3:])
print(s[:-4])

# ------------------------------------------------------------------

# formated Strings
fname = "Nuwani"
sname = "Sithara"

print("My name is " + fname + " " + sname)

v = f'My name is {fname} {sname}'  # Formated strings

print(v)

# -----------------------------------------------------

# String methods
msg = "Welcome to Python"
c = len(msg)
print(c)
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.find('to'))
print(msg.replace('Python', 'Java'))
print('Welcome' in msg)
print('blah' in msg)

# ------------------------------------------------------

# Arithmetics
x = 20 / 3
y = 20 // 3
print(x)
print(y)

# -----------------------------------------------------

# B O D M A S
a1 = (3 + 4)
a2 = 3 ** 4  # Power(3^4)
a3 = 3 * 4
a4 = 3 / 4
a5 = 3 + 4
a6 = 3 - 4

print(4 ** 5 - (5 ** 5 + 7) / 6)
