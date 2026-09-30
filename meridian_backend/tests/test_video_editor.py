"""
meridian_backend/tests/test_video_editor.py
Unit Test Suite for Video Editor Tools
"""

import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_video_editing_pipeline():
    """Test video creation, trimming, watermarking, speed change, and GIF conversion."""
    import cv2
    import numpy as np
    from src.tools.video_editor import (
        trim_video, concat_videos, change_video_speed,
        add_text_watermark, convert_video_to_gif
    )

    # 1. Create a dummy test video
    temp_dir = tempfile.mkdtemp(prefix="test_video_")
    video1_path = os.path.join(temp_dir, "video1.mp4")
    video2_path = os.path.join(temp_dir, "video2.mp4")

    width, height, fps = 320, 240, 10.0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out1 = cv2.VideoWriter(video1_path, fourcc, fps, (width, height))
    for i in range(20):  # 2 seconds
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        frame[:, :] = (i * 10, 50, 100)
        out1.write(frame)
    out1.release()

    out2 = cv2.VideoWriter(video2_path, fourcc, fps, (width, height))
    for i in range(20):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        frame[:, :] = (100, i * 10, 50)
        out2.write(frame)
    out2.release()

    # 2. Test Trim Video
    trimmed_path = os.path.join(temp_dir, "trimmed.mp4")
    trim_res = trim_video(video1_path, trimmed_path, start_sec=0.5, end_sec=1.5)
    assert "Successfully trimmed" in trim_res
    assert os.path.exists(trimmed_path)

    # 3. Test Concat Videos
    concat_path = os.path.join(temp_dir, "merged.mp4")
    concat_res = concat_videos([video1_path, video2_path], concat_path)
    assert "Successfully concatenated" in concat_res
    assert os.path.exists(concat_path)

    # 4. Test Speed Change
    speed_path = os.path.join(temp_dir, "speed.mp4")
    speed_res = change_video_speed(video1_path, speed_path, speed_factor=2.0)
    assert "Adjusted video speed" in speed_res
    assert os.path.exists(speed_path)

    # 5. Test Watermark
    wm_path = os.path.join(temp_dir, "watermark.mp4")
    wm_res = add_text_watermark(video1_path, wm_path, text="Meridian-X Test")
    assert "Successfully added watermark" in wm_res
    assert os.path.exists(wm_path)

    # 6. Test GIF Conversion
    gif_path = os.path.join(temp_dir, "output.gif")
    gif_res = convert_video_to_gif(video1_path, gif_path, fps=5.0)
    assert "Successfully converted" in gif_res
    assert os.path.exists(gif_path)
