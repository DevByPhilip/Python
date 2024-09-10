# FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else: 
        print(i) 

# Skottårskontroll
year = input('Skriv ett årtal: ')

if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
    print(f'{year} är ett skottår')
else:
    print(f'{year} är inte ett skottår')