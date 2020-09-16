# Alexandra Excell  PSID: 1595971

print('Birthday Calculator\n')

print('Current day')
current_month = int(input('Month:'))
current_day = int(input('Day:'))
current_year = int(input('Year:\n'))

print('Birthday')
birthday_month = int(input('Month:'))
birthday_day = int(input('Day:'))
birthday_year = int(input('Year:'))

year = current_year - birthday_year

if current_month > birthday_month:
    print('You are', year, 'years old.')
elif current_month < birthday_month:
    print('You are', year - 1, 'years old.')
elif current_month == birthday_month:
    if current_day > birthday_day:
        print('You are', year, 'years old.')
    elif current_day == birthday_day:
        print('You are', year, 'years old.')
        print('Happy Birthday!')
    else:
        print('You are', year - 1, 'years old.')