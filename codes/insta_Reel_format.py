from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.video.fx.all import resize

# === Input video ===
input_path = "input.mp4"
output_path = "reel_output.mp4"

# === Load video ===
clip = VideoFileClip(input_path)

# === Resize or pad to 1080x1920 (9:16) ===
target_width, target_height = 1080, 1920
clip_resized = resize(clip, height=target_height)

# If width is still less than 1080, center it with padding
if clip_resized.w < target_width:
    x_pad = (target_width - clip_resized.w) // 2
    final_clip = CompositeVideoClip([clip_resized.set_position(("center", "center"))],
                                    size=(target_width, target_height))
else:
    # Crop horizontally if needed
    x_center = clip_resized.w // 2
    final_clip = clip_resized.crop(x_center - target_width//2,
                                   x_center + target_width//2,
                                   0, target_height)

# === Export ===
final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=30)
