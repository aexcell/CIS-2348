# Alexandra Excell PSID: 1595971

# Exact Change

def exact_change(user_input):

    numdollars = 0
    numquarters = 0
    numdimes = 0
    numnickels = 0
    numpennies = 0
    change = user_input
    if change == 0:
        print('no change')
    if change >= 100:
        numdollars = change//100
        change = change - numdollars * 100
    if change >= 25:
        numquarters = change//25
        change = change - numquarters * 25
    if change >= 10:
        numdimes = change//10
        change = change - numdimes * 10
    if change >= 5:
        numnickels = change//5
        change = change - numnickels * 5
    if change >= 1:
        numpennies = change

    if numdollars > 1:
        print('%d dollars' % numdollars)
    elif numdollars == 1:
        print('%d dollar' % numdollars)
    if numquarters > 1:
        print('%d quarters' % numquarters)
    elif numquarters == 1:
        print('%d quarter' % numquarters)
    if numdimes > 1:
        print('%d dimes' % numdimes)
    elif numdimes == 1:
        print('%d dime' % numdimes)
    if numnickels > 1:
        print('%d nickels' % numnickels)
    elif numnickels == 1:
        print('%d nickel' % numnickels)
    if numpennies > 1:
        print('%d pennies' % numpennies)
    elif numpennies == 1:
        print('%d penny' % numpennies)

    return numdollars, numquarters, numdimes, numnickels, numpennies

if __name__ == '__main__':
    inputval = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(inputval)
