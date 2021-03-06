---
Project: "Image Conversion to .jpg"
author: ["Jake Williams", "Contact  : info@jakeawilliams.com"]
date: "2022-07-03"
subject: "Image Conversion to .jpg in Python"
keywords: [Image, Python]
lang: "en-US"
---
# Image Conversion to .jpg

## Introduction & Objective

This is a simple Python script that converts images in a directory to .jpg format.

![https://media.giphy.com/media/HaW2iLDzbXePTUzUuP/giphy.gif](https://media.giphy.com/media/HaW2iLDzbXePTUzUuP/giphy-downsized.gif)
## Requirements

This script requires the following Python modules:

-PIL (Python Imaging Library) <br>
-Image (Python Imaging Library) <br>
-os (Operating System)

```python
# Start by importing the image
from PIL import Image   # module for image processing
import os              # module for file system
                    #image-input-path
im = Image.open('images/in/image1.png')
print("The size of the image before conversion is: ", end = "")
print(os.path.getsize('images/in/image1.png'))
# ------------------------------------------------------------



# Display the image before editing ---
Image.open('images/in/image1.png') 
# ------------------------------------


# Convert Image to .jpg -------------
rgb_im = im.convert('RGB')
# ------------------------------------


# Save the image --------------------
rgb_im.save('images/out/image1.jpg')
print("The size of the image after conversion is: ", end = "")
print(os.path.getsize('images/out/image1.jpg'))
# ------------------------------------


# Open the converted image ---------
Image.open('images/out/image1.jpg') 
# ------------------------------------
