try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
