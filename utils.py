import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Create folder if not exist
def createFolder(directory) -> None:
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

# Use Canvas to convert figure to image
def figure_to_image(fig):
    canvas = FigureCanvas(fig)
    canvas.draw()
    width, height = canvas.get_width_height()
    img = np.frombuffer(canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)
    return img

# Merge two plots and save the result
def coomparePlotAndSafe(plt_prev, plt_after, save_path) -> None:
    img_prev = figure_to_image(plt_prev)
    img_after = figure_to_image(plt_after)

    fig, axs = plt.subplots(1, 2, figsize=(15, 6))
    axs[0].imshow(img_prev)
    axs[0].set_title('Before filling')
    axs[0].axis('off')
    axs[1].imshow(img_after)
    axs[1].set_title('After filling')
    axs[1].axis('off')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()