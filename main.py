#this will determine weither you are able to watch a movie today
print("POV you want to watch a movie")

dishes = input("Do you need to do the dishes?(yes or no)")

#the first chore you have to get done

if dishes == "yes":
    print("Do the dishes first.")
elif dishes == "no":
    print("Next question")
else:
    print("You can only answer yes or no.")

homework = input ("Do you have homework?(yes or no)")

#you also have to chek if you have homework today and if you've already done it

if homework == "yes":
    home = input("Have you already done it?(yes or no)")
    if home == "yes":
        print("Next question")
    elif home == "no":
        print("Do your homework first.")
    else:
        print("You can only answer yes or no.")
elif homework == "no":
    print("Next question")
else:
    print("You can only anwer yes or no.")

dinner = input("Have you eaten dinner?(yes or no)")

#you have to have eaten dinner before you can watch a movie

if dinner == "yes":
    print("Next question")
elif dinner == "no":
    print("Eat dinner first")
else:
    print("You can only answer yes or no.")

print("Bedtime is 9:00")
time = int(input("What time is it?(enter time as three numbers, no semicolon, Ex, 9:00 would be entered as 900)"))

#you can't strat a movie past your bedtime

if time >= 900:
    print("It is too late to start a movie. You can maybe watch a movie tommorrow.")
elif time <= 900:
    print("Next question")
else:
    print("You entered in the time wrong. Try again.")

mom = input("Did your mom say you could?(yes or no)")

#you have to chek with your mom before you can watc a movie
#all of your other task must be done before you can watch a movie
#if not all of your tasks are complete, then you have to finish them before you can watch a movie

if mom == "no":
    print("You can't watch a movie today. Maybe another time.")
elif mom == "yes" and dishes == "no" and dinner == "yes" and homework == "no" and time <= 900:
    print("You can watch a movie today!")
elif mom == "yes" and dishes == "no" and dinner == "yes" and homework == "yes" and home =="yes" and time <= 900:
    print("You can watch a movie today!")
else:
    print("Finish everything you need to do, then you take this survey again and maybe watch a movie later today or tommorrow")