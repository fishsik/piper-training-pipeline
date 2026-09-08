import os
import json
import numpy as np
import soundfile as sf

def create_dummy_data():
    wav_dir = "dataset/preprocessed_wavs"
    os.makedirs(wav_dir, exist_ok=True)
    
    # 1초짜리 무음 생성 (16kHz, 모노)
    dummy_audio = np.zeros(16000, dtype=np.float32)
    dummy_path = os.path.join(wav_dir, "sample_001.wav")
    sf.write(dummy_path, dummy_audio, 16000, subtype='PCM_16')
    
    # dataset.jsonl 작성
    jsonl_path = "dataset/dataset.jsonl"
    data = {
        "audio_file": "wavs/sample_001.wav",
        "text": "This is a dry run test for the pipeline.",
        "speaker": 0
    }
    
    with open(jsonl_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")
        
    print("더미 데이터 생성 완료!")

if __name__ == "__main__":
    create_dummy_data()