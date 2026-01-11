# Real-Time Moving Object Detection

## Overview
A Flask-based web application that performs real-time motion detection using OpenCV. This project captures video from a webcam, processes frames to detect moving objects, and streams the video with motion highlighted in real-time.

## Features
- Real-time motion detection from webcam feed
- Visual highlighting of detected motion areas
- Web-based streaming interface using Flask
- Efficient frame processing with OpenCV
- Optimized for low-latency performance

## Technology Stack
- **Backend**: Flask (Python web framework)
- **Computer Vision**: OpenCV
- **Video Processing**: NumPy

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Real-Time-Moving-Object-Detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:
```bash
python motion_detection.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. The application will display the live video feed with motion detection enabled.

## How It Works

1. **Video Capture**: The application captures frames from the default webcam
2. **Processing**: Each frame is processed to detect motion using background subtraction
3. **Visualization**: Detected motion is highlighted with contours
4. **Streaming**: Frames are encoded and streamed to the web interface

## Requirements
See `requirements.txt` for detailed package versions.

## License
MIT License - See LICENSE file for details

## Notes
- Ensure your system has a functioning webcam
- The application runs on localhost by default
- Motion detection sensitivity can be adjusted in the code
