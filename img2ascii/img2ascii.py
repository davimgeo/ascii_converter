import cv2
import numpy as np

# ASCII density string
#ascii_density = " .:-=+*#%@"
ascii_density = " .:coPO?@■"
ascii_image = ''

try:
    # Read the image
    image = cv2.imread('/home/davi/Desktop/coding_tests/img2ascii/images/lain.jpg')
    # Convert the image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
except:
    print("Could not find the file. Please verify file path")
    exit()

# Get the dimentions of the image
height, width = image.shape

# Factor to scale down the image
n = 2

# Calculate the new dimensions
new_height = int(height / n)
new_width = int(width / n)

# Rezise image while maintaining the aspect ratio
image = cv2.resize(image, (new_width, new_height))

# Get the corresponding ASCII character for a given brightness value
def respective_ascii(current_brightness):
    n = 255 / (len(ascii_density) - 1)
    return ascii_density[int(np.ceil(current_brightness / n))] 

# Create the ASCII image
for i in range(new_height):
    for j in range(new_width):
        brightness = image[i][j]
        ascii_image += respective_ascii(brightness)
    ascii_image += '\n'

# Write the ASCII art to a text file
with open("ascii_image.txt", 'w', encoding='utf-8') as f:
    f.write(ascii_image)
    
print(ascii_image)
