import random
spot1 = "___"
spot2 = "___"
spot3 = "___"
spot4 = "___"
spot5 = "___"
spot6 = "___"
spot7 = "___"
spot8 = "___"
spot9 = "___"
win = False
X_count = 0
O_count = 0
tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
print(tictactoe_board)
game = int(input("Do you want to play a friend or robot? (1 = friend, 2 = robot)"))
if game == 1:
    move1 = int(input("Player 1 you are O...Pick a spot (1-9): "))
    O_count = 1
    if move1 == 1:
        spot1 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 2:
        spot2 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 3:
        spot3 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 4:
        spot4 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 5:
        spot5 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 6:
        spot6 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 7:
        spot7 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 8:
        spot8 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 9:
        spot9 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    move2 = int(input("Player 2 you are X...Pick a spot (1-9): "))
    X_count = 1
    if move2 == 1:
        spot1 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 2:
        spot2 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 3:
        spot3 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 4:
        spot4 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 5:
        spot5 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 6:
        spot6 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 7:
        spot7 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 8:
        spot8 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 9:
        spot9 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    move3 = int(input("Player 1 you are O...Pick a spot (1-9): "))
    O_count = 2
    if move3 == 1:
        spot1 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 2:
        spot2 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 3:
        spot3 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 4:
        spot4 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 5:
        spot5 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 6:
        spot6 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 7:
        spot7 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 8:
        spot8 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 9:
        spot9 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    move4 = int(input("Player 2 you are X...Pick a spot (1-9): "))
    X_count = 2
    if move4 == 1:
        spot1 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 2:
        spot2 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 3:
        spot3 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 4:
        spot4 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 5:
        spot5 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 6:
        spot6 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 7:
        spot7 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 8:
        spot8 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 9:
        spot9 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    move5 = int(input("Player 1 you are O...Pick a spot (1-9): "))
    O_count = 3
    if move5 == 1:
        spot1 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 2:
        spot2 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 3:
        spot3 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 4:
        spot4 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 5:
        spot5 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 6:
        spot6 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 7:
        spot7 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 8:
        spot8 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 9:
        spot9 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
        print("YOU WON!")
    if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
        print("YOU WON!")
        win = True
    if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
        print("YOU WON!")
        win = True
    if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
        print("YOU WON!")
        win = True
    if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
        print("YOU WON!")
        win = True
    if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
        print("YOU WON!")
        win = True
    if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
        print("YOU WON!")
        win = True
    if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
        print("YOU WON!")
        win = True
    if win == False:
        move6 = int(input("Player 2 you are X...Pick a spot (1-9): "))
        X_count = 3
        if move6 == 1:
            spot1 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 2:
            spot2 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 3:
            spot3 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 4:
            spot4 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 5:
            spot5 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 6:
            spot6 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 7:
            spot7 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 8:
            spot8 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 9:
            spot9 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
            print("YOU WON!")
        if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
            print("YOU WON!")
            win = True
        if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
            print("YOU WON!")
            win = True
        if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
            print("YOU WON!")
            win = True
        if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
            print("YOU WON!")
            win = True
        if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
            print("YOU WON!")
            win = True
        if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
            print("YOU WON!")
            win = True
        if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
            print("YOU WON!")
            win = True
        if win == False:
            move7 = int(input("Player 1 you are O...Pick a spot (1-9): "))
            O_count = 4
            if move7 == 1:
                spot1 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 2:
                spot2 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 3:
                spot3 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 4:
                spot4 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 5:
                spot5 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 6:
                spot6 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 7:
                spot7 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 8:
                spot8 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 9:
                spot9 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
                print("YOU WON!")
            if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
                print("YOU WON!")
                win = True
            if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
                print("YOU WON!")
                win = True
            if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
                print("YOU WON!")
                win = True
            if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
                print("YOU WON!")
                win = True
            if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
                print("YOU WON!")
                win = True
            if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
                print("YOU WON!")
                win = True
            if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
                print("YOU WON!")
                win = True
            if win == False:
                move8 = int(input("Player 2 you are X...Pick a spot (1-9): "))
                X_count = 4
                if move8 == 1:
                    spot1 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 2:
                    spot2 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 3:
                    spot3 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 4:
                    spot4 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 5:
                    spot5 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 6:
                    spot6 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 7:
                    spot7 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 8:
                    spot8 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 9:
                    spot9 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
                    print("YOU WON!")
                if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
                    print("YOU WON!")
                    win = True
                if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
                    print("YOU WON!")
                    win = True
                if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
                    print("YOU WON!")
                    win = True
                if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
                    print("YOU WON!")
                    win = True
                if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
                    print("YOU WON!")
                    win = True
                if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
                    print("YOU WON!")
                    win = True
                if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
                    print("YOU WON!")
                    win = True
                if win == False:
                    move9 = int(input("Player 1 you are O...Pick a spot (1-9): "))
                    O_count = 5
                    if move9 == 1:
                        spot1 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 2:
                        spot2 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 3:
                        spot3 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 4:
                        spot4 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 5:
                        spot5 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 6:
                        spot6 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 7:
                        spot7 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 8:
                        spot8 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 9:
                        spot9 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
                        print("YOU WON!")
                    if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
                        print("YOU WON!")
                        win = True
                    if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
                        print("YOU WON!")
                        win = True
                    if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
                        print("YOU WON!")
                        win = True
                    if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
                        print("YOU WON!")
                        win = True
                    if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
                        print("YOU WON!")
                        win = True
                    if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
                        print("YOU WON!")
                        win = True
                    if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
                        print("YOU WON!")
                        win = True
                    if X_count == 4 and O_count == 5 and win == False:
                        print("It's a tie.")
                        
elif game == 2:
    move1 = int(input("Player 1 you are O...Pick a spot (1-9): "))
    O_count = 1
    open_spot = [1,2,3,4,5,6,7,8,9]
    open_spot.remove(move1)
    if move1 == 1:
        spot1 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 2:
        spot2 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 3:
        spot3 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 4:
        spot4 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 5:
        spot5 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 6:
        spot6 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 7:
        spot7 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 8:
        spot8 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move1 == 9:
        spot9 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    print("Robot you are X...Pick a spot (1-9)")
    move2 = open_spot[random.randint(0,7)]
    print(move2)
    open_spot.remove(move2)
    X_count = 1
    if move2 == 1:
        spot1 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 2:
        spot2 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 3:
        spot3 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 4:
        spot4 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 5:
        spot5 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 6:
        spot6 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 7:
        spot7 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 8:
        spot8 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move2 == 9:
        spot9 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    move3 = int(input("Player 1 you are O...Pick a spot (1-9): "))
    O_count = 2
    open_spot.remove(move3)
    if move3 == 1:
        spot1 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 2:
        spot2 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 3:
        spot3 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 4:
        spot4 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 5:
        spot5 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 6:
        spot6 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 7:
        spot7 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 8:
        spot8 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move3 == 9:
        spot9 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    print("Robot you are X...Pick a spot (1-9)")
    move4 = open_spot[random.randint(0,5)]
    print(move4)
    open_spot.remove(move4)
    X_count = 2
    if move4 == 1:
        spot1 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 2:
        spot2 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 3:
        spot3 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 4:
        spot4 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 5:
        spot5 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 6:
        spot6 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 7:
        spot7 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 8:
        spot8 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move4 == 9:
        spot9 = "_X_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    move5 = int(input("Player 1 you are O...Pick a spot (1-9): "))
    O_count = 3
    open_spot.remove(move5)
    if move5 == 1:
        spot1 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 2:
        spot2 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 3:
        spot3 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 4:
        spot4 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 5:
        spot5 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 6:
        spot6 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 7:
        spot7 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 8:
        spot8 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if move5 == 9:
        spot9 = "_O_"
        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
        print(tictactoe_board)
    if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
        print("YOU WON!")
    if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
        print("YOU WON!")
        win = True
    if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
        print("YOU WON!")
        win = True
    if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
        print("YOU WON!")
        win = True
    if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
        print("YOU WON!")
        win = True
    if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
        print("YOU WON!")
        win = True
    if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
        print("YOU WON!")
        win = True
    if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
        print("YOU WON!")
        win = True
    if win == False:
        print("Robot you are X...Pick a spot (1-9)")
        move6 = open_spot[random.randint(0,3)]
        print(move6)
        open_spot.remove(move6)
        X_count = 3
        if move6 == 1:
            spot1 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 2:
            spot2 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 3:
            spot3 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 4:
            spot4 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 5:
            spot5 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 6:
            spot6 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 7:
            spot7 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 8:
            spot8 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if move6 == 9:
            spot9 = "_X_"
            tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
            print(tictactoe_board)
        if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
            print("YOU WON!")
        if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
            print("YOU WON!")
            win = True
        if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
            print("YOU WON!")
            win = True
        if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
            print("YOU WON!")
            win = True
        if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
            print("YOU WON!")
            win = True
        if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
            print("YOU WON!")
            win = True
        if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
            print("YOU WON!")
            win = True
        if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
            print("YOU WON!")
            win = True
        if win == False:
            move7 = int(input("Player 1 you are O...Pick a spot (1-9): "))
            O_count = 4
            open_spot.remove(move7)
            if move7 == 1:
                spot1 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 2:
                spot2 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 3:
                spot3 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 4:
                spot4 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 5:
                spot5 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 6:
                spot6 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 7:
                spot7 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 8:
                spot8 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if move7 == 9:
                spot9 = "_O_"
                tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                print(tictactoe_board)
            if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
                print("YOU WON!")
            if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
                print("YOU WON!")
                win = True
            if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
                print("YOU WON!")
                win = True
            if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
                print("YOU WON!")
                win = True
            if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
                print("YOU WON!")
                win = True
            if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
                print("YOU WON!")
                win = True
            if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
                print("YOU WON!")
                win = True
            if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
                print("YOU WON!")
                win = True
            if win == False:
                print("Robot you are X...Pick a spot (1-9)")
                move8 = open_spot[random.randint(0,1)]
                print(move8)
                open_spot.remove(move8)
                X_count = 4
                if move8 == 1:
                    spot1 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 2:
                    spot2 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 3:
                    spot3 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 4:
                    spot4 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 5:
                    spot5 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 6:
                    spot6 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 7:
                    spot7 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 8:
                    spot8 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if move8 == 9:
                    spot9 = "_X_"
                    tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                    print(tictactoe_board)
                if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
                    print("YOU WON!")
                if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
                    print("YOU WON!")
                    win = True
                if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
                    print("YOU WON!")
                    win = True
                if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
                    print("YOU WON!")
                    win = True
                if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
                    print("YOU WON!")
                    win = True
                if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
                    print("YOU WON!")
                    win = True
                if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
                    print("YOU WON!")
                    win = True
                if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
                    print("YOU WON!")
                    win = True
                if win == False:
                    move9 = int(input("Player 1 you are O...Pick a spot (1-9): "))
                    O_count = 5
                    open_spot.remove(move9)
                    if move9 == 1:
                        spot1 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 2:
                        spot2 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 3:
                        spot3 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 4:
                        spot4 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 5:
                        spot5 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 6:
                        spot6 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 7:
                        spot7 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 8:
                        spot8 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if move9 == 9:
                        spot9 = "_O_"
                        tictactoe_board = spot1 + "|" + spot2 + "|" + spot3 + "\n" + spot4 + "|" + spot5 + "|" + spot6 + "\n" + spot7 + "|" + spot8 + "|" + spot9
                        print(tictactoe_board)
                    if spot1 == spot2 and spot1 == spot3 and spot1 != "___":
                        print("YOU WON!")
                    if spot4 == spot5 and spot4 == spot6 and spot4 != "___":
                        print("YOU WON!")
                        win = True
                    if spot7 == spot8 and spot7 == spot9 and spot7 != "___":
                        print("YOU WON!")
                        win = True
                    if spot1 == spot4 and spot1 == spot7 and spot1 != "___":
                        print("YOU WON!")
                        win = True
                    if spot2 == spot5 and spot2 == spot8 and spot2 != "___":
                        print("YOU WON!")
                        win = True
                    if spot3 == spot6 and spot3 == spot9 and spot3 != "___":
                        print("YOU WON!")
                        win = True
                    if spot1 == spot5 and spot1 == spot9 and spot1 != "___":
                        print("YOU WON!")
                        win = True
                    if spot3 == spot5 and spot3 == spot7 and spot3 != "___":
                        print("YOU WON!")
                        win = True
                    if X_count == 4 and O_count == 5 and win == False:
                        win = False
                        print("It's a tie.")

