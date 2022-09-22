import os
import random

from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.rock import Rock
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 10


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = 580
    position = Point(x, y)

    userControl = Actor()
    userControl.set_text("#")
    userControl.set_font_size(FONT_SIZE)
    userControl.set_color(WHITE)
    userControl.set_position(position)
    cast.add_actor("user", userControl)
    
    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
        text_for_gem = "*"
        text_for_rock = "O"
        message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position1 = Point(x, y)
        position = position.scale(CELL_SIZE)
        position1 = position1.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gem = Gem()
        gem.set_text(text_for_gem)
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)
        gem.set_message(message)
        cast.add_actor("gems", gem)

        rock = Rock()
        rock.set_text(text_for_rock)
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position1)
        rock.set_message(message)
        cast.add_actor("rocks", rock)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()