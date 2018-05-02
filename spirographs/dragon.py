import turtle
import math
import random

class Spiro:
    def __init__(self, x_coordinate, y_coordinate, pen_color, large_radius, small_radius, offset_ratio, step_size, fill_color = ""):
        self.turtle = turtle.Turtle()
        turtle.register_shape('Spyro.gif')
        self.turtle.shape('Spyro.gif')
        self.turtle.color(pen_color, fill_color)

        self.x_coordinate = x_coordinate  # this is xc
        self.y_coordinate = y_coordinate  # this is yc
        self.large_radius = int(large_radius)  # this is R
        self.small_radius = int(small_radius)  # this is r
        self.offset_ratio = offset_ratio  # this is l
        self.step_size = step_size  # this is not in the book

        self.rotations = self.small_radius//math.gcd(self.small_radius, self.large_radius)  # this is nRot
        self.radii_ratio = self.small_radius / self.large_radius  # this is k

        self.drawing_complete = False
        self.current_angle = 0

        self.restart()

    def restart(self):
        self.drawing_complete = False
        self.current_angle = 0
        self.turtle.showturtle()
        self.turtle.up()
        self._set_pos()
        self.turtle.down()

    def _set_pos(self):
        x = self.calculate_x()
        y = self.calculate_y()
        self.turtle.setpos(self.x_coordinate + x, self.y_coordinate + y)

    def calculate_x(self):
        return self.large_radius * ( (1 - self.radii_ratio) * math.cos(self.current_angle) + self.offset_ratio * self.radii_ratio * math.cos((1 - self.radii_ratio) * self.current_angle/self.radii_ratio) )

    def calculate_y(self):
        return self.large_radius * ( (1 - self.radii_ratio) * math.sin(self.current_angle) - self.offset_ratio * self.radii_ratio * math.sin((1 - self.radii_ratio) * self.current_angle/self.radii_ratio) )

    def draw(self):
        large_radius, radii_ratio, offset_ratio = self.large_radius, self.radii_ratio, self.offset_ratio

        for i in range(0, 360*self.rotations + 1, self.step_size):
            self.current_angle = math.radians(i)
            self._set_pos()
        self.turtle.hideturtle()

    def update(self):
        #skip the rest of the steps if done
        if self.drawing_complete:
            return
        #increment the angle
        self.current_angle += math.radians(self.step_size)
        #draw a step
        self._set_pos()
        #if drawing is complete, set flag
        if self.current_angle >= math.pi*2*self.rotations:
            self.drawing_complete = True
            self.turtle.hideturtle()

class SpiroAnimator:
    # constructor
    def __init__(self, N):
        # set the timer value in milliseconds
        self.deltaT = 10
        # get the window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # create the Spiro objects
        self.spiros = []
        for i in range(N):
            # generate random parameters
            rparams = self.generate_random_params()
            # set the spiro parameters
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            # call timer
            turtle.ontimer(self.update, self.deltaT)

    # generate random parameters
    def generate_random_params(self):
        width, height = self.width, self.height
        large_radius = random.randint(50, min(width, height)//2)  # Large radius
        small_radius = random.randint(10, 9*large_radius//10)  # small radius
        offset_ratio = random.uniform(0.1, 0.9)  # offset ratio
        x_coordinate = random.randint(-width//2, width//2)  # x coordinate
        y_coordinate = random.randint(-height//2, height//2)  # y coordinate
        step_size = random.randint(5, 20)
        pen_color = (random.random(),
               random.random(),
               random.random())
        return (x_coordinate, y_coordinate, pen_color, large_radius, small_radius, offset_ratio, step_size)

    # restart sprio drawing
    def restart(self):
        for spiro in self.spiros:
            spiro.restart()

    def update(self):
        # update all spiros
        nComplete = 0
        for spiro in self.spiros:
            # update
            spiro.update()
            # count completed ones
            if spiro.drawing_complete:
                nComplete += 1
        # if all spiros are complete, restart
        if nComplete != len(self.spiros):
            turtle.ontimer(self.update, self.deltaT)

# TODO add countdown
# TODO only draws two at a time
# TODO use multiple cores
# TODO note page 27

# Project consdidered complete as of 05/02/18