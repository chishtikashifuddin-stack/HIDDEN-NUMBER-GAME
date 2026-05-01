import random
players = []
def main():
    global secret
    print("               *--------------------------------------*                   ")
    print("               |          HIDDEN NUMBER GAME          |                   ")
    print("               *--------------------------------------*\n                 ")
    print("                     *---------------------------*                        ")
    print("                     |GUESS THE NUMBER (1 TO 100)|                        ")
    print("                     *---------------------------*\n                      ")        
    choice = input("CHOICE HOW MANY PAYERS YOU WANT : ")
    if choice.isdigit():
        choice = int(choice)
        if choice <= 50 and choice!=0:
            one(choice)
        else:
            print("                ---------------------------------           ")
            print("               |The PLAYER CAPACITY ONLY 1 to 50.|          ")
            print("                ---------------------------------        \n")
            main()
    else:
        print("                      ------------------------                   ")
        print("                     |PLEASE ENTER NUMBER ONLY|                   ")
        print("                      ------------------------\n                  ")
        main()
        
def one(choice):
    for i in range(choice):
        a = input(f"ENTER PLAYER NAME : ")
        players.append(a)
    print("GAME STARTED\n")
    secret = random.randint(1,100)
    for e1 in range(10000):
        for c in players:
            print("*-----------------------------*")
            b = input(f"ENTER YOURE NUMBER {c} : ")
            if b.isdigit():
                b=int(b)
                if b < 0 or b > 100:
                    print("Please enter a number between 1 and 100")
                if b == secret:
                    print(f"PLAYER {c} wins!,The is number : {secret}")
                    print("------------------------------------\n")               
                    again = input("Play again? (yes/no): ")
                    if again == "no" or again == "NO":
                        print("Game Over!\n")
                        players.clear()
                        main()   
                    if again == "yes" or again == "YES":
                        print("New Game !")
                        one(choice)
                    else:
                        print("PLEASE ENTER YES OR NO")
                        main()           
                        
                if b < secret:
                    print("         Higher        ")
                    print("---------------------")

                if b > secret:
                    print("         Lower         ")
                    print("---------------------")
            else:
                print("PLEASE ENTER NUMBER ONLY")
                print("-----------------------\n")
                
main()