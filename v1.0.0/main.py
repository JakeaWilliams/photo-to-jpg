# %% [markdown]
# #   Image Conversion to Standardized Format <br>
# Jake Williams -- Linkedin.com/in/Jakeintech <br>
# <h> Step 1 - 
# Start by importing the image

# %%
from PIL import Image   # module for image processing
import os              # module for file system
                    #image-input-path
im = Image.open('images/in/image1.png')
print("The size of the image before conversion is: ", end = "")
print(os.path.getsize('images/in/image1.png'))



# %%
Image.open('images/in/image1.png') #Display the image before editing

# %% [markdown]
# <h> Step 2) <h1>Convert Image to .jpg

# %%
rgb_im = im.convert('RGB') #convert to jpg

# %% [markdown]
# <h> Step 3)        <h1>Save the image

# %%
rgb_im.save('images/out/image1.jpg')
print("The size of the image after conversion is: ", end = "")
print(os.path.getsize('images/out/image1.jpg'))

# %% [markdown]
# Open the converted image

# %%
Image.open('images/out/image1.jpg') #display the image after editing


