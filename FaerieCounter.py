#David Macy
#This is a terminal application that asks the user which pieces it would like to use for the faerie chess board game.
#Once all the pieces have been selected it will count up how many points the user has left or if they picked too many pieces.
#This was created so people do not need to count up the points themselves but rather have the application do it and let them know if they have points to spare


#check to see if there are more than 1 piece or less than 0 pieces selected to see if user picked a valid amount when selecting for rank II pieces
def check_for_rankII(piece):
    if piece > 1 or piece < 0:
        print("Please select 0 to 1", piece)

run = True

while run:

    choose_diff = True
    total_points = 0
    min_points = 0
    max_points = 0
    rank_1 = 0
    rank_2 = 0
    rank_3 = 0

    print("Hello! Welcome to the Faerie Chess Counter\n\nBegin by choosing the difficulty. Insert B for beginner, I for "
          "intermediate, and A for advanced")

    #This is where the user will select which difficulty they are playing on. The difficulty will determine how many points
    #they can have when choosing their pieces
    while choose_diff:
        difficulty = input("\nWhat difficulty are you playing on:\n").upper()
        #print(type(difficulty))
        if difficulty == "B":
            print("Great you will play with 60 - 65 points")
            min_points = 60
            max_points = 65
            choose_diff = False
            break
        elif difficulty == "I":
            print("Great you will play with 65 - 70 points")
            min_points = 65
            max_points = 70
            choose_diff = False
            break
        elif difficulty == "A":
            print("Great you will play with 70 - 75 points")
            min_points = 70
            max_points = 75
            choose_diff = False
            break
        else:
            difficulty = print("Please choose B, I, or A")
            continue

    #The user can only select 8 rank I pieces so it will break when the user selects more than 8
    while rank_1 < 8:
        rank_1 = 0
        total_points = 0

        pawn_value = 1
        peasant_value = 2
        soldier_value = 3

        pawn_limit = 8
        peasant_limit = 2
        soldier_limit = 2

        peasant_min = 0
        soldier_min = 0

        pawn = 0
        peasant = 0
        soldier = 0

        pawn = int(input("How many pawns would you like: "))
        if pawn < 4 or pawn > pawn_limit:
            print("Invalid input. Please select between 4 and", pawn_limit, "pawns.")
            continue
        total_points += pawn * pawn_value
        rank_1 += pawn
        if rank_1 == 8:
            print("You have selected the maximum number of Rank I pieces")
            break
        elif rank_1 == 4:
            peasant = 2
            soldier = 2
            total_points += (peasant * peasant_value + soldier * soldier_value)
            print("Due to picking 4 pawns you will automatically get 2 peasants and 2 soldiers")
            break
        elif rank_1 > 4:
            peasant_min = max(0,8 - (rank_1 + soldier_limit))
            peasant_limit = min(2, 8 - rank_1)

        print("You can select from", peasant_min, "to", peasant_limit, "peasants")
        peasant = int(input("How many peasants would you like: "))
        if peasant < peasant_min or peasant > peasant_limit:
            print("Invalid input. Please select between ", peasant_min, "and ", peasant_limit)
            continue
        total_points += peasant * peasant_value
        rank_1 += peasant
        if rank_1 == 8:
            print("You have picked the maximum number of pieces")
            break
        elif rank_1 == 6:
            print("You automatically get 2 soldiers")
            soldier = 2
            total_points += soldier * soldier_value
            rank_1 += soldier
        elif rank_1 == 7:
            print("You automatically get 1 soldier")
            soldier = 1
            total_points += soldier * soldier_value
            rank_1 += soldier
    print("You selected", pawn, "Pawns", peasant, "Peasants", soldier, "Soldiers")
    print("Total points for Rank I pieces:", total_points, ". You have", max_points - total_points, "points left!\nNow"
            " lets pick your Rank II pieces. You can only select 6 Rank II pieces.")

    rankI_points = total_points

    done_selecting = False

    #User can only select 6 rank_2 pieces and will break when the user has selected more than 6
    while rank_2 < 6 and not done_selecting:
        total_points = rankI_points
        rook_value = 9
        knight_value = 4
        bishop_value = 6
        catapult_value = 3
        chamberlain_value = 6
        courtesan_value = 6
        herald_value = 6
        inquisitor_value = 6
        lancer_value = 5
        pontiff_value = 8
        thief_value = 5
        tower_value = 10

        classical_limit = 2
        new_limit = 1

        rank_2 = 0

        rook = int(input("How many rooks would you like: "))
        if rook > classical_limit or rook < 0:
            print("Invalid input. Please select between 0 and", classical_limit, "rooks.")
            continue
        total_points += rook * rook_value
        rank_2 += rook

        knight = int(input("How many knights would you like: "))
        if knight > classical_limit or knight < 0:
            print("Invalid input. Please select between 0 and", classical_limit, "knights.")
            continue
        total_points += knight * knight_value
        rank_2 += knight

        bishop = int(input("How many bishops would you like: "))
        if bishop > classical_limit or bishop < 0:
            print("Invalid input. Please select between 0 and", classical_limit, "bishops.")
            continue
        total_points += bishop * bishop_value
        rank_2 += bishop

        if rank_2 == 6:
            done_selecting = True
            break

        print("\nFor the rest of these insert 0 for no and 1 for yes")
        catapult = int(input("Would you like a catapult: "))
        check_for_rankII(catapult)
        total_points += catapult * catapult_value
        rank_2 += catapult

        if rank_2 == 6:
            done_selecting = True
            break

        chamberlain = int(input("Would you like a chamberlain: "))
        check_for_rankII(chamberlain)
        total_points += chamberlain * chamberlain_value
        rank_2 += chamberlain

        if rank_2 == 6:
            done_selecting = True
            break

        courtesan = int(input("Would you like a courtesan: "))
        check_for_rankII(courtesan)
        total_points += courtesan * courtesan_value
        rank_2 += courtesan

        if rank_2 == 6:
            done_selecting = True
            break

        herald = int(input("Would you like a herald: "))
        check_for_rankII(herald)
        total_points += herald * herald_value
        rank_2 += courtesan

        if rank_2 == 6:
            done_selecting = True
            break

        inquisitor = int(input("Would you like an inquisitor: "))
        check_for_rankII(inquisitor)
        total_points += inquisitor * inquisitor_value
        rank_2 += inquisitor

        if rank_2 == 6:
            done_selecting = True
            break

        lancer = int(input("Would you like a lancer: "))
        check_for_rankII(lancer)
        total_points += lancer * lancer_value
        rank_2 += lancer

        if rank_2 == 6:
            done_selecting = True
            break

        pontiff = int(input("Would you like a pontiff: "))
        check_for_rankII(pontiff)
        total_points += pontiff * pontiff_value
        rank_2 += pontiff

        if rank_2 == 6:
            done_selecting = True
            break

        thief = int(input("Would you like a thief: "))
        check_for_rankII(thief)
        total_points += thief * thief_value
        rank_2 += thief

        if rank_2 == 6:
            done_selecting = True
            break

        tower = int(input("Would you like a tower: "))
        check_for_rankII(tower)
        total_points += tower * tower_value
        rank_2 += tower

        if rank_2 == 6:
            done_selecting = True
            break

    print("You have selected all of your Rank II pieces")
    print("Total points for Rank II & Rank I pieces:", total_points, ". You have", max_points - total_points,
          "points left!\nNow lets pick your Rank III pieces. You can only select 2 Rank III pieces.")


    rankIII_points = total_points

    #Can only select 2 rank 3 pieces
    while rank_3 < 2:
        rank_3 = 0
        total_points = rankIII_points
        queen_value = 12
        king_value = 0
        jester_value = 12
        regent_value = 15

        print("Enter 0 for no and 1 to yes")
        queen = int(input("Would you like a queen: "))
        if (queen > 1 or queen < 0):
            print("Please insert 0 or 1")
            continue
        elif (queen == 1):
            total_points += queen * queen_value
            rank_3 += queen
        else:
            print("Since you did not select a queen you automatically get a jester")
            jester = 1
            total_points += jester * jester_value

        if max_points - total_points <= regent_value:
            print("You do not have enough points for a regent so you will have to get a king.")
            king = 1
            total_points += king * king_value
            rank_3 += king
            break

        king = (int(input("Would you like a king: ")))
        if (king > 1  or king < 0):
            print("Please insert 0 or 1")
            continue
        elif (king == 1):
            total_points += king * king_value
            rank_3 += king
            break
        else:
            print("Since you did not select a king you automatically get a regent")
            regent = 1
            total_points += regent * regent_value
            break

    print("You have selected all of your Rank III pieces")
    print("Total points for Rank III pieces:", total_points,". You have", max_points - total_points,
          "points left!")
    redo = input("Would you like to change the difficulty or pick different pieces? Insert y or n: ").lower()
    if redo != "y":
        print("Thank you. See you next time!")
        break
    elif redo == "y":
        choose_diff = True
        rank_1 = 0
        rank_2 = 0
        rank_3 = 0