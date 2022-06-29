birth, gender = input().split()
year = int(birth[:2])
age = 0

if gender == '1' or gender == '2':
    year += 1900
else:
    year += 2000

age = 2012 - year + 1

print(age)