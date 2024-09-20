# Functions & arguments
print("Python is great language")
print("String don't get executed as code")

# multiple lines
print('I want to be a Millionaire');\
    print('God is the greatest');\
        print('This life is Vanity') 

# new lines
print('Hi!, \nyou are beautiful')

# introducing keywords arguments
print('Hey', end='');\
     print('what is your name')
     
print('Hi', 'Excuse me', sep='!', end='!\n');\
    print('Hmmm', 'you are beautiful!!', sep=',', end='girl')


# OPERATORS
# exponentials
print(2 ** 10)
print(5** 50)
print(2 ** 3)

# multiplications
print(10 * 10)
print(8 * 6)

# division & floor division(returns outputs in nearest interger)
print(5 / 10)
print(3 / 8) 

print(7 // 12)
print(4 // -9)

# modulo (to calculate remainder)
print(4 % 2)
print(17 % 9)

# additions
print(5 + 8)
print(16 + 13)

# subtraction
print(5 - 4)
print(22 - 9)

print(2 * 3 ** 3 * 4)
print(2 * (2 + 3))
print(9 % 4)
print(13 / 4 + 13 % 4)
print(2 ** 3.)
print(10 - 6 ** 2 / 9 * 10 + 1)

x = 10 / 4
y = 5 / 2.0
print(x + y)

print(6. // 4)

# variables
rate_of_liter = 1000
amount_of_liter_to_get = 15
print(rate_of_liter * amount_of_liter_to_get) 

age = 22
AGE = 44

age /=2
print(age + AGE)

amount = 4
cost = 2
cost += 2
print(amount * cost)

y = 5
y = 'Jack'
print(y)

# inputs
print(int(15.5) - 10)

# strings operators (to repeat strings several times)
print('ha' * 5)
print(int('22'))
print(str(25))

x = 5 
y = 'Sally'
print(str(x) + y)

# comparsion operators
print('Hello!' == 'Hello!')
print('Hello!' == 'Goodbye!') 
print(2 != 2)
print(2 != 4)

rate_of_liter = 1000
amount_of_liter_to_get = 50
print(rate_of_liter > amount_of_liter_to_get)

min_score = 113
score = 113
print(score > min_score)
print(score <= min_score)

y = 7
x = 5
print(x !=y)

# conditional statement
age = int(input('How old are you?'))
if age >= 18:
    print('You are an adult')
    
one_dollar = int(input( 'How much is five dollar?'))
if one_dollar >= 1700:
    if one_dollar == 1700:
        print('you have enough!')
    else:
        print("you don't have enough")
        
if 4 + 5 == 10:
    print("True")
else:
    print('False')
print('True')

a = 3
if (a == 0):
    print('Am I here?')
elif (a == 3):
    print('or over here')
    
x = -10
if x < 0:
    print('The negative number', x, 'is not valid here.')
print('This is always printed')

q = 5
r = 10
if r < q:
    print('q is greater than r')
elif q == r:
    r = 5
    print('q and r are equal')
else:
    print('r is greater than q')
    
z = 0
e = 6 
f = 6
if e > 0:
    if f > 0:
        z = z + 6
    elif e > 6:
        z = z + 5
    else:
        z = z + 4
else:
    zip = z + 3
print(z)

# Loop functions
i = 1
x = 3
sum = 0
while (i <= x):
    sum += i
    i += 1
print(sum)

x = 0
while (x < 50):
    x+=2
print(x)

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1

i = 5
while True:
    if i % 0o11 == 0:
        break
    print(i)
    i += 1

x = 1
while (x <= 5):
    x += 1
    print(x)

i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2

i = 1
while True:
    if i % 0o7 == 0:
        break
    print(i)
    i += 1

x = 1
while (x < 20):
    x = x * 2
print(x)

x = 'abcd'
for i in x:
    print(i)
    x.upper()

x = 'abcd'
for num in range(5, 11):
    print(num)

x = 'abcd'
for i in range(len(x)):
    print(i)

x = 'abcd'
for i in range(len(x)):
    print('hello')

x = 'abcd'
for i in x:
    print(i.upper())

for num in range(0, 11):
    if num % 2 != 0:
        print(num)

# OPERATORS
is_hungry = True
if (not is_hungry):
    print('You are not hungry')
else:
    print('You are hungry')

is_hungry = False
if(not is_hungry):
    print('You are not hungry')
else:
    print('You are hungry')

x = 6
print(x > 4 and x < 12)

# bitwise operatotors
print(22 << 1)

x = 2
print(x << 4)

print(5 ^ 11)

print(int(1001))

a = 20
b = 5
print('a & b =', a & b)

x = 2
print(x << 2)

a = 20
b = 5
print('a | b =', a | b)

print(-200)

# List 
numbers = [1, 2, 3, 4, 5]
numbers[4] = 6
print(numbers[4])

list1 = [10, 11, 12, 13, 14]
print(list1[::3])

list1 = [1, 2, 3, 4, 5]
list1[0] = 10
print(list1)

# List methods
list1 = ['Go', 'Java', 'C', 'Rust']
print(min(list1))

ages = [56, 72, 24, 46]
ages.sort()
print(ages)

list1 = [4, 4, 3, 1]
list1.pop(2)
print(list1)

list1 = [10, 20, 30, 40, 50]
list1.append(60)
print(list1)

list1 = ['uk', 'india', 'Canada']
list1.insert(1,8)
print(list1)

num = [4, 4, 3, 1]
num.sort()
print(num)

list1=['Go', 'Java', 'C', 'Python']
print(max(list1))

# Iterating Lists
for x in [0, 2, 1, 3]:
    for y in [0, 4, 1, 2]:
        print('*')

for letter in 'KodeKloud':
    if letter == 'u':
        continue
    print('Letter : ' + letter)

sum = 0
values = [2, 9, 1, 7]
for number in values:
    sum +=  number
print(sum)

sum = 0
values = [2, 9, 1, 7]
for number in values:
    sum = sum +  number
print(sum)

list1 = [1, 2, 3, 4]
for i, j in enumerate(list1):
    print(i, j)

list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
    if len(i)==3:
        print(i)

letters = ['A', 'B', 'C', 'D', 'E']
print(letters[1:])

list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
    if len(i)==4:
        print(i)

list1 = [1, 2, 3, 4]
for index, j in enumerate(list1):
    print(index, j)

list1 = [4,0,7,1]
print(list1[::-1])

list1 = [10, 11, 12, 13, 14]
print(list1[::1])