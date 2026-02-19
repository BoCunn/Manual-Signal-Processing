import numpy as np
import matplotlib.pyplot as plt

def display_features(features, Manfeatures):

    for key, value in features.items():
        if isinstance(value, np.ndarray):
            plt.figure(figsize=(10, 5))
            plt.title(f"{key} Feature")
            plt.xlabel('Time Frames')
            plt.ylabel('Value')  # not Hz unless it's frequency
            plt.plot(value.flatten())
        else:
            print(f"{key}: {value}")

    for key, value in Manfeatures.items():
        if isinstance(value, np.ndarray):
            plt.figure(figsize=(10, 5))
            plt.title(f"{key} Feature")
            plt.xlabel('Time Frames')
            plt.ylabel('Value')
            plt.plot(value.flatten())
        else:
            print(f"{key}: {value}")

    plt.show()   # BLOCKS and keeps all plots open
