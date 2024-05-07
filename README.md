# Copy Clipper

Copy Clipper is a screen capture tool that enables users to select portions of their screen either via a lasso tool or a rectangular selection. The selected area is then processed to extract readable text using OCR (Optical Character Recognition), and the text is automatically copied to the clipboard.

#### Dispclaimer
* Easy OCR is not 100% accurate

## Features

- **Screen Selection**: Choose a specific area of the screen with a lasso (left click) or rectangle tool (right click).
- **OCR Integration**: Automatically recognize and extract text from the selected screen area.
- **Clipboard Management**: Copy the extracted text directly to the clipboard.
- **Multi-monitor Support**: Works across multiple monitors.
![Copyclip](https://github.com/Gabriel-Halaweh/CopyClipper/assets/115294138/3ae5d815-9f2b-4847-bd7f-10b4e721af4d)

## Usage

### Activating Screen Capture Mode
To start capturing a portion of your screen:
1. Hold down **CTRL + SHIFT + SPACE**. This will activate the screen capture mode.
2. Once activated, you will see the screen's overlay indicating that you are in capture mode.

### Making Selections
- **Lasso Tool**: Click and hold the left mouse button, then move the mouse to draw a freeform shape around the area you want to capture. Release the button to complete the selection.
- **Rectangle Tool**: Click and hold the right mouse button, then drag to draw a rectangular shape. Release the button to finalize the rectangle.

### Size Limitations
The OCR functionality is optimized for images up to 1500 pixels in width or height. Ensure that the selected area does not exceed these dimensions to maintain accuracy and performance.

### Copying Text to Clipboard
After releasing the mouse button to finalize your selection, the tool automatically processes the captured area, extracts readable text using OCR, and copies this text directly to your clipboard.

### Exiting Screen Capture Mode
- To exit the screen capture mode at any time, press **SHIFT + SPACE + ESC**. 


## Installation

To use Copy Clipper, you need to have Python installed on your machine along with several dependencies. Here's how you can set it up:

#### Dependencies

Copy Clipper relies on the following Python libraries:
- `opencv-python` (cv2): For image processing tasks.
- `pyautogui`: For screen capture and mouse position tracking.
- `numpy`: For handling image arrays.
- `Pillow`: For additional image handling outside of OpenCV.
- `easyocr`: For performing OCR on images.
- `keyboard`: For listening to keyboard shortcuts.
- `pyperclip`: For clipboard operations.
- `winsound`: For playing sounds (note: `winsound` is only available on Windows).
- `screeninfo`: For getting information about the monitors.

#### PIp command:
pip install opencv-python pyautogui numpy Pillow easyocr keyboard pyperclip screeninfo
