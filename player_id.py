import csv
import os

def save_player_data():
    # File name to store the player data
    file_name = "player_data.csv"

    # Ask the user for their in-game name and player ID
    in_game_name = input("Enter your in-game name: ")
    player_id = input("Enter your player ID: ")

    # Check if the file exists
    file_exists = os.path.exists(file_name)

    # Open the file in append mode
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the header only if the file is new
        if not file_exists:
            writer.writerow(["In-Game Name", "Player ID"])

        # Write the in-game name and player ID to the file
        writer.writerow([in_game_name, player_id])

    print(f"Player data (Name: '{in_game_name}', ID: '{player_id}') has been saved.")


save_player_data()
