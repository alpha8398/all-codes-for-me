import subprocess
from PIL import Image

# Convert XCF to PNG using xcftools
subprocess.run(['xcf2png', 'my_first_edit.xcf', '-o', 'my_first_edit.png'])

# Convert PNG to JPG using Pillow
img = Image.open('my_first_edit.png').convert('RGB')
img.save('my_first_edit.jpg', quality=95)

print("XCF converted to JPG successfully!")
