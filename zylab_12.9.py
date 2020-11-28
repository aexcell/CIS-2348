# Alexandra Excell
# PSID: 1595971


# Split input into 2 parts: name and age

parts = input().split()
name = parts[0]
while name != '-1':

    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError:
        age = 0
        print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]













# parts = ["Lee 18", "Lua 21","Mary Beth 19","Stu 33","-1"]
#
# if __name__ == __main__:
# parts = input()
# name = parts[0].split()[0:-1]
# idx = 0
# while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    # try:
    #     name = ' '.join(parts[idx].split()[0:-1])
        # age = parts[idx].split()[-1]
        # print(name, age)
        # # print('{} {}'.format(name, age))
        # idx+=1
    # except ValueError as i:
        #     print(i)
        #     age = 0
        #     return age

