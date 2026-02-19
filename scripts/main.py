from load_audio import load_audio
from display import display_features
<<<<<<< HEAD
=======
from feature_extraction import extract_features
from manualFeatures import Extract_Manual
>>>>>>> master

# Load the audio file
music, sr = load_audio('data/testAudio.mp3', offset=81, duration=10)

<<<<<<< HEAD
=======
# Extract features
features = extract_features(music, sr)

# Extract manual features
Manfeatures = Extract_Manual(music)

# Display features
display_features(features, Manfeatures)

>>>>>>> master
