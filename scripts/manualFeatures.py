import numpy as np

#Manual Extraction of Features from Signals


#Manual RMS
def Extract_Manual(audio, frame_size=2048, hop_length=512):
  
    Manfeatures = {}
    
    rms = []
    for i in range(0, len(audio) - frame_size, hop_length):
        frame = audio[i:i + frame_size]
        rms.append(np.sqrt(np.mean(frame ** 2)))
    Manfeatures["Manual RMS"] = np.array(rms)


    zcr=[]
    for i in range(0, len(audio) - frame_size, hop_length):
        frame = audio[i:i + frame_size]
        
        if len(frame) < frame_size:
            frame = np.pad(frame, (0, frame_size - len(frame)))

        zero_crossings = np.sum(np.abs(np.diff(np.sign(frame))))/2
        zcr.append(zero_crossings / len(frame))
    Manfeatures["Manual ZCR"] = np.array(zcr)    


    ste=[]

    for i in range(0, len(audio), hop_length):
        frame = audio[i:i + frame_size]
        
        if len(frame) < frame_size:
            frame = np.pad(frame, (0, frame_size - len(frame)))

        stel=np.sum(frame ** 2)
        ste.append(stel)
        
    Manfeatures["Manual STE"] = np.array(ste)

    return Manfeatures