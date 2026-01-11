from flask import Flask, Response
import cv2
import numpy as np

app = Flask(__name__)

cap = cv2.VideoCapture(0)

# Background subtractor for motion detection
mog = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=25, detectShadows=False)

def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.resize(frame, (640, 480))

        # --- 1. Convert to grayscale ---
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # --- 2. Create silhouette (black person on white background) ---
        _, silhouette = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

        # Convert silhouette to BGR
        silhouette_bgr = cv2.cvtColor(silhouette, cv2.COLOR_GRAY2BGR)

        # Make background white, person black
        silhouette_bgr[silhouette == 255] = [0, 0, 0]    # Person = black
        silhouette_bgr[silhouette == 0] = [255, 255, 255]  # Background = white

        # --- 3. Edge detection on silhouette ---
        edges = cv2.Canny(silhouette, 50, 150)

        # --- 4. Motion detection ---
        fgmask = mog.apply(gray)
        _, motion_mask = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)

        # --- 5. Red outline on moving edges only ---
        moving_edges = cv2.bitwise_and(edges, motion_mask)

        # Draw red edges on silhouette
        silhouette_bgr[moving_edges > 0] = [0, 0, 255]

        # --- Streaming ---
        _, buffer = cv2.imencode('.jpg', silhouette_bgr)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
