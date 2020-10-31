# Alexandra Excell  PSID: 1595971
# First Part

jer_num1 = int(input("Enter player 1's jersey number:\n"))
rating1 = int(input("Enter player 1's rating:\n\n"))

jer_num2 = int(input("Enter player 2's jersey number:\n"))
rating2 = int(input("Enter player 2's rating:\n\n"))

jer_num3 = int(input("Enter player 3's jersey number:\n"))
rating3 = int(input("Enter player 3's rating:\n\n"))

jer_num4 = int(input("Enter player 4's jersey number:\n"))
rating4 = int(input("Enter player 4's rating:\n\n"))

jer_num5 = int(input("Enter player 5's jersey number:\n"))
rating5 = int(input("Enter player 5's rating:\n\n"))


roster = {jer_num1:rating1,
          jer_num2:rating2,
          jer_num3:rating3,
          jer_num4:rating4,
          jer_num5:rating5}
roster_list = sorted(roster)
print("ROSTER")
for player in roster_list:
    print("Jersey number: {}, Rating: {}".format(player,roster[player]),end="\n")

def print_menu():
    menu = {'a': 'Add player',
            'd':'Remove player',
            'u': 'Update player rating',
            'r': "Output players above a rating",
            'o': 'Output roster',
            'q': 'Quit'}
    print('\nMENU')
    for option in menu:
        print('{} - {}'.format(option, menu[option]))
    print('')
    user_input = input('Choose an option:\n')
print_menu()