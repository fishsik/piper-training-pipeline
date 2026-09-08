#!/bin/bash

# 학습 파라미터 설정
DATASET_DIR="dataset/custom_english_speaker"
OUTPUT_DIR="output/checkpoint"
ACCELERATOR="cuda" # GPU 활용

python3 -m piper_train \
    --dataset-dir "$DATASET_DIR" \
    --accelerator "$ACCELERATOR" \
    --devices 1 \
    --batch-size 32 \
    --validation-split-ratio 0.05 \
    --max-epochs 1000 \
    --checkpoint-dir "$OUTPUT_DIR"