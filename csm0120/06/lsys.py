"""
A module for drawing fractals with L-systems, using matplotlib.
Illustrates plotting, dictionaries, strings, loops, functions and a class.
"""

import lsys
import matplotlib.pyplot as plt
import math

# The angle for each turn, which is a constant
theta = math.radians(60)


def lsystem(axiom, rules, iterations):
    """Expand an axiom using the rules, for several iterations"""
    current_commands = axiom
    for i in range(iterations):
        new_commands = ""
        for c in current_commands:
            if c in rules:
                new_commands += rules[c]
            else:
                new_commands += c
        current_commands = new_commands
    return current_commands


def forward(pos):
    (x,y,direction) = pos
    x = x + math.cos(direction)
    y = y + math.sin(direction)
    return (x, y, direction) 

def turn_right(pos):
    (x,y,direction) = pos
    direction = (direction - theta) % ((math.pi) * 2)
    return (x, y, direction) 

def turn_left(pos):
    (x,y,direction) = pos
    direction = (direction + theta) % ((math.pi) * 2)
    return (x, y, direction)



def interpret_commands(command_string):
    """Takes a string and converts it into the corresponding x and y locations"""
    x_posns = []
    y_posns = []
    now = (0, 0, 0) # x, y, direction at start
    
    for c in command_string:
        if c == "F":
            new_pos = forward(now)
            x_posns.append(new_pos[0])
            y_posns.append(new_pos[1])
        elif c == "+":
            new_pos = turn_right(now)
        elif c == "-":
            new_pos = turn_left(now)
        else:
            pass # do nothing
        now = new_pos
    
    return (x_posns, y_posns)




def plot_results(x_posns, y_posns):
    """Plots the final path"""
    plt.plot(x_posns, y_posns)
    pass



if __name__ == "__main__":

    # sierpinski
    axiom = 'FX+'
    rules = {
       'X': 'YF+XF+Y',
       'Y': 'XF-YF-X'
       }
    iterations = 3

    # Run the l-system to produce a final command string
    command_string = lsystem(axiom, rules, iterations)

    # Interpret the commands to produce x and y locations showing where we moved
    (x_posns, y_posns) = interpret_commands(command_string)

    # Plot the path taken by the final positions
    plot_results(x_posns, y_posns)
