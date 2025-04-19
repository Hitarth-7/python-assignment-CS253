import random #Importing random library for generating random choice for the computer
choices=["rock", "paper", "scissors"] #Giving the choices as rock paper and scissors to evaluate inputs later
en_choice={"rock":4, "paper":2, "scissors":3} #Enumerating the choices effectively to calculate the winner of the game

#Function for the game rock paper scissors
def Rock_Paper_Scissors(user_in, wins, losses, ties):
    c_wins=wins #Win local variable declared for updating
    c_losses=losses #Loss local variable declared for updating
    c_ties=ties #Ties local variable declared for updating
    c_out=random.choice(choices) #Choosing random input for the computer
    print(f"Your Choice : {user_in} \n Computer's choice : {c_out}") #Printing both players' choices
    #Calculating the winner on the basis of enumerated choices 
    if(en_choice[user_in] > en_choice[c_out]): #Checking if the user score is more than computer's for input pairs containing scissors
        if(en_choice[user_in]==en_choice[c_out]+2): #Checking for the case of user_in=rock and c_out=paper then the user loses
            print("You Lost!") #Printing win message
            c_losses+=1 #Loss counter updated for the round
        else:
            print("You Won!") #Printing win message
            c_wins+=1 #Win counter updated for the round
    elif(en_choice[c_out] > en_choice[user_in]): #Checking if the computer's score is more than user's for input pairs containing scissors
        if(en_choice[c_out]==en_choice[user_in]+2): #Checking for the case of user_in=rock and c_out=paper then the user loses
            print("You Won!") #Printing win message
            c_wins+=1 #Win counter updated for the round
        else:
            print("You Lost!") #Printing win message
            c_losses+=1 #Loss counter updated for the round
    else: #If either of them is not greater than the other, then both inputs must be equal
        print("Draw!") #Print draw
        c_ties+=1 #Tie counter updated for the round
    return [c_wins, c_losses, c_ties] #Returning after the game ends

#Function main
def main():
    wins=0 #Win counter initialized for the round
    losses=0 #Loss counter initialized for the round
    ties=0 #Tie counter initialized for the round
    #Looping over infinitely since ending the game depends on the user input
    while True:
        user_in=input("Enter your choice from Rock Paper or Scissors : \nOR Type quit to exit \n") #Prompting user for input
        user_in=user_in.lower() #Converting everything to lower to maintain consistency and allow case insensitive experience for the user
        if(user_in == "quit"): #If the user types quite, loop breaks and game ends
            print(f'Your total Wins are {wins}') #Win score printed for the round
            print(f'Your total Losses are {losses}') #Loss score printed for the round
            print(f'Your total Ties are {ties}') #Tie counter printed for the round
            print("Thank you for playing") #Printing thankyou message
            break
        elif(user_in not in choices): # if user inputs anything other than the choices given to them, then the game repeats
            print("Invalid Input, PLease try again") #Printing the invalid input message
            continue #Starting over the game
        [wins, losses, ties]=Rock_Paper_Scissors(user_in, wins, losses, ties) #Calling the game to check for winner and dereferencing the return values 

#If the file containing the main and not the file in which this file is imported is running the program then call main
if __name__ == "__main__":
    main()