import librosa
import matplotlib.pyplot as plt
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
    
    # Extract Spectral Centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)
    features['Spectral Centroid'] = spectral_centroid
    
    # Extract Zero Crossing Rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio)
    features['Zero Crossing Rate'] = zero_crossing_rate
    
    # Extract Spectral Flatness
    spectral_flatness = librosa.feature.spectral_flatness(y=audio)
    features['Spectral Flatness'] = spectral_flatness
    
    # Caluclate Euclidean distance between Spectral Flatness an dSPectral Centroid:
    distance = euclidean(spectral_flatness.flatten(), spectral_centroid.flatten())
    features['Euclidean Distance'] = distance
  
    return features