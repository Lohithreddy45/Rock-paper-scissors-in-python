import random
user_input = int(input("enter the number (0-2)\n where \n 0 -Rock \n 1 -paper \n 2 -scissors: "))
computer_input = random.randint(0,2)
if user_input >=3 or user_input <0:
    print("Please enter invalid number")
elif user_input ==0 and computer_input == 2:print("Congoo..! You Won")
elif user_input ==2 and computer_input ==0:print("Naah..!  You Lost")
elif user_input == computer_input:print("Its a draw")    
elif computer_input > user_input:print("Naah..!  You Lost")
elif user_input>computer_input:print("Congoo..! You Won")
else:pass