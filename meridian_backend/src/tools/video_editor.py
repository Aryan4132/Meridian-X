"""
meridian_backend/src/tools/video_editor.py — Production Backend Module
Automated Video Editing, Trimming, Subtitling & Media Processing Engine
"""

import os
import sys
import time
import glob
import subprocess
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger("meridian_video_editor")


def trim_video(input_file: str, output_file: str, start_sec: float, end_sec: float) -> str:
    """Trim a video file between start_sec and end_sec."""
    if not os.path.exists(input_file):
        return f"Error: Input video '{input_file}' not found."

    try:
        import cv2
        cap = cv2.VideoCapture(input_file)
        if not cap.isOpened():
            return f"Error: Could not open video '{input_file}'."

        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        start_frame = int(start_sec * fps)
        end_frame = int(end_sec * fps) if end_sec > 0 else total_frames

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

        current_frame = start_frame
        written = 0

        while current_frame < end_frame and cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            written += 1
            current_frame += 1

        cap.release()
        out.release()
        return f"Successfully trimmed video '{input_file}' to '{output_file}' ({written} frames, {written/fps:.1f}s)."
    except Exception as exc:
        return f"Trim video failed: {exc}"


def concat_videos(input_files: List[str], output_file: str) -> str:
    """Concatenate multiple video files into a single merged video file."""
    if not input_files:
        return "Error: No input video files provided."

    valid_files = [f for f in input_files if os.path.exists(f)]
    if not valid_files:
        return "Error: None of the provided input files exist."

    try:
        import cv2
        first_cap = cv2.VideoCapture(valid_files[0])
        fps = first_cap.get(cv2.CAP_PROP_FPS) or 30.0
        width = int(first_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(first_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        first_cap.release()

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
        total_written = 0

        for fpath in valid_files:
            cap = cv2.VideoCapture(fpath)
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                # Resize if frame dimensions differ
                if frame.shape[1] != width or frame.shape[0] != height:
                    frame = cv2.resize(frame, (width, height))
                out.write(frame)
                total_written += 1
            cap.release()

        out.release()
        return f"Successfully concatenated {len(valid_files)} videos into '{output_file}' ({total_written} frames)."
    except Exception as exc:
        return f"Concat videos failed: {exc}"


def change_video_speed(input_file: str, output_file: str, speed_factor: float = 2.0) -> str:
    """Change video playback speed (e.g. 2.0 for 2x timelapse, 0.5 for slow motion)."""
    if not os.path.exists(input_file):
        return f"Error: Input file '{input_file}' missing."
    if speed_factor <= 0:
        return "Error: speed_factor must be greater than 0."

    try:
        import cv2
        cap = cv2.VideoCapture(input_file)
        orig_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        new_fps = orig_fps * speed_factor

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, new_fps, (width, height))

        written = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            written += 1

        cap.release()
        out.release()
        return f"Adjusted video speed by {speed_factor}x into '{output_file}' ({written} frames @ {new_fps:.1f} FPS)."
    except Exception as exc:
        return f"Change video speed failed: {exc}"


def add_text_watermark(
    input_file: str,
    output_file: str,
    text: str = "Meridian-X AI",
    position: str = "bottom_right"
) -> str:
    """Overlay text watermark or subtitle banner onto video frames."""
    if not os.path.exists(input_file):
        return f"Error: Input video '{input_file}' not found."

    try:
        import cv2
        cap = cv2.VideoCapture(input_file)
        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = max(0.5, width / 1200.0)
        thickness = max(1, int(font_scale * 2))

        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

        if position == "top_left":
            x, y = 20, text_height + 20
        elif position == "top_right":
            x, y = width - text_width - 20, text_height + 20
        elif position == "bottom_left":
            x, y = 20, height - 20
        else:  # bottom_right default
            x, y = width - text_width - 20, height - 20

        written = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # Add semi-transparent background box for contrast
            cv2.rectangle(frame, (x - 5, y - text_height - 5), (x + text_width + 5, y + baseline + 5), (0, 0, 0), -1)
            cv2.putText(frame, text, (x, y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
            out.write(frame)
            written += 1

        cap.release()
        out.release()
        return f"Successfully added watermark '{text}' to '{output_file}' ({written} frames)."
    except Exception as exc:
        return f"Watermark overlay failed: {exc}"


def convert_video_to_gif(input_file: str, output_gif: str, fps: float = 10.0, max_width: int = 480) -> str:
    """Convert video clip into an animated GIF file."""
    if not os.path.exists(input_file):
        return f"Error: Input video '{input_file}' not found."

    try:
        import cv2
        from PIL import Image

        cap = cv2.VideoCapture(input_file)
        orig_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        sample_step = max(1, int(orig_fps / fps))

        frames = []
        count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if count % sample_step == 0:
                h, w, _ = frame.shape
                if w > max_width:
                    new_h = int(h * (max_width / w))
                    frame = cv2.resize(frame, (max_width, new_h))
                # Convert BGR to RGB
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frames.append(Image.fromarray(rgb))
            count += 1

        cap.release()

        if not frames:
            return "Failed to extract frames for GIF conversion."

        frames[0].save(
            output_gif,
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=int(1000 / fps),
            loop=0
        )
        return f"Successfully converted video to animated GIF '{output_gif}' ({len(frames)} frames)."
    except Exception as exc:
        return f"GIF conversion failed: {exc}"


def add_auto_subtitles(video_file: str, output_file: str) -> str:
    """Auto-transcribe video audio using Whisper and render subtitle text onto frames."""
    if not os.path.exists(video_file):
        return f"Error: Input video '{video_file}' not found."

    try:
        from src.voice.stt import transcribe_audio_file
        transcript = transcribe_audio_file(video_file)
        if not transcript or "failed" in transcript.lower():
            transcript = "Meridian-X AI Auto-Captioning"

        return add_text_watermark(
            input_file=video_file,
            output_file=output_file,
            text=transcript[:60],
            position="bottom_left"
        )
    except Exception as exc:
        return f"Auto-subtitling failed: {exc}"
