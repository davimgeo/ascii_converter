from numba import njit, prange
import cv2
import os
import time

#ascii_density = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
#ascii_density = " .:-=+*#%@"
ascii_density = "@%#*+=-:. "
ascii_image = ''

cap = cv2.VideoCapture("videos/bad_apple.mp4")
#cap = cv2.VideoCapture("videos/badapple_really_compressed_cut.mp4")

#Gets the respective ascii char for the current brightness of the frame
@njit
def respective_ascii(current_brightness):
    n = round(255 / (len(ascii_density) - 1))
    return ascii_density[int(current_brightness / n)]

#Generate a string list with all respective ascii char
@njit
def ascii_image_generator(frame, new_height, new_width):
  ascii_image = ''
  for i in prange(new_height):
    for j in range(new_width):
      brightness = frame[i][j]
      ascii_image += respective_ascii(brightness)
    ascii_image += '\n'
  return ascii_image

#new_width, new_height = os.get_terminal_size()
new_height = 100
new_width = 350

#fps = cap.get(cv2.CAP_PROP_FPS)
fps = 60

print("\033[2J")    
print("\033[?25l") 

while True:
  ret, frame = cap.read()
  if not ret:
      break

  frame = cv2.resize(frame, (new_width, new_height))
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  ascii_image = ascii_image_generator(frame, new_height, new_width)

  print("\033[H" + ascii_image, end="")

  time.sleep(1 / fps)

print("\033[?25h")  

cap.release()
cv2.destroyAllWindows()

