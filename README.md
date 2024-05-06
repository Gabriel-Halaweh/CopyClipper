# Copy Clipper

Copy Clipper is a screen capture tool that enables users to select portions of their screen either via a lasso tool or a rectangular selection. The selected area is then processed to extract readable text using OCR (Optical Character Recognition), and the text is automatically copied to the clipboard.

## Features

- **Screen Selection**: Choose a specific area of the screen with a lasso (left click) or rectangle tool (right click).
- **OCR Integration**: Automatically recognize and extract text from the selected screen area.
- **Clipboard Management**: Copy the extracted text directly to the clipboard.
- **Multi-monitor Support**: Works across multiple monitors.

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
