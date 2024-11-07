print('תנאים:')
print('5:')
while True:
    try:
        f: int = int(input('enter a 4-digit number:'))
        if f <= 999 or f >= 9999:
            print('not a 4-digit number')
            continue
        else:
            break
    except ValueError as str:
        print('ValueError')

result = f % 10
print(result)

print('6:')
while True:
    try:
        six: int = int(input('enter a 4-digit number:'))
        if six <= 999 or six >= 9999:
            print('not a 4-digit number')
            continue
        else:
            break
    except ValueError as str:
        print('ValueError')
x = six // 10
result = x % 10
print(result)

print('7:')
s: int = int(input('enter a 2-digit number:'))
ahadot: int = s // 10
asarot: int = s % 10
print(ahadot + asarot)

print('8:')
h: int = int(input('enter a 2-digit number:'))
ahadot: int = h // 10
asarot: int = h % 10
new_number: int = asarot * 10 + ahadot * 1
print(new_number)

print('9:')
n: int = int(input('enter a number:'))
if n % 2 == 0:
    print('even')
else:
    print('odd')
pay: float = 0

print("'10'")
salary = int(input("enter your salary:"))
if salary > 6000 and salary < 12000:
    tax = salary * 0.10
    print("your salary after taxes is:", salary - tax)
if salary > 12000 and salary < 18000:
    tax = salary * 0.20
    print("your salary after taxes is:", salary - tax)
if salary > 18000 and salary < 25000:
    tax = salary * 0.30
    print("your salary after taxes is:", salary - tax)
if salary > 25000 and salary < 35000:
    tax = salary * 0.40
    print("your salary after taxes is:", salary - tax)
if salary > 35000 and salary < 50000:
    tax = salary * 0.45
    print("your salary after taxes is:", salary - tax)
if salary < 12000:
    tax = salary * 0.51
    print("your salary after taxes is:", salary - tax)

print('11:')

age: int = int(input('enter your age:'))
height: float = float(input('enter your height:'))
if 18 < age and height > 100:
    print('you can go!!!')
elif 8 < age < 18 and height > 115:
    print('you can go!!!')
else:
    print("Sorry, you can't go up,you are not in the criteria")

print('לולאות:')
print('3')
n: int = int(input('enter a number:'))
if n % 2 == 0:
    for i in range(0, n + 1, 2):
        print(i, end=' ')
else:
    for i in range(0, n + 2, 2):
        print(i, end=' ')

print()
print('4:')
max = int(input("enter a num(max):"))
den = int(input("enter a num(den):"))
i = 0
while (i < max):
    i += 1
    if i % den == 0:
        print(i, "divided my den")

print('עיבוד נתונים')
print("4:")
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
result = 0
for i in range(num2):
    result = result + num1
print("the answer is ", result)
print()

print("5:")
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
result = 1
for i in range(num2):
    result = result * num1
print("the answer is ", result)

print('6:')
number = int(input("enter a num:"))
digit = int(input("enter one digit:"))
while number > 0:
    last_digit = number % 10
    if last_digit == digit:
        answer = True
        break
    else:
        answer = False
    number //= 10
print(answer)

print('7:')
a = int(input('enter a number:'))
b = int(input('enter a number:'))
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print("The greatest common denominator is:", a)

print('8:')
is_prime = True
number: int = int(input('enter a number:'))
if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')

print('לולאות מורכבות:')
print('2:')
Infavor_list = []
against_list = []
avoids_list = []
veto_list = []
i = 0
subject = input("enter the vote subject:")
while (i <= 44):
    print("enter your vote country num", i + 1)
    i += 1
    try:
        vote = input()
        match vote:
            case "1":
                Infavor_list.append(vote)
            case "2":
                against_list.append(vote)
            case "3":
                avoids_list.append(vote)
            case "4":
                print("country number", i, "voted veto")
                break
            case _:
                print("Invalid vote number. Please enter 1, 2, 3, or 4.")
    except ValueError:
        print("Error: Please enter a valid number (1, 2, 3, or 4).")
print("end of votting! on the vote for the", subject, "\nResualts:")
print("infavor countries:", len(Infavor_list), "\nthe list-", Infavor_list)
print("against countries:", len(against_list), "\nthe list-", against_list)
print("avoiding countries:", len(avoids_list), "\nthe list-", avoids_list)
