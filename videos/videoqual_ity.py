import os
import subprocess

def get_video_info(file_path):
    """Returns resolution and bitrate using ffprobe."""
    try:
        cmd = [
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height,bit_rate",
            "-of", "default=noprint_wrappers=1:nokey=1",
            file_path
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        lines = result.stdout.strip().split("\n")
        if len(lines) >= 3:
            width, height, bitrate = lines
            return int(width), int(height), int(bitrate)
        else:
            return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def check_all_mp4s_in_folder(folder_path):
    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith(".mp4"):
            full_path = os.path.join(folder_path, filename)
            info = get_video_info(full_path)
            if info:
                width, height, bitrate = info
                print(f"{filename}: {width}x{height}, {bitrate / 1000:.2f} kbps")
            else:
                print(f"{filename}: Could not retrieve info")

# Example usage
check_all_mp4s_in_folder(r"C:\hpswsetup\sp108789\po_rn")  # Replace with your actual path


# # Paste your input URLs as a multi-line string here
# input_text = """
# https://i.ibb.co/mVqvJcTH/output-0003.png
# https://i.ibb.co/YFbMVMcc/output-0004.png
# https://i.ibb.co/Z1tyR756/output-0005.png
# https://i.ibb.co/rGhFMmNk/output-0006.png
# https://i.ibb.co/4Ry0hSZw/output-0007.png
# https://i.ibb.co/8DN36FcK/output-0008.png
# https://i.ibb.co/N2XQkZ1p/output-0009.png
# https://i.ibb.co/5gKjgctr/output-0010.png
# https://i.ibb.co/kVYbh3JB/output-0011.png
# https://i.ibb.co/4wTHzTL6/output-0012.png
# https://i.ibb.co/f5jrTjH/output-0013.png
# https://i.ibb.co/ks69RLfC/output-0014.png
# https://i.ibb.co/V0PWRXFd/output-0015.png
# https://i.ibb.co/4RngCw2h/output-0016.png
# https://i.ibb.co/TDbQ99GX/output-0017.png
# https://i.ibb.co/gLCDkC9H/output-0018.png
# https://i.ibb.co/chg506cf/output-0019.png
# https://i.ibb.co/ksgbVdyw/output-0020.png
# https://i.ibb.co/zWCsjYPN/output-0021.png
# https://i.ibb.co/NgK6dGc2/output-0022.png
# https://i.ibb.co/Pv10dkwv/output-0023.png
# https://i.ibb.co/kss85Xs7/output-0024.png
# https://i.ibb.co/8vmXqqd/output-0025.png
# https://i.ibb.co/G4tmXxJH/output-0026.png
# https://i.ibb.co/nNxfBz9Q/output-0027.png
# https://i.ibb.co/TMTyQKZp/output-0028.png
# https://i.ibb.co/pBGCmRWv/output-0029.png
# https://i.ibb.co/xqwQNnqP/output-0030.png
# https://i.ibb.co/wFn28YRN/output-0031.png
# https://i.ibb.co/R4V2LjYL/output-0032.png
# https://i.ibb.co/r2XSYSdL/output-0033.png
# https://i.ibb.co/ZpGPw59X/output-0034.png
# https://i.ibb.co/FL3tNT9W/output-0035.png
# https://i.ibb.co/6JJt7tR7/output-0036.png
# https://i.ibb.co/gMTqJsVS/output-0037.png
# https://i.ibb.co/h1Lh9Xky/output-0038.png
# https://i.ibb.co/Kcg2cHfc/output-0039.png
# https://i.ibb.co/xtWrWHvz/output-0040.png
# https://i.ibb.co/tpw5GT5x/output-0041.png
# https://i.ibb.co/60LgcJJQ/output-0042.png
# https://i.ibb.co/MyJ3CGwg/output-0043.png
# https://i.ibb.co/27GBvNZy/output-0044.png
# https://i.ibb.co/dsYsTf9R/output-0045.png
# https://i.ibb.co/GQxDnvf2/output-0046.png
# https://i.ibb.co/XHx95ZT/output-0047.png
# https://i.ibb.co/60XpmLzW/output-0048.png
# https://i.ibb.co/39BNvfnp/output-0049.png
# https://i.ibb.co/NdmBK2Kq/output-0050.png
# https://i.ibb.co/CpL2Bvcc/output-0051.png
# https://i.ibb.co/gMGfgQFs/output-0052.png
# https://i.ibb.co/0p5TLF4D/output-0053.png
# https://i.ibb.co/7xFv8N0M/output-0054.png
# https://i.ibb.co/zTKZNb3s/output-0055.png
# https://i.ibb.co/nN6KFKts/output-0056.png
# https://i.ibb.co/BV9gNhxr/output-0057.png
# https://i.ibb.co/93NKKGXR/output-0058.png
# https://i.ibb.co/SXMK9GfN/output-0059.png
# https://i.ibb.co/mrkpTdP8/output-0060.png
# https://i.ibb.co/YFXcdzfC/output-0061.png
# https://i.ibb.co/TDtdNdyz/output-0062.png
# https://i.ibb.co/gMtk5fY8/output-0063.png
# https://i.ibb.co/23tZwW8Y/output-0001.png
# https://i.ibb.co/G4f0TwY5/output-0002.png
# """

# # Split the input by lines, strip whitespace, and ignore empty lines
# lines = [line.strip() for line in input_text.strip().split('\n') if line.strip()]

# # Convert each line to a double-quoted string and join with commas
# output = ",\n".join(f'"{line}"' for line in lines)

# print(output)
