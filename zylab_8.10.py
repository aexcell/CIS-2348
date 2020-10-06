# Alexandra Excell PSID: 1595971

# Palindrome

def check_palindrome(string):
    n_string = string.replace(' ', '')
  # print(n_string)
    length = len(n_string)
    first = 0
    last = length -1
    status = 1
    while(first<last):
           if(n_string[first]==n_string[last]):
               first=first+1
               last=last-1
           else:
               status = 0
               break
    return int(status)
string = input()
status= check_palindrome(string)
if(status):
    print(string, 'is a palindrome')
else:
    print(string, 'is not a palindrome')