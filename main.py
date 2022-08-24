import os


def check(input, condition):
    for list in condition:
        # print(list)
        check = all(item in input for item in list)
        # print(check)
        if check:
            check = True
            return check
    return False

empty_frame = "  |   |   \n" \
              "----------\n" \
              "  |   |   \n" \
              "----------\n" \
              "  |   |   "

key_frame = f"A | B | C\n" \
            "-----------\n" \
            f"D | E | F\n" \
            "-----------\n" \
            f"G | H | I "


win_condition = [['A', 'B', 'C'],
                 ['D', 'E', 'F'],
                 ['G', 'H', 'I'],
                 ['A', 'D', 'G'],
                 ['B', 'E', 'H'],
                 ['C', 'F', 'I'],
                 ['A', 'E', 'I'],
                 ['G', 'E', 'C']]


player_1 = []
player_2 = []

print(empty_frame)
game_continue = False
user_input = input("Would you like to play Tic-Tac-Toe game? Yes/No: ").upper()

if user_input == "YES":
    print(key_frame)
    print("\n")
    game_continue = 9
    while game_continue > 0:
        if game_continue % 2 != 0:
            player_1_input = input("Player 1: ").upper()
            player_1.append(player_1_input)
            key_frame = key_frame.replace(player_1_input, 'O')
        else:
            player_2_input = input("Player 2: ").upper()
            player_2.append(player_2_input)
            key_frame = key_frame.replace(player_2_input, 'X')
        os.system('clear')
        print(key_frame)
        print("\n")

        # print(player_1)
        # print(check(player_1, win_condition))
        if check(player_1, win_condition):
            # print(check(player_1, win_condition))
            print("Player 1 won!")
            game_continue = 0

        # print(player_2)
        # print(check(player_2, win_condition))
        if check(player_2, win_condition):
            print("Player 2 won!")
            game_continue = 0

        game_continue -= 1

    # print(player_1)
    # print(player_2)

elif user_input == "NO":
    print("Alright, Goodbye.")
else:
    print("Sorry invalid, entry, goodbye!")
