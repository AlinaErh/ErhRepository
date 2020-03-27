#кортеж
people = ("Anna", 20,  "Jack", 18, "Olivia", 25, "Mia", 12)
print("Name:", people[0], "Age:", people[-7])

i = 2

while i < len(people):
    print("Name:", people[i], "Age:", people[i+1])
    i += 2

print("Number of people: ", len(people)//2)

print("-----")

#словарь
users = {1: "Anna", 2: "Jack", 3: "Olivia", 4: "Mia"}
print(users)

users[1] = "Michael"

print(users)

print("Key: ")

key = int(input())

if key in users:
    del users[key]
    for key in users:
        print(key, ":", users[key])
else:
    print("Error")

print("-----")

#строка
string1 = "Hello, world"
string2 = "!"
print(string1, string2 * 3)
string = string1 + string2
n = len(string)
print(string[n: :-1])
print(string[:5])
St = string.replace(",", "_")
print(St)
s7 = string[7]
print(s7, "-", ord(s7))

print("-----")

#циклы
while True:
    print("Number:")
    Number = input()
    if Number == "-":
        break

string = "!!Stop!!"

for i in string:
    if i == "!":
        continue
    print(i, end='')

print("-----")

#условие
print("1 or 2 = ")
number = int(input())
if number != 1 and number != 2:
    print("Error")
elif number == 1:
    print("One")
else:
    print("Two")

print("-----")

#функция

def NOD(A, B):
    while A != 0 and B != 0:
        if A > B:
            A %= B
        else:
            B %= A
    return A + B

print(NOD(36, 9))


