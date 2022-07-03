---
Project: "Image Conversion to .jpg"
author: ["Jake Williams", "Contact  : info@jakeawilliams.com"]
date: "2022-07-03"
subject: "Image Conversion to .jpg in Python"
keywords: [Image, Python]
subtitle: "OSCP Exam Report"
lang: "en-US"
titlepage: true
titlepage-color: "ADC3D1"
titlepage-text-color: "EEECF1"
titlepage-rule-color: "EEECF1"
titlepage-rule-height: 2
book: true
classoption: oneside
code-block-font-size: \scriptsize
---
# Image Conversion to .jpg

![Walkthrough](https://media.giphy.com/media/HaW2iLDzbXePTUzUuP/giphy.gif) <br>

## Introduction & Objective

This is a simple Python script that converts all the images in a directory to .jpg format.


## Requirements

This script requires the following Python modules:

-PIL (Python Imaging Library) <br>
-Image (Python Imaging Library) <br>
-os (Operating System)

# Steps to run the script

TBD - Need to add steps to run the script

**Proof of Concept Code Here:**
Modifications to the existing exploit was needed and is highlighted in red.

```python
# Start by importing the image
from PIL import Image   # module for image processing
import os              # module for file system
                    #image-input-path
im = Image.open('images/in/image1.jpeg')
print("The size of the image before conversion is: ", end = "")
print(os.path.getsize('images/in/image1.jpeg'))
# ------------------------------------------------------------



# Display the image before editing ---
Image.open('images/in/image1.jpeg') 
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
