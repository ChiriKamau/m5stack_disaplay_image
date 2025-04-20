from PIL import Image
import numpy as np
import base64

# Open and resize image
img = Image.open("stacy.jpg").convert("RGB").resize((320, 240))
pixels = np.array(img)

# Convert to RGB565
rgb565 = ((pixels[:,:,0] >> 3) << 11) | ((pixels[:,:,1] >> 2) << 5) | (pixels[:,:,2] >> 3)

# Convert to bytes and compress with Base64
img_bytes = rgb565.astype('>u2').tobytes()  # Big-endian uint16
encoded = base64.b64encode(img_bytes).decode('ascii')

# Generate C array
with open("stacy1.h", "w") as f:
    f.write(f'const char stacy_img_compressed[] PROGMEM = "{encoded}";\n')