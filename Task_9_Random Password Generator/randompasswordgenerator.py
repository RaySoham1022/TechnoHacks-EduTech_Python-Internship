import random
import string

lowercaseletters = string.ascii_lowercase
uppercaseletters = string.ascii_uppercase
numbersdigits = string.digits
specialpuncsymbols = "@$#&*"
masterstring = numbersdigits + lowercaseletters + uppercaseletters + specialpuncsymbols

print('\nPassword Generator')
print("-------------------")

passlength = int(input('\nEnter Your Password Length : '))

var = random.sample(masterstring, passlength)

final_password = "".join(var)

print("Your Password can be : " , final_password , "\n")