import os
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as anime

#Need to get the list of participants from zoom
file_path = 'participants.csv'

with open(file_path,'r') as f:
	reader_obj = csv.reader(f)
	names = [i for i in reader_obj]

#To get true os level random value
_random = list(os.urandom(1))[0]
# print(_random)
_random = int(round(_random * (len(names)-1)/255))
# print(_random,names)

print('The winner of Gift card is:',names[_random][0])

#Setting up the plot
figure = plt.figure(figsize = (12,8))
disp_text = 'Congratulations the winner of gift card is:\n'+names[_random][0]
figure.set_facecolor('black')
axis = figure.add_axes([0,0,1,1])
axis.set_facecolor('black')
text_obj = axis.text(0.5, 0.5, disp_text ,horizontalalignment='center',verticalalignment='center',fontsize=36,c='black')

#Colors offsets for smooth animation
red_offset = 0
green_offset = 192
blue_offset = 64

#Function defined for animation
def winner(i):
    """ Returns a text objct for animation """
    
    #Changing color Values
    colors_red = ((4 * i + red_offset)%256)/256
    colors_green = ((2 * i + green_offset )%256)/256
    colors_blue = (( i + blue_offset)%256)/256
    colors = (colors_red,colors_green,colors_blue)
    
    #Setting up change in color values
    text_obj.set_color(color=colors)
    
    return text_obj,

#Animation
winner_disp = anime.FuncAnimation(figure,winner,frames=100,interval=0.1,blit=True)
winner_disp.save('winner.gif', fps=30)
plt.show()
