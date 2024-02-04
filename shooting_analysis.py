""" Analyse data from experiment and produce graphed interpretations based on data provided """
from get_data_set import GetDataSet
from target_plot import TargetPlot
from analysis_functions import validate_input, extract_data_points

def main():
    """ bring together other modules and functions to create a working script """

    csv_file = validate_input()
    data_set = GetDataSet(csv_file)

    for result in data_set.data_set:
        average_shot, participant, sights, shots_x_coordinates, shots_y_coordinates = extract_data_points(result)
        plot = TargetPlot(participant, sights)
        plot.plot_participant_data(average_shot, shots_x_coordinates, shots_y_coordinates)
        plot.save_plot_and_teardown()

if __name__ == "__main__":
    main()
