'''
05-06 Prove Asignment
Jordan Kraude
CSE 111
2/08/2021

Purpose: To excercise making and using functions
'''
from tkinter import Tk, Frame, Canvas, BOTH
# I deleted most of the small instruction comments because honestly
# they were bugging me quite a bit. It was very untidy as more
# and more kept gettting added.
import random
def main():
    width = 800
    height = 500

    # Create the root Tk object.
    root = Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = Frame()
    frame.master.title("Scene")
    frame.pack(fill=BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.

    # Sky call
    sky_height = 0
    sky_left = scene_left
    draw_sky(canvas, sky_left, sky_height)

    # Moon call
    left = scene_left - 50
    top = scene_top - 50
    height = 200
    draw_moon(canvas, left, top, height)

    # Ground call
    ground_height = 400
    ground_left = scene_left
    draw_ground(canvas, ground_left, ground_height)

    # Tree call
    tree_left = scene_left + 500
    tree_top = scene_top + 250
    tree_height = 150
    draw_pine_tree(canvas, tree_left, tree_top, tree_height)

    # Snow call
    draw_snow(canvas)

    # Cloud call
    cloud_left = scene_left + 200
    cloud_height = scene_top + 50
    draw_cloud(canvas, cloud_left, cloud_height)
    

   

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_pine_tree(canvas, peak_x, peak_y, height):
    # repeated element
    for i in range(int(random.uniform(50,10))):
        # I had to make x1 and y1 so that the trees could all be in
        # different places
        x1 = peak_x + random.choice(range(-450,300))
        y1 = peak_y + random.choice(range(0, 100))

        trunk_width = height / 14
        trunk_height = height / 8
        trunk_left = x1 - trunk_width / 2
        trunk_right = x1 + trunk_width / 2
        trunk_bottom = y1 + height

        skirt_width = height / 2
        skirt_height = height
        skirt_left = x1 - skirt_width / 2
        skirt_right = x1 + skirt_width / 2
        skirt_bottom = y1 + skirt_height

        # I decided to not show the ouline or trunks because
        # it would mess up the picture meaning it would make it look worse.
        # This way collision doesn't matter for the trees. It all blends

        # Draw the trunk of the pine tree.
        # canvas.create_rectangle(trunk_left, skirt_bottom,
                #trunk_right, trunk_bottom,
                #outline="gray20", width=1, fill="tan4")

        # Draw the crown (also called skirt) of the pine tree.
        canvas.create_polygon(x1, y1,
                skirt_right, skirt_bottom,
                skirt_left, skirt_bottom,
                outline=None, width=1, fill="dark green")
    

#Function for the sky
def draw_sky(canvas, pixels_x, height):
    sky_left = pixels_x
    sky_right = pixels_x + 800
    sky_top = height
    sky_bottom = height + 400
    # Draw the basic rectangle for the sky
    canvas.create_rectangle(sky_left, sky_top,
            sky_right, sky_bottom, 
            outline ="gray20", width=1, fill="black")

#Function for the cloud    
def draw_cloud(canvas, pixels_x, height):
    # repeated element
    for i in range(int(random.uniform(0,100))):
        color_bank = ['white', 'lightgray']
        x1 = random.choice(range(100, 700))
        x2 = x1 + random.choice(range(150, 300))
        y1 = random.choice(range(0, 100))
        y2 = y1 + random.choice(range(25, 50))
        color = random.choice(color_bank)
        canvas.create_oval(x1, y1,
            x2, y2,
            outline = 'white', width=1, fill= color)

#Function for the ground
def draw_ground(canvas, pixels_x, height):
    ground_left = pixels_x
    ground_right = pixels_x + 800
    ground_height = height
    ground_bottom = height + 100

    canvas.create_rectangle(ground_left, ground_height,
            ground_right, ground_bottom,
            outline = "gray", width=1, fill= "white")

def draw_snow(canvas):
    # Repeated element
    for i in range(int(random.uniform(0,3000))):
        x1 = random.choice(range(0,800))
        y1 = random.choice(range(0,500))
        x2 = x1 + 3
        y2 = y1 + 3
        canvas.create_oval(x1,y1,x2,y2,
        outline = 'white', width=1, fill = 'white')

def draw_moon(canvas, moon_left, moon_top, height):
    # element for the scene
    x1 = moon_left
    x2 = moon_left + height
    y1 = moon_top
    y2 = moon_top + height
    canvas.create_oval(x1,y1,x2,y2,
    outline = 'light gray', width=1, fill = 'white')

# call main function
main()