# Alexandra Excell PSID: 1595971

# Coding Problem 2
# Part b
import calendar
import csv
f = open('inputDates.txt',newline='')
dates = list(csv.reader(f,delimiter='\n'))
output=[]
for date in dates:
    date = date[0].replace(',','')
    first_space = date.find(' ')
    month = date[:first_space]
    second_space = date.find(' ',first_space +1)
    day = date[first_space + 1:second_space]
    year= date[second_space + 1:]

    if month not in calendar.month_name:
        continue

    month_num = list(calendar.month_name).index(month)

    print('{month_num}/{day}/{year}'.format(month_num=month_num,day=day,year=year))
    output.append('{month_num}/{day}/{year}\n'.format(month_num=month_num,day=day,year=year))

# Part c
f = open('parsedDates.txt','w+')
for row in output:
    f.write(row)
f.close()