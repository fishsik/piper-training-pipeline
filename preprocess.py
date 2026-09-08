import os
import librosa
import soundfile as sf

def preprocess_audio(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith(".wav"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # 16kHz 모노로 강제 변환
            y, sr = librosa.load(input_path, sr=16000, mono=True)
            sf.write(output_path, y, 16000, subtype='PCM_16')

if __name__ == "__main__":
    preprocess_audio("dataset/raw_wavs", "dataset/preprocessed_wavs")