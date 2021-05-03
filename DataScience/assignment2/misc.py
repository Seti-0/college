import matplotlib.pyplot as plt
from matplotlib import rcParams
import os


# This is to prevent labels being cut off when
# saving figures as images on the disk.
rcParams.update({'figure.autolayout': True})

# This is the folder to which all charts will be
# saved.
SAVE_DIR = "charts"
    
    
def plt_save(name, parent = None):
    """
    Save the current matplotlib figure to
    the save dir in the form "name_kind.png"
    
    If a parent path is given, save to that
    subfolder of the save dir.
    """
    
    # Add the save_dir to the parent path
    
    if parent is None:
        parent = SAVE_DIR
    else:
        parent = SAVE_DIR + "/" + parent
    
    # Try to ensure that the target path exists.
    
    # If there is an exception here, it is most likely
    # because the path does already exist.
    
    try:
        os.makedirs(parent)
    except:
        pass
    
    # Create the path and save the figure.
    
    path = f"{parent}/{name}.png"
    
    plt.savefig(path)
 
    