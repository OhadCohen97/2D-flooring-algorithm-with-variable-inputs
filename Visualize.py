import matplotlib.pyplot as plt
import matplotlib.patches as patches
from random import random

#tool to visualize solution
def visualize(rectangles):
    fig = plt.figure()
    axes = fig.add_subplot(1, 1, 1)

    for idx, r in enumerate(rectangles):
        axes.add_patch(
            patches.Rectangle(
                (r.x, r.y),  # (x,y)
                r.w,  # width
                r.h,  # height
                fill=True,
                color=(random(), random(), random()),
            )
        )

    axes.text(r.x + 0.5 * r.w, r.y + 0.5 * r.h, str(idx))
    axes.set_xlim(0, 1000)
    axes.set_ylim(0, 1000)
    plt.show()
