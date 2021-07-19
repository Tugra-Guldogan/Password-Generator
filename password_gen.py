import random

numbers = ['1','2','3','4','5','6','7','8''9','0']
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
characters = ["#","!","@","$","%","^","&","*","(",")","-","_","/",":",":","{","}","[","]","+","="]
l = random.choice(small)
x = random.choice(letters)
y = random.choice(numbers)
z = random.choice(characters)
sq = 0
num = 0

q = random.choice(small)
w = random.choice(letters)
e = random.choice(numbers)
r = random.choice(characters)

t = random.choice(small)
u = random.choice(letters)
i = random.choice(numbers)
o = random.choice(characters)

p = random.choice(small)
g = random.choice(letters)
h = random.choice(numbers)
j = random.choice(characters)

m = (input('Press enter to continue :'))

num= random.randint(0,99)

if num<100:
    if num%2==0:
        sp= random.choice(numbers)
        jd = random.choice(characters)
        print("Your password : ",l+x+y+z+q+w+e+r+t+u+i+o+p+g+h+j+sp+jd)

    else:

       print("Your password : ","h",l+x+y+z+q+w+e+r+t+u+i+o+p+g+h+j+l+q+w+r+t+u+y)

elif num>100:
    if num % 2 == 0:
        io= random.choice(characters)
        pk = random.choice(characters)
        print("Your password : ", l + x + y + z + q + w + e + u + i + o + p + g + h + j + pk + io)

    else:
        gh= random.choice(numbers)
        ab = random.choice(letters)
        print("Your password : ", l + x + y + z + q + w + e + u + i + o + p + g + h + j + gh+ ab)

else:
    uh = random.choice(numbers)
    ib = random.choice(letters)
    print("Your password : ", l + x + y + z + q + w + e + u + i + o + p + g + h + j + uh + ib + t + h + q + l + j)
