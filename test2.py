# Calculate Age

name = input('Enter your name : ')
b_year = input('Enter your birth year : ')

# convert b_year to integer
t = int(b_year)

age = 2024 - t

# age = 2024 - int(b_year)

print(name + ', Your are ' + str(age) + ' years old.')
