def print_roster(roster_use):
    print("ROSTER")
    for jersey_use, rating_use in sorted(roster_use.items()):
        print(f"Jersey number: {jersey_use}, Rating: {rating_use}")


roster = {}
for i in range(1, 6):
    jersey = int(input(f"Enter player {i}'s jersey number:\n"))
    rating = int(input(f"Enter player {i}'s rating:\n\n"))
    roster[jersey] = rating

print_roster(roster)

menu = {
    'a': "Add player",
    'd': "Remove player",
    'u': "Update player rating",
    'r': "Output players above a rating",
    'o': "Output roster",
    'q': "Quit\n"
}

while True:
    print("\nMENU")
    for option, description in menu.items():
        print(f"{option} - {description}")
    choice = input("Choose an option:\n")

    if choice == 'o':
        print_roster(roster)
    elif choice == 'a':
        new_jersey = int(input("Enter a new player's jersey number:\n"))
        new_rating = int(input("Enter the player's rating:\n"))
        roster[new_jersey] = new_rating
    elif choice == 'd':
        jersey_to_remove = int(input("Enter a jersey number:\n"))
        if jersey_to_remove in roster:
            del roster[jersey_to_remove]
    elif choice == 'u':
        jersey_to_update = int(input("Enter a jersey number:\n"))
        if jersey_to_update in roster:
            new_rating = int(input("Enter a new rating for player:\n"))
            roster[jersey_to_update] = new_rating
    elif choice == 'r':
        rating_threshold = int(input("Enter a rating:\n"))
        print(f"ABOVE {rating_threshold}")
        for jersey, rating in sorted(roster.items()):
            if rating > rating_threshold:
                print(f"Jersey number: {jersey}, Rating: {rating}")
    elif choice == 'q':
        break
