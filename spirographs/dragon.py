import turtle
import math

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
            #self.turtle.hideturtle()
