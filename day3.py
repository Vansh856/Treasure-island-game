'''#conditional statement
print("Welcome to the rollercoster")
Hight= int (input("What's your height in cm?  \n"))
bill=0
if Hight>120:
    print("Can ride")
    age=int(input("What is your age? "))
    if age<12:
        bill=5     # if this condition is true bill will be set to 5
        print("You have to pay $5")
    elif age <=18:
        bill=7               # if this condition is true bill will be set to 7
        print("You have to pay $7")
    else:
        bill=12                # if this condition is true bill will be set to 12 
        print("You have to pay $12")
    photo=input("Do you want a photo.Type y for yes, or type n for no")
    if photo=="y":
        bill+=3
        print(f"you have to pay ${bill}")

else:
    print("Can't ride")
    

#modulas operaTOR
print(10%3)

#EVEN ODD CHECK

num= int(input("ENTER THE NUMBER "))
if num%2==0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")


# pizza delivery

print("Welcome to the pizza deliveries!")

#pizza delivery

print("Welcome to the python pizza deliveries!")
size=input("What size pizza do you want? s,m or l:")
pepperoni=input("Do you want pepproni on your pizza? Y or N :")
extra_cheese=input("Do you want extra cheese? Y or N :")
bill=0
if size== "s":
    bill+=15
elif size=="m":
    bill+=20
elif size=="l":
    bill+=25
else:
    print("Enter a correct input")
if pepperoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3
if extra_cheese=="y":
    bill+=1
print(f"Ypur final bil is:  $ {bill}")
 
# tresure island game
print("Welcome to Treasure Island.\nYour mission is to find the treasure")
level1=input("Which side do you want to go? l for left , r for right")
if level1=="l":
    print("Congratulations, you have entered in level 2 ")
    level2=input("River ahed.\n Doo you want to swim or wait for the boat?\n Enter s for swim , and w to wait")
    if level2=="s":
        print("Attacked by trout.\n Game Over.")
    elif level2=="w":
        print("Congratulation, you havel completed level 2.")
        final_level=input("3 doors ahead. Which one you want to choose.\n Enter r for red, y for yello, b for blue.")
        if final_level=="r":
            print("Burned by fire.\n Game Over.")
        elif final_level=="y":
            print("YOU WON!")
        elif final_level=="b":
            print("Eaten by beasts.\n Game Over.")

    else:
        print("Enter a valid input.")
elif level1==r:
    print("Fall into a hole.\n Game over.")
else:
    print("Enter a correct input")

'''