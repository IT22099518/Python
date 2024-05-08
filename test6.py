nic = input("Enter your NIC : ")

if len(nic) == 9 or len(nic) == 11:
    print(f'Your NIC has {len(nic)} numbers and it is valid')
else:
    print(f'Your NIC has {len(nic)} numbers and it is invalid')