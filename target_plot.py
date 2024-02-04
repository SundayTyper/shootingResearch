""" Module to plot given data to target shaped graphs. Relies on matplotlib """
import matplotlib.pyplot as plt


class TargetPlot:
    """ Class creates a target shaped plot using matplotlib and marks data on it """

    def __init__(self, participant, sights):

        self.participant = participant
        self.sights = sights

        # define plot boundaries and size
        plt.ylim(bottom = 0, top = 200)
        plt.xlim(left = 0, right = 200)

        # define cirlces on the graph that match scoring rings on a shooting target.
        # This is to make the graph look like the real targets
        # Cirles are defined by 'centre point', 'radius', 'fill'
        ring1 = plt.Circle((100,100), 76, fill = False)
        ring2 = plt.Circle((100,100), 68, fill = False)
        ring3 = plt.Circle((100,100), 60, fill = False)
        ring4 = plt.Circle((100,100), 52, fill = False)
        ring5 = plt.Circle((100,100), 44, fill = False)
        ring6 = plt.Circle((100,100), 36.5, fill = False)
        ring7 = plt.Circle((100,100), 28.5, fill = False)
        ring8 = plt.Circle((100,100), 20.5, fill = False)
        ring9 = plt.Circle((100,100), 13, fill = False)
        ring10 = plt.Circle((100,100), 5, fill = False)

        # add rings to plot
        plt.gcf().gca().add_artist(ring1)
        plt.gcf().gca().add_artist(ring2)
        plt.gcf().gca().add_artist(ring3)
        plt.gcf().gca().add_artist(ring4)
        plt.gcf().gca().add_artist(ring5)
        plt.gcf().gca().add_artist(ring6)
        plt.gcf().gca().add_artist(ring7)
        plt.gcf().gca().add_artist(ring8)
        plt.gcf().gca().add_artist(ring9)
        plt.gcf().gca().add_artist(ring10)

        # add graph title
        plt.title('Participant number: ' +str(participant)+' Sight type: ' +sights)


    def plot_participant_data(self, average_shot, shots_x_coordinates, shots_y_coordinates):
        """ plot the participant data to the graph """

        # plot average shot to output graph. Plot as dot
        plt.plot(average_shot[0], average_shot[1], 'o', color='b')

        distance_from_average_list = []
        # add each shot to the graph
        for i, value in enumerate(shots_x_coordinates):
            x_sep = average_shot[0] - shots_x_coordinates[i]
            y_sep = average_shot[1] - shots_y_coordinates[i]
            plt.plot(shots_x_coordinates[i], shots_y_coordinates[i], 'x', color='r')
            # calculate seperation from centre point
            distance = ((y_sep **2) + (x_sep **2))**0.5
            distance_from_average_list.append(distance)

        shortest_distance_from_average = round(min(distance_from_average_list), 1)
        furthest_distance_from_average = round(max(distance_from_average_list), 1)
        average_distance_from_average = round(sum(distance_from_average_list)/len(distance_from_average_list), 1)


        # define circles for the average shot grouping and maximum grouping, add to plot
        grouping = plt.Circle((average_shot[0], average_shot[1]), furthest_distance_from_average,
                                color = 'r', fill = False)
        avgrouping = plt.Circle((average_shot[0], average_shot[1]), average_distance_from_average,
                                color = 'b', fill = False)
        plt.gcf().gca().add_artist(grouping)
        plt.gcf().gca().add_artist(avgrouping)

        # print some information for the researcher
        print(f"Participant {self.participant}'s largest distance from the average shot is: {str(furthest_distance_from_average)}")
        print(f"Participant {self.participant}'s smallest distance from the average shot is: {str(shortest_distance_from_average)}")
        print(f"Participant {self.participant}'s average distance from the average shot is: {str(average_distance_from_average)}")

    def save_plot_and_teardown(self):
        """ export graph to file that can be used in research paper/poster """
        filename = 'participent_'+str(self.participant)+'_sight_'+self.sights+'.png'
        plt.savefig(filename)
        plt.clf()
