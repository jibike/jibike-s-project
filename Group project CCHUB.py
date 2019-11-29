print("ROCK PAPER SCISSORS")
name=input("Enter your name")
print("Welcome",name)
def RPS():
    games_list=["rock","paper","scissors"]
    from random import choice
    guesses=choice(games_list)
    users_guess=input("Enter your guess:")
    for i in guesses:
        if users_guess==i:
            print("CORRECT")
        else:   
            print("WRONG")
            print(" ")


        return
RPS()
a=''
while a != 'stop':
    a=input("Do you want to play again?")
    if a=="yes":
        RPS()
    else:
         quit()

       
