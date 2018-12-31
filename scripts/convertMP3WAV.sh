#!/bin/bash
if [ $# -lt 2 ]; then
    echo "mp3ToWAV in.mp3 out.wav"
else
    ffmpeg -i $1 $2
fi
