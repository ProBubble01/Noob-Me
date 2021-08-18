fif = open("The_mighty_IF.py", "w")
fif.write('''k = int(input("enter your number:" ))''')
for i in range(100000000):
    fif.write(f'''\nif k == {i}:\n    if k%2 == 0:\n        print("number is even")\n    else:\n        print("number is odd")''')
fif.close
