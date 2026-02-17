import numpy as np
import matplotlib.pyplot as plt

def display_features(features):
    
    for key, value in features.items():
        if isinstance(value, np.ndarray):
            plt.figure(figsize=(10, 5))
            plt.title(f"{key} Feature")
            plt.xlabel('Time Frames')
            plt.ylabel('Hz')
            plt.plot(value.flatten())
            plt.show(block=False)
        else:
            print(f"{key}: {value}")
    plt.pause(0.1)  # Pause to allow plots to render
    plt.show()  # Keep all plots open until closed by the user


    