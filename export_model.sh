#!/bin/bash
# export_model.sh

OUTPUT_DIR="output/checkpoint"

python3 -m piper_train.export \
    --checkpoint "$OUTPUT_DIR/lightning_logs/version_0/checkpoints/last.ckpt" \
    --output-dir "output/onnx"

print "ONNX export completed!"