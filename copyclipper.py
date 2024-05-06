import time
from pyperclip import copy as pypercopy
from winsound import Beep

import cv2
import keyboard
import numpy as np
import pyautogui
from easyocr import Reader
from PIL import ImageGrab
from screeninfo import get_monitors

def read_text(img):
    # Initialize the OCR reader with English language support
    reader = Reader(['en'])
    # Convert PIL image to a numpy array for processing
    img_array = np.array(img)
    # Perform OCR on the image
    results = reader.readtext(img_array)
    # Extract text from the OCR results and concatenate into a single string
    text = ' '.join([text for (_, text, _) in results])
    return text

def get_screen_of_mouse():
    # Retrieve the current mouse position
    x, y = pyautogui.position()
    # Loop through all monitors to find which one contains the mouse
    for monitor in get_monitors():
        if monitor.x <= x <= monitor.x + monitor.width and monitor.y <= y <= monitor.y + monitor.height:
            return monitor
    return None

def draw_lasso_or_rectangle(event, x, y, flags, param):
    # Handler for mouse events to draw lasso or rectangle selections on the image
    global pts, drawing, img_overlay, rect_start_point

    if event == cv2.EVENT_LBUTTONDOWN:
        # Start drawing on left mouse button down
        drawing = True
        pts = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE and drawing and not flags & cv2.EVENT_FLAG_RBUTTON:
        # Draw line segments between points for lasso tool
        cv2.line(img_overlay, pts[-1], (x, y), (0, 255, 0), 2)
        pts.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP and not flags & cv2.EVENT_FLAG_RBUTTON:
        # Finish drawing and close the loop on left button up
        drawing = False
        pts.append((x, y))
        cv2.line(img_overlay, pts[-1], pts[0], (0, 255, 0), 2)  # Close the loop
        # Create a mask and apply to image to select region
        mask = np.zeros_like(img_gray, dtype=np.uint8)
        cv2.fillPoly(mask, np.array([pts]), 255)
        selected_img = cv2.bitwise_and(img, img, mask=mask)
        crop_and_copy(selected_img)

    if event == cv2.EVENT_RBUTTONDOWN:
        # Start rectangle drawing on right mouse button down
        rect_start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_RBUTTON:
        # Draw a rectangle overlay as the mouse moves
        img_overlay = img.copy()
        cv2.rectangle(img_overlay, rect_start_point, (x, y), (0, 0, 255), 2)

    elif event == cv2.EVENT_RBUTTONUP:
        # Finalize the rectangle on right button up
        img_overlay = img.copy()
        cv2.rectangle(img_overlay, rect_start_point, (x, y), (0, 0, 255), 2)
        rect_end_point = (x, y)
        mask = np.zeros_like(img_gray, dtype=np.uint8)
        cv2.rectangle(mask, rect_start_point, rect_end_point, 255, -1)
        selected_img = cv2.bitwise_and(img, img, mask=mask)
        crop_and_copy(selected_img)

def crop_and_copy(selected_img):
    # Crop the selected image region and copy the resulting text to the clipboard
    gray = cv2.cvtColor(selected_img, cv2.COLOR_BGR2GRAY)
    x, y, w, h = cv2.boundingRect(cv2.findNonZero(gray))
    crop = selected_img[y:y+h, x:x+w]
    h, w = crop.shape[:2]
    text = read_text(crop)
    pypercopy(text)

def add_color_with_opacity(img, color_bgr=(255,200,200), opacity=0.15):
    # Apply a translucent overlay to the entire image
    overlay = img.copy()
    cv2.rectangle(overlay, (0, 0), (img.shape[1], img.shape[0]), color_bgr, -1)
    return cv2.addWeighted(overlay, opacity, img, 1 - opacity, 0)

def main():
    print("Copy Clipper is running!")
    global img, img_overlay, img_gray, drawing, pts, rect_start_point
    drawing = False
    pts = []
    rect_start_point = None

    while True:
        # Main loop to check for user input and handle screen capture
        time.sleep(1)
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('space') and keyboard.is_pressed('shift'):
            monitor = get_screen_of_mouse()
            if monitor:
                # Grab a screenshot of the selected monitor
                screenshot = ImageGrab.grab(bbox=(monitor.x, monitor.y, monitor.x + monitor.width, monitor.y + monitor.height), all_screens=True)
                img = np.array(screenshot)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img_overlay = img.copy()

                # Setup and display the snipping tool window
                cv2.namedWindow("Snipping Tool", cv2.WINDOW_NORMAL)
                cv2.moveWindow("Snipping Tool", monitor.x, monitor.y)
                cv2.setWindowProperty("Snipping Tool", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.setWindowProperty("Snipping Tool", cv2.WND_PROP_TOPMOST, 1)
                cv2.setMouseCallback("Snipping Tool", draw_lasso_or_rectangle)

                while keyboard.is_pressed('ctrl') and keyboard.is_pressed('space') and keyboard.is_pressed('shift'):
                    # Display the snipping tool while the key combination is held
                    time.sleep(0.01)
                    cv2.imshow("Snipping Tool", add_color_with_opacity(img_overlay))
                    key = cv2.waitKey(1) & 0xFF
                    if key == 27:  # ESC key to exit
                        break

                cv2.destroyAllWindows()
        
        # Check for ESC key outside the screen capturing loop
        if keyboard.is_pressed('shift') and keyboard.is_pressed('space') and keyboard.is_pressed('esc'):
            Beep(350,600)  # Beep to signal exit
            print("Exiting Copyclipper")
            break

if __name__ == "__main__":
    main()
