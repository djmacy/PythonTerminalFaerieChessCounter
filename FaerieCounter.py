choose_diff = True

total_points = 0
min_points = 0
max_points = 0
rank_1 = 0
rank_2 = 0

'''
print("Hello! Welcome to the Faerie Chess Counter\n\nBegin by choosing the difficulty. Insert B for beginner, I for "
      "intermediate, and A for advanced")

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

while rank_1 < 8:
    pawn_value = 1
    peasant_value = 2
    soldier_value = 3

    pawn_limit = 8
    peasant_limit = 2
    soldier_limit = 2

    peasant_min = 0
    soldier_min = 0

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

'''
while rank_2 < 6:
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

    




