print("what do you want to do? huh?!")
print("Option 1: add two numbers")
print("Option 2: sub two numbers")
print("Option 3: mui two numbers")
print("Option 4: div two numbers")
option=float(input("What option man?"))
while option!=1 or option!=2 or option!=3 or option!=4:
    print("Between 1 and 4, duh!!")
    option = float(input("What option man?"))
add1 = float(input("Gimme da namba one!"))
add2 = float(input("Gimme da namba two!"))
if option==1:
    print("Let's suuuummm this shit!")
    print("And the result is", " ", add1+add2)
elif option==2:
    print("subtracting it is")
    print("And the result is", " ", add1 - add2)
elif option==3:
    print("let's mult pulty these nambas!")
    print("And the result is", " ", add1 * add2)
elif option==4:
    while add2==0:
        print("Bitch! Are you kidding me?")
        print("Choose another namba two!")
        add2 = float(input("Gimme da namba two!"))
    print("Deva  it is")
    print("And the result is", " ", add1 / add2)
else:
    print("Oh my gosh, don't you know how to use a calculeinard?")

