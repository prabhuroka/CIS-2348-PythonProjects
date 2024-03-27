# Prabhu Roka
# 1986444
def output_roster(roster):
    print("ROSTER")
    for jersey_number in sorted(roster.keys()):
        print(f"Jersey number: {jersey_number}, Rating: {roster[jersey_number]}")


def add_player(roster):
    jersey_number = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    roster[jersey_number] = rating


def delete_player(roster):
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in roster:
        del roster[jersey_number]
    else:
        print("Jersey number not found.")


def update_player_rating(roster):
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in roster:
        new_rating = int(input("Enter a new rating for player:\n"))
        roster[jersey_number] = new_rating
    else:
        print("Jersey number not found.")


def output_players_above_rating(roster):
    rating_threshold = int(input("Enter a rating:\n"))
    above_players = []
    for jersey_number in sorted(roster.keys(), key=int):
        rating = roster[jersey_number]
        if rating > rating_threshold:
            above_players.append((jersey_number, rating))

    if above_players:
        print(f"\nABOVE {rating_threshold}")
        for jersey_number, rating in above_players:
            print(f"Jersey number: {jersey_number}, Rating: {rating}")
    else:
        print("No players found above the specified rating.")

def main():
    roster = {}
    for i in range(5):
        jersey_number = int(input(f"Enter player {i + 1}'s jersey number:\n"))
        rating = int(input(f"Enter player {i + 1}'s rating:\n\n"))
        roster[jersey_number] = rating

    output_roster(roster)

    menu_options = {
        'a': add_player,
        'd': delete_player,
        'u': update_player_rating,
        'r': output_players_above_rating,
        'o': output_roster
    }

    choice = ''
    while choice != 'q':
        print("\nMENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")

        choice = input("\nChoose an option:\n")

        if choice in menu_options:
            menu_options[choice](roster)
        elif choice != 'q':
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
