import os, shutil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from PIL import Image

#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

#Number of frames, figure and axis size, and output directory
num_frames = 50 
fig, ax = plt.subplots(figsize=(5,6)) 
output_dir = "frames"

#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

#Creation of directory if it doesn't exist
def set_directory():
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

#Canvas Properties (Ticks, Border, Background Color)
def setCanvasProperties(ax):
    #fig = ax.figure
    #fig.set_facecolor("black")
    rgba_color = (45/255, 36/255, 37/255, 1)
    ax.set_facecolor(rgba_color)

    # Remove ticks, labels and border
    ax.set_xticks([])
    ax.set_yticks([])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

#Image open, resize, and array parameters
def init():
    return []

image = Image.open('PE.jpg')
image = image.resize((100,100)) #ONLY WORKS IF (100,100), DO NOT CHANGE
npimage = np.array(image)/255.0

#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

#Animation Parameters
def animate(frame, ax, npimage, canvas):
    width, height, _ = npimage.shape

    # Set limits according to the image size
    #ax.set_xlim(0, width) #Doesn't work, keep just in case
    #ax.set_ylim(0, height)

    for _ in range(600):
        w = np.random.randint(0, width)
        h = np.random.randint(0, height)

        radius = np.random.rand()*1

        w = np.clip(w, 0, width - 1)
        h = np.clip(h, 0, height - 1)
        
        print(w,h, image.getpixel((w,h)), radius)

        color = npimage[h, w]

        circle = Circle((w, height - h), radius, color=color, alpha=0.7)
        ax.add_patch(circle)

    #Save File/Frame Function
    filename = os.path.join(output_dir, f"{frame+1:04d}.jpg")
    plt.savefig(filename, 
                bbox_inches='tight', 
                pad_inches=0.1,
                dpi=100)
    
    canvas.draw()
    return ax.patches

#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

#Main Function
def main(ax, canvas):
    set_directory()
    setCanvasProperties(ax)

    anim = FuncAnimation(ax.figure, animate, init_func=init,
                        fargs=(ax, npimage, canvas),
                        frames=num_frames, interval=0,
                        blit=False, repeat=False)

    return anim
    plt.show()


