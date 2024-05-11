from numba import jit
import numpy as np
import cv2
import os
import time

#ascii_density = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
ascii_density = " .:-=+*#%@"
ascii_image = ''

cap = cv2.VideoCapture("/home/malum/Desktop/coding_tests/vid2ascii/videos/badapple_really_compressed_cut.mp4")

@jit(nopython=True)
def respective_ascii(current_brightness):
    n = round(255 / (len(ascii_density) - 1))
    return ascii_density[int(current_brightness / n)]

@jit(nopython=True)
def ascii_image_generator(frame):
    ascii_image = ''
    for i in range(new_height):
        for j in range(new_width):
            brightness = frame[i][j]
            ascii_image += respective_ascii(brightness)
        ascii_image += '\n'
    return ascii_image


new_height = 75
new_width = 250

fps = cap.get(cv2.CAP_PROP_FPS)

while True:
    ret, frame = cap.read()

    if not ret: break

    frame = cv2.resize(frame, (new_width, new_height))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ascii_image = ascii_image_generator(frame)

    os.system('cls' if os.name == 'nt' else 'clear')

    print(ascii_image)

#1 / fps é a taxa de amostragem de frames, o periodo
    time.sleep(1 / fps)

    if cv2.waitKey(25) & 0xFF == ord('q'): break
print(count)
cap.release()
cv2.destroyAllWindows()

