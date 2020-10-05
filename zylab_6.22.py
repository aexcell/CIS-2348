# Alexandra Excell PSID: 1595971

# Brute force equation solver
p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())
p5 = int(input())
p6 = int(input())


t = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if p1*x+p2*y==p3:
            if p4*x+p5*y==p6:
                print(x,y)
                t = True
if t == False:
    print('No solution')