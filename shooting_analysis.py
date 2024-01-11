
import numpy as np
import matplotlib.pyplot as plt

# create empty/zeros array of x, y coordinates
data = np.zeros((30,2))

# experiment data, for participant number and which sight type they were using 
partic = str(input('Enter the participent number: '))
sight = str(input('Easyhit or iron? '))

cont = 'y'
shots = 0

# whilst true, loop through data input to enter all shot coordinates
# improvement here to use pandas and read directly from an input file
# improvment wasn't made as shot coordinates were calculated by hand then inputted directly 

while cont == 'y':
    
    shots += 1
    print('bullet ' +str(shots))
    x = float(input('Enter x co-ordinate : '))
    y = float(input('Enter y co-ordinate : '))


    # load shot coordinates to array
    # this could have been done in the input line, but kept seperate for ease of reference to the researcher
    data[shots-1,0]=x
    data[shots-1,1]=y

    # information for data inputter, and break condition
    print("You have added " + str(shots) + " shots")
    cont = str(input('Would you like to add another shot? y/n '))

# mean average coordinates, saves as 2 point array, sum calculated on each coloumn of shot array
av = np.sum(data, axis=0)/shots


print('The average co-ordinates are: ' +str(av))

av_dist_added_late = []
#greatest and smallest distance from average
dist_large = 0
dist_low = 100

# counter variable to track loop
rowat = 0
for row in data:

    # 0,0 is deemed a miss and is removed from average calculations
    if row[0] == 0 and row[1] == 0:
        data = np.delete(data, rowat, axis=0)

    else:

        x_sep = av[0] - row[0]
        y_sep = av[1] - row[1]

        plt.plot(row[0], row[1], 'x', color='R')

        # calculate straight line distance from centre to shot and add to list
        dist = np.sqrt((y_sep **2) + (x_sep **2))
        av_dist_added_late.append(dist)

        rowat += 1

        # correct max and min spread of shots
        # improvement, this did not need to be a re-written variable, we could call max() and min() on the list of distances
        if dist > dist_large:
        
            dist_large = dist
    
        elif dist < dist_low:
        
            dist_low = dist

# print data points for reseracher to read
averagedistance = (np.sum(av_dist_added_late))/shots
print('Largest distance from the average shot is: ' +str(dist_large))
print('Smallest distance from the average shot is: ' +str(dist_low))
print('Average distance from the average shot is: ' +str(averagedistance))



# plot shots and average

# plot average shot to output graph and define limits of graph
plt.ylim(bottom = 0, top = 200)
plt.xlim(left = 0, right = 200)
plt.plot(av[0], av[1], 'o', color='B')


# target rings
# define cirlces on the graph that match scoring rings on a shooting target. This is to make the graph look like the real targets 
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

# define circles for the avrage shot grouping and maximum grouping
group = plt.Circle((av[0], av[1]), dist_large, color = 'r', fill = False)
avgroup = plt.Circle((av[0], av[1]), averagedistance, color = 'b', fill = False)

# actually print calculated lines and points
plt.gcf().gca().add_artist(avgroup)
plt.gcf().gca().add_artist(group)
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
plt.title('Participant number: ' +str(partic)+' Sight type: ' +sight)

# export graph to file that can be used in research paper/poster
filename = 'participent_'+str(partic)+'_sight_'+sight+'.png'
plt.savefig(filename)

# display graph for analysis 
plt.show()
