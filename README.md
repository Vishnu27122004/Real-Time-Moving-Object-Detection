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


## System Architecture

The application follows a client-server architecture with real-time video streaming:

```
Webcam Input
    |
    v
OpenCV VideoCapture (cv2.VideoCapture(0))
    |
    v
Grayscale Conversion
    |
    v
Background Subtraction (MOG2)
    |
    v
Morphological Operations (Erosion/Dilation)
    |
    v
Contour Detection & Filtering
    |
    v
Draw Contours on Frame
    |
    v
JPEG Encoding
    |
    v
Flask MJPEG Stream (/video_feed)
    |
    v
Web Browser (HTML5 Display)
```

## Component Details

### 1. Video Capture Module
- **Purpose**: Acquire frames from webcam in real-time
- **Technology**: OpenCV (cv2.VideoCapture)
- **Functions**:
  - Initialize camera device (index 0)
  - Read frames continuously at 30 FPS
  - Handle frame buffering
- **Frame Format**: BGR color space (OpenCV default)

### 2. Motion Detection Engine
- **Algorithm**: MOG2 (Mixture of Gaussians)
- **Process**:
  1. Capture frame from camera
  2. Apply background subtraction to isolate moving regions
  3. Apply morphological operations (erode/dilate)
  4. Detect contours in processed frame
  5. Filter contours by area threshold (~500 px)
- **Tunable Parameters**:
  - Contour area threshold
  - Morphological kernel size (5x5)
  - Sensitivity level

### 3. Frame Processing Pipeline
- Convert BGR frame to grayscale
- Apply Gaussian blur for noise reduction
- Background subtraction
- Morphological operations
- Contour detection
- Draw green contours on original frame

### 4. Flask Web Server
- **Routes**:
  - `GET /` - Main HTML page
  - `GET /video_feed` - MJPEG stream endpoint
- **Streaming Protocol**: Motion JPEG (MJPEG)
  - Each frame as JPEG
  - Boundary markers between frames
  - Continuous HTTP streaming
- **Performance**: Non-blocking, multi-client support

### 5. Frontend Interface
- HTML5 with embedded image tag
- Displays `/video_feed` stream
- Real-time video display
- Lightweight and responsive

## Processing Flow Diagram

```
START
  |
  v
Initialize Flask App
  |
  v
Initialize OpenCV VideoCapture
  |
  +-----> Server Listening on localhost:5000
  |        |
  |        v
  |      Client Request (GET /)
  |        |
  |        v
  |      Serve HTML Page
  |        |
  |        v
  |      Browser displays <img src='/video_feed'>
  |
  +-----> Continuous Loop
           |
           v
         Read Frame from Camera
           |
           v
         Grayscale Conversion
           |
           v
         Background Subtraction
           |
           v
         Morphological Operations
           |
           v
         Contour Detection
           |
           v
         Filter by Area Threshold
           |
           v
         Draw Detected Contours
           |
           v
         JPEG Encode Frame
           |
           v
         Send as MJPEG Frame
           |
           v
         Browser Display Updates
           |
           +---> Repeat
END
```

## Data Flow - Motion Detection Algorithm

```
Raw Camera Frame (BGR)
        |
        v
  [Grayscale]
   Gray Frame
        |
        v
[Background Subtraction - MOG2]
   Foreground Mask
   (White=Motion, Black=Static)
        |
        v
 [Gaussian Blur]
   Smoothed Mask
        |
        v
[Morphological Operations]
   Erosion -> Remove small noise
   Dilation -> Fill holes
        |
        v
 [Contour Detection]
   List of Contours
        |
        v
[Area Filtering]
   Contours > 500 px area
        |
        v
 [Drawing]
   Green contours on RGB frame
        |
        v
Annotated Output Frame
```

## Configuration Parameters

| Parameter | Value | Purpose |
|-----------|-------|----------|
| Camera Index | 0 | Default webcam |
| Frame Rate | 30 FPS | Video smoothness |
| Contour Threshold | 500 px | Motion sensitivity |
| Morphological Kernel | 5x5 | Contour smoothing |
| JPEG Quality | 80% | Stream quality |
| Server Port | 5000 | Web access |
| Color Space | BGR/Gray | Processing efficiency |

## Key Algorithms

### Background Subtraction (MOG2)
- Mixture of Gaussian model per pixel
- Adaptive background learning
- Identifies pixels significantly different from background
- Output: Binary foreground mask

### Morphological Operations
- **Erosion**: Remove small objects (noise)
- **Dilation**: Fill holes in objects
- Applied in sequence: Erosion -> Dilation (Closing operation)

### Contour Detection
- Uses OpenCV's findContours function
- Detects boundaries of objects
- Calculates area of each contour
- Filters out small noise contours

## Performance Optimization Tips

1. **Reduce Frame Resolution**: Lower resolution = faster processing
2. **Adjust Morphological Kernel**: Larger kernel = more smoothing
3. **Tune Contour Threshold**: Higher threshold = less sensitivity
4. **JPEG Quality**: Lower quality = smaller file size, faster streaming
5. **Frame Rate**: 15-30 FPS provides good balance

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Camera not found | Device index wrong | Try index 1 or 2 |
| High CPU usage | Processing too slow | Reduce resolution |
| Lag in stream | Network/processing slow | Reduce JPEG quality |
| No motion detected | Threshold too high | Lower contour threshold |
| Too much noise | Threshold too low | Increase contour threshold |

## Future Enhancements

- [ ] Multi-threaded frame capture
- [ ] Machine learning-based motion classification
- [ ] Video recording with timestamp
- [ ] Motion-triggered alerts
- [ ] Web dashboard for parameter tuning
- [ ] Mobile app integration
- [ ] Cloud upload capability
- [ ] Multi-camera support
