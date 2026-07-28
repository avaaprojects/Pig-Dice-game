import myfns

def play():
    myfns.clear()
    if choice.lower()=="y":
        while True:
            n=input("Please enter number of players (minimum of 2, maximum of 4: \n\n")
            if n.isdigit():
                n=int(n)
                if 1 < n <= 4:
                    break
                else:
                    print("\nOnly a minimum of 2 and maximum of 4 players! Please try again...")
            else:
                print("\nInvalid entry! Please try again...")
    elif choice.lower()=="n":
        print("You have quit the game...")
        return
    else:
        print("Please enter a valid choice...")

    for i in range(1,n+1):
        name=input(f"Player-{i}, what would you like to go by?- ")
        myfns.addname(name)

    max_score=50
    player_scores=myfns.fetch_score()
    current_score=0

    while max(player_scores)[0]< max_score:
        for pid in range(n):
            player_scores=myfns.fetch_score()
            current_score=player_scores[pid][0]
            current_player=myfns.fetch_name()[pid][0]

            print(f"\n{current_player}, your turn has started! \n")
            print(f"Your total score is {player_scores[pid]}\n")

            while True:
                should_roll=input("Would you like to roll (y): ")
                if should_roll.lower()!="y":
                    print("Ending your turn..")
                    break

                myfns.roll()

                if myfns.rand_num==1:
                    print("You rolled a ONE, your turn is DONE! ")
                    current_score=0
                    break
                else:
                    current_score=current_score+ myfns.rand_num
                    print(f"You rolled a {myfns.rand_num}. Your Current score is {current_score}")

                if current_score >= 50:
                    break

            myfns.update_score(current_player, current_score)
            print(f"{current_player}'s score is {current_score}")

    myfns.find_winner()
    myfns.clear()

while True:
    with open("rules.txt","r") as obj:
        rules=obj.read()
        print(rules, "\n\n")

    choice=input(
        "Y- I'm ready to play\n"
        "N- I'd like to quit\n\n"
        "Enter your choice: ")
    play()
