# David Macy
# This is a terminal application that asks the user which pieces it would like to use for the Brybelly faerie chess board game.
# once all the pieces have been selected it will count up how many points the user has left or if they picked too many pieces.
# this was created so people do not need to count up the points themselves but rather have the application do it and let them know if they have points to spare.

def check_for_valid_input(piece):
    selecting = True
    while selecting:
        user_input = input(piece)
        if user_input.isdigit():
            value = int(user_input)
            return value
            break
        else:
            print("Invalid input. Please insert a valid integer")
            continue


def calculate_rankI_points(min_points, max_points):
    total_points = 0
    rank_1 = 0
    # This is how many points that each piece is worth
    pawn_value = 1
    peasant_value = 2
    soldier_value = 3
    # This is the maximum number of pieces available for each piece.
    pawn_limit = 8
    peasant_limit = 2
    soldier_limit = 2
    pawn_min = 4
    # The user can only select 8 rank I pieces so it will break when the user selects more than 8
    while rank_1 < 8:
        pawn = check_for_valid_input("How many pawns would you like: ")

        if pawn < pawn_min or pawn > pawn_limit:
            print("Invalid input. Please select between", pawn_min, "and", pawn_limit, "pawns.")
            continue
        # This variable will keep track of how many points the user has until the end of the script
        total_points += pawn * pawn_value
        # rank_1 will determine when we have selected the right number of pieces. 8 is the maximum number of rank_1 pieces
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
            peasant_min = max(0, 8 - (rank_1 + soldier_limit))
            peasant_limit = min(2, 8 - rank_1)

        print("You can select from", peasant_min, "to", peasant_limit, "peasants")
        peasant = check_for_valid_input("How many peasants would you like: ")
        if peasant < peasant_min or peasant > peasant_limit:
            print("Invalid input. Please select between", peasant_min, "and", peasant_limit, "peasants.")
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

    return total_points


# User can only select 6 rank_2 pieces and will break when the user has selected more than 6
def calculate_rankII(total_points, max_points):
    # classical_limit is 2 because in the original game of chess you have 2 rooks, 2 bishops, and 2 knights
    classical_limit = 2
    rank_2 = 0

    # This is the value of each rank_II piece
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

    while rank_2 < 6:
        # This will make sure that we get to six total pieces selected
        rank_2 = 0
        # restart the total points calculated to what the total was after rank_1 calculation if loop gets reset to
        rank_2_starting_points = total_points

        # Again similar with the Rank I pieces we have a limited number of pieces that the user can pick. For rank_II its 6
        print("Please select 6 Rank II pieces!")
        rook = check_for_valid_input("How many rooks would you like: ")
        if rook > classical_limit or rook < 0:
            rook = 0
            print("Invalid input. Please select between 0 and", classical_limit, "rooks.")
            continue
        rank_2_starting_points += rook * rook_value
        rank_2 += rook

        knight = check_for_valid_input("How many knights would you like: ")
        if knight > classical_limit or knight < 0:
            knight = 0
            print("Invalid input. Please select between 0 and", classical_limit, "knights.")
            continue
        rank_2_starting_points += knight * knight_value
        rank_2 += knight

        bishop = check_for_valid_input("How many bishops would you like: ")
        if bishop > classical_limit or bishop < 0:
            bishop = 0
            print("Invalid input. Please select between 0 and", classical_limit, "bishops.")
            continue
        rank_2_starting_points += bishop * bishop_value
        rank_2 += bishop

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break

        # There is only one of each piece that you can select from after you are done selecting from rooks, knights, and bishops.
        print("\nFor the rest of these insert y for yes and n for no")
        catapult = (input("Would you like a catapult: "))
        if catapult == "y":
            catapult = 1
            rank_2_starting_points += catapult * catapult_value
            rank_2 += catapult
        # If the user provides bad input we will restart the entire loop
        elif catapult != "n" and catapult != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break

        chamberlain = (input("Would you like a chamberlain: "))
        if chamberlain == "y":
            chamberlain = 1
            rank_2_starting_points += chamberlain * chamberlain_value
            rank_2 += chamberlain
        elif chamberlain != "n" and chamberlain != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break

        courtesan = (input("Would you like a courtesan: "))
        if courtesan == "y":
            courtesan = 1
            rank_2_starting_points += courtesan * courtesan_value
            rank_2 += courtesan
        elif courtesan != "n" and courtesan != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break

        herald = (input("Would you like a herald: "))
        if herald == "y":
            herald = 1
            total_points += herald * herald_value
            rank_2 += herald
        elif herald != "n" and herald != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            break

        inquisitor = (input("Would you like a inquisitor: "))
        if inquisitor == "y":
            inquisitor = 1
            rank_2_starting_points += inquisitor * inquisitor_value
            rank_2 += inquisitor
        elif inquisitor != "n" and inquisitor != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break

        lancer = (input("Would you like a lancer: "))
        if lancer == "y":
            lancer = 1
            rank_2_starting_points += lancer * lancer_value
            rank_2 += lancer
        elif lancer != "n" and lancer != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break

        pontiff = (input("Would you like a pontiff: "))
        if pontiff == "y":
            pontiff = 1
            rank_2_starting_points += pontiff * pontiff_value
            rank_2 += pontiff
        elif pontiff != "n" and pontiff != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break

        thief = (input("Would you like a thief: "))
        if thief == "y":
            thief = 1
            rank_2_starting_points += thief * thief_value
            rank_2 += thief
        elif thief != "n" and thief != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break

        tower = (input("Would you like a tower: "))
        if tower == "y":
            tower = 1
            rank_2_starting_points += tower * tower_value
            rank_2 += tower
        elif tower != "n" and tower != "y":
            rank_2 = 0
            print("please insert a valid value: y or n")
            continue

        if rank_2 >= 6:
            total_points = rank_2_starting_points
            break
        else:
            print("You only selected", rank_2, "pieces. Be sure to select 6 rank II pieces. The count will now reset!")
            continue

    return total_points


def calculate_rankIII(total_points, max_points):
    rank_3 = 0
    # Can only select 2 rank_III pieces
    while rank_3 < 2:
        queen_value = 12
        king_value = 0
        jester_value = 12
        regent_value = 15

        print("\nFor these insert y for yes and n for no")
        queen = input("Would you like a queen: ")
        if queen == "y":
            queen = 1
            total_points += queen * queen_value
        elif queen == "n":
            print("Since you did not select a queen you automatically get a jester")
            jester = 1
            total_points += jester * jester_value
        else:
            print("Invalid input. Please select 'y' or 'n'")
            continue

        if max_points - total_points <= regent_value:
            print("You do not have enough points for a regent so you will have to get a king.")
            king = 1
            total_points += king * king_value
            rank_3 += king
            break

        king = input("Would you like a king: ")
        if king == "y":
            king = 1
            total_points += king * king_value
        elif king == "n":
            print("Since you did not select a king you automatically get a regent")
            regent = 1
            total_points += regent * regent_value
            break
        else:
            print("Invalid input. Please select 'y' or 'n'")
            continue

    return total_points


def choose_difficulty():
    choose_diff = True
    print(
        "Hello! Welcome to the Faerie Chess Counter\n\nBegin by choosing the difficulty. Insert B for beginner, I for "
        "intermediate, and A for advanced")
    # This is where the user will select which difficulty they are playing on. The difficulty will determine how many points
    # they can have when choosing their pieces
    while choose_diff:
        difficulty = input("\nWhat difficulty are you playing on:\n").upper()
        if difficulty == "B":
            print("Great you will play with 60 - 65 points")
            min_points = 60
            max_points = 65
            break
        elif difficulty == "I":
            print("Great you will play with 65 - 70 points")
            min_points = 65
            max_points = 70
            break
        elif difficulty == "A":
            print("Great you will play with 70 - 75 points")
            min_points = 70
            max_points = 75
            break
        else:
            print("Please choose B, I, or A")
            continue
    return min_points, max_points

# Define the main function to run the application
def main():
    run = True

    while run:

        min_points, max_points = choose_difficulty()
        total_points = calculate_rankI_points(min_points, max_points)

        print("Total points for Rank I pieces:", total_points, ". You have", max_points - total_points,
              "points left!\nNow"
              " lets pick your Rank II pieces. You can only select 6 Rank II pieces.")

        total_points = calculate_rankII(total_points, max_points)
        print("You have selected all of your Rank II pieces")
        print("Total points for Rank II & Rank I pieces:", total_points, ". You have", max_points - total_points,
              "points left!\nNow lets pick your Rank III pieces. You can only select 2 Rank III pieces.")

        total_points = calculate_rankIII(total_points, max_points)
        print("You have selected all of your Rank III pieces")
        print("Total points for Rank III pieces:", total_points, ". You have", max_points - total_points,
              "points left!")

        redo = input("Would you like to change the difficulty or pick different pieces? Insert y or n: ").lower()
        if redo != "y":
            print("Thank you. See you next time!")
            break
        elif redo == "y":
            run = True


if __name__ == "__main__":
    main()
