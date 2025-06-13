import re

# Path to your input file
INPUT_FILE = "video_list.txt"

# Thresholds (in kbps)
LOW_MAX    = 1500
MEDIUM_MAX = 6000

low, medium, high = [], [], []

with open(INPUT_FILE, 'r') as f:
    for line in f:
        m = re.match(r'(\S+\.mp4):.*,\s*([\d\.]+)\s*kbps', line)
        if not m:
            continue
        filename = m.group(1)
        bitrate  = float(m.group(2))

        if bitrate < LOW_MAX:
            low.append(filename)
        elif bitrate <= MEDIUM_MAX:
            medium.append(filename)
        else:
            high.append(filename)

# Helper to write a list to a file in ffmpeg concat format
def write_list(lst, fname):
    with open(fname, 'w') as out:
        for fn in lst:
            out.write(f"file '{fn}'\n")
    print(f"Wrote {len(lst)} entries to {fname}")

# Write out each category
write_list(low,    "low_quality.txt")
write_list(medium, "medium_quality.txt")
write_list(high,   "high_quality.txt")
