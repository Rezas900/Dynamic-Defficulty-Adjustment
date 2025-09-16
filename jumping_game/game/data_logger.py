import csv
import os

# A function for returns the specification of other obstcales
def get_next_obstacles_features(collided_obstacle, all_obstacles):
    
    # first we creat a list of other obstacles
    other_obstacles = [obs for obs in all_obstacles if obs != collided_obstacle]

    # default value 
    other_abs_dist1 = -1
    other_abs_height1 = -1
    other_abs_dist2 = -1
    other_abs_height2 = -1

    if len(other_obstacles) > 0:
        other_abs_dist1 = other_obstacles[0].rect.x
        other_abs_height1 = other_obstacles[0].rect.height

    if len(other_obstacles) > 1:
        other_abs_dist2 = other_obstacles[1].rect.x
        other_abs_height2 = other_obstacles[1].rect.height

    return [other_abs_dist1, other_abs_height1, other_abs_dist2, other_abs_height2]

# make a dierctory for savig the Logs:
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
root_of_game_dir = os.path.dirname(current_dir)
logs_dir = os.path.join(root_of_game_dir, 'Logs', "game_logs.csv")
os.makedirs(os.path.dirname(logs_dir), exist_ok=True)

# A function for saving game data to a CSV file
def save_game_data_to_csv(game_data):
    with open(logs_dir, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(game_data)