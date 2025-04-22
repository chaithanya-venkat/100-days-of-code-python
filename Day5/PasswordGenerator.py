import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("how many letters do you want in your password? "))
nr_numbers = int(input("how many numbers do you want in your password? "))
nr_symbols = int(input("how many symbols do you want in your password? "))

password_list = []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for number in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

for symbol in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(f"the password is {password}")