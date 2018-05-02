import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])
plt.imshow(x, interpolation='nearest')

plt.show()

# example
# np.random.choice([0, 255], 4*4, p=[0.1, 0.9]).reshape(4, 4)


def add_glider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 255], [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i + 3, j:j + 3] = glider
    return grid


ON = 255
OFF = 0


# main() function
def main():
    # command line argumentss are in sys.argv[1], sys.argv[2], ...
    # sys.argv[0] is the script name and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    # add arguments
    parser.add_argument('--grid-size', dest='N', type=int, default=100, required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', default=50, type=int, required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    args = parser.parse_args()

    # set grid size
    N = max(args.N, 9)
    # TODO Start from here next time, page 48

    # set animation update interval
    if args.interval:
        update_interval = args.interval

    # declare grid
    grid = np.array([])
    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N * N).reshape(N, N)
        addGlider(1, 1, grid)
    else:
        # populate grid with random on/off - more off than on
        grid = randomGrid(N)