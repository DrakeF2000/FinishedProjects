from multiprocessing.resource_sharer import stop
import random

#Enter the minimum and maximum limits fo the dice rolls below
min_val = 1
max_val = 6

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Dices rolling...")
    print("The values are....")
#Printing the rolls value
print(random.randint(min_val,max_val))
print(random.randint(min_val,max_val))
roll_again= input("Roll the Dices Again?")

stop