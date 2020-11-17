import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}[]()*;/,_-"

all = lower + upper + numbers + symbols

lenght = 34

password = "".join(random.sample(all, lenght))
print(password) 