import librosa
def load_audio(file_path, offset, duration):
    """
    Load an audio file using librosa.

    Parameters:
    - file_path: str, path to the audio file
    - offset: float, start reading after this time (in seconds)
    - duration: float, only load up to this much audio (in seconds)

    Returns:
    - music: np.ndarray, the audio time series
    - sr: int, the sampling rate of the audio
    """
    music, sr = librosa.load(file_path, sr=None, mono=True, offset=offset, duration=duration)
    return music, sr