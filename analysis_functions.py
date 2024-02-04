""" functions to be used in the main file """
import sys

def validate_input():
    """ Return error if data input file not provided. Return file path """
    if len(sys.argv) != 2:
        sys.exit("Please provide a csv file containing your data")
    return sys.argv[1]

def extract_data_points(data_row):
    """ Extract data points to variables from csv row entry. Calculate the average shot """
    participant = data_row[0]
    sights = data_row[1]
    shots_x_coordinates = []
    shots_y_coordinates = []
    for shot in data_row[2:]:
        if shot:
            coordinates = shot.split('-')
            try:
                shots_x_coordinates.append(float(coordinates[0]))
            except:
                pass
            try:
                shots_y_coordinates.append(float(coordinates[1]))
            except:
                pass
    average_x_coordinate = sum(shots_x_coordinates)/len(shots_x_coordinates)
    average_y_coordinate = sum(shots_y_coordinates)/len(shots_y_coordinates)
    return [average_x_coordinate, average_y_coordinate], participant, sights, shots_x_coordinates, shots_x_coordinates
