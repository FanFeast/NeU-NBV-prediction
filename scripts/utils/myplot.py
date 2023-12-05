import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import os
import argparse

# Set the font sizes and line width here if needed, or remove/comment out if not required
PLOT_FONT_SIZE = 22
PLOT_LEGEND_SIZE = 18
PLOT_TICKS_SIZE = 18
PLOT_LINE_WIDTH = 4

plt.rcParams["figure.figsize"] = [12, 8]
plt.rcParams["figure.autolayout"] = True
sb.set_palette("bright")

def plot(dataframe_path):
    # Check if the dataframe exists
    if not os.path.exists(dataframe_path):
        raise FileNotFoundError("dataframe does not exist!")
    
    # Read the dataframe
    total_df = pd.read_csv(dataframe_path)
    
    # Create the plot
    sb.lineplot(
        data=total_df,
        x="Reference Image Number",
        y="PSNR",
        hue="Planning Type",
        linewidth=PLOT_LINE_WIDTH
    )
    
    # Set axis labels and save the plot
    plt.xlabel("Number of collected images", fontsize=PLOT_FONT_SIZE)
    plt.ylabel("PSNR", fontsize=PLOT_FONT_SIZE)
    plt.savefig(os.path.join(os.path.dirname(dataframe_path), "plot_results.svg"), bbox_inches="tight")
    plt.clf()

# Assume the dataframe_path is provided as an argument
# dataframe_path = "/home/ubuntu/nbv-prediction/scripts/experiments/dtu/04-12-2023-18-38/dataframe.csv"  # Replace with your actual path
# dataframe_path = "/home/ubuntu/nbv-prediction/scripts/experiments/dtu/04-12-2023-18-44/dataframe.csv"  # Replace with your actual path
dataframe_path = "/home/ubuntu/nbv-prediction/scripts/experiments/dtu/05-12-2023-02-48 _DTU_MOdel_on_US/dataframe.csv"

plot(dataframe_path)
