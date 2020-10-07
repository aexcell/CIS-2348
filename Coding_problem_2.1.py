# Alexandra Excell PSID: 1595971

# Coding Problem 2
# Part a
import calendar

date = 'April 5, 2020'
date = date.replace(',','')
first_space = date.find(' ')
month = date[:first_space]
second_space = date.find(' ',first_space +1)
day = date[first_space + 1:second_space]
year= date[second_space + 1:]

month_num = list(calendar.month_name).index(month)

print('{month_num}/{day}/{year}'.format(month_num=month_num,day=day,year=year))