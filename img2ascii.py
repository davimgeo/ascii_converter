import cv2

#ascii_density = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
ascii_density = " .:-=+*#%@"
ascii_image = ''

image = cv2.imread('/home/malum/Desktop/coding_tests/img2ascii/images/lumahlinda.jpg')

#Turn image into gray scale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = image.shape

new_height = 100
new_width = 200

#Resizing the image for the new height and width
image = cv2.resize(image, (new_width, new_height))

#Gets the correspondent ascii index for a brightness values
def respective_ascii(current_brightness):
    n = round(255 / (len(ascii_density) - 1), 2)
    return ascii_density[int(current_brightness / n)] 

#Iterate for each brightness value and gets correspondent ascii char
for i in range(new_height):
    for j in range(new_width):
        brightness = image[i][j]
        ascii_image += respective_ascii(brightness)
    ascii_image += '\n'

# with open("ascii_image.txt", 'w') as f:
#      f.write(ascii_image)

print(ascii_image)