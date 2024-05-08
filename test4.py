
a = input("Enter your birth year : ")
b = input("Enter last 7 digits of your NIC : ")
print('Your NIC number is : ' + a[2:] + b + "V")

# using formated string
print(f'Your NIC number is : {a[2:]}{b}V')