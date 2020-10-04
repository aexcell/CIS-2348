# Alexandra Excell PSID: 1595971

simple_password = input()
password = ''

for x in simple_password:
    if(x=='i'):
        password+="!"
    elif(x=='a'):
        password += "@"
    elif (x == 'm'):
        password += "M"
    elif (x == 'B'):
        password += "8"
    elif (x == 'o'):
        password += "."
    else:
        password += x
password += "q*s"
print(password)