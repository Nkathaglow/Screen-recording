# Install and import the necessary libraries
import numpy as np
import cv2
import pyautogui

# Set the screen size, output name and the frame
SCREEN_SIZE = (1920, 1080)
output_filename = "record.avi"
fps = 20.0

# Choose the video codec for record saving
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Fix the VideoWriter_fourcc argument
out = cv2.VideoWriter(output_filename, fourcc, fps, SCREEN_SIZE)

try:
    # Start an infinite loop for recording the screen
    while True:
        # Capture the screen as an image using the pyautogui library
        img = pyautogui.screenshot()
        # The image is converted to a numPy array for processing
        frame = np.array(img)
        # Convert the color format from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

        # Displays the captured frame on the screen
        cv2.imshow("Screen Recording", frame)  # Fix the imshow function

        # Pressing 'q' exits and saves the recording
        if cv2.waitKey(1) == ord("q"):
            break

except KeyboardInterrupt:
    pass

# Releases the video writer and closes the OpenCV window
out.release()
cv2.destroyAllWindows()
