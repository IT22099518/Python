phone = input('Enter phone number : ')
if len(phone) == 10:
    print('Number is correct')
else:
    b = 10 - len(phone)
    print(str(b) + ' numbers/s are missing')


# -----------------------------------------------

num = input('Enter your phone number : ')
len_num = len(num)
num_left = 10 - len_num
print(f'{num_left} number/s are missing!')

