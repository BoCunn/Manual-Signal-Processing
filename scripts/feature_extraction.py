from pyexpat import features

import librosa
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import euclidean

def extract_features(audio, sr):
    """
    Extract features from an audio signal.

    Parameters:
    - audio: np.ndarray, the audio time series
    - sr: int, the sampling rate of the audio

    Returns:
    - features: dict, a dictionary containing extracted features
    """
    features = {}
    
    # Display Waveform
    librosa.display.waveshow(y=audio, sr=sr)
    plt.title('Waveform of Audio')
    plt.show(block=False)
    
    # Extract RMS
    RMS = librosa.feature.rms(y=audio)
    features['RMS'] = RMS
    
    # Extract Zero Crossing Rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio)
    features['Zero Crossing Rate'] = zero_crossing_rate
    
    # Extract Short Time Energy
    frame_length = 2048  # same used for RMS
    STE = (RMS.flatten() ** 2) * frame_length
    features['Short Time Energy'] = STE



    return features