from PIL import Image
import numpy as np

# Open JPG and resize to 320x240
img = Image.open("stacy.jpg").convert("RGB").resize((320, 240))
pixels = np.array(img)

# Convert to RGB565 (16-bit)
rgb565 = ((pixels[:,:,0] >> 3) << 11) | ((pixels[:,:,1] >> 2) << 5) | (pixels[:,:,2] >> 3)

# Generate C array
with open("stacy_img.h", "w") as f:
    f.write("const uint16_t stacy_img[] PROGMEM = {\n")
    for row in rgb565:
        f.write("    " + ", ".join([f"0x{px:04X}" for px in row]) + ",\n")
    f.write("};\n")