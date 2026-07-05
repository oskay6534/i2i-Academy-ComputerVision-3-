# Real-Time Finger Counter (Real-Time Hand Tracking)

This project is a real-time computer vision application that detects a human hand via webcam and counts the number of open fingers using Google's MediaPipe framework and OpenCV.

## 🚀 Features
- Real-time hand landmark detection (21 points tracking).
- Dynamic finger counting logic based on coordinate analysis.
- Visual feedback with live text on the screen.

## 🛠️ Tech Stack & Dependencies
This project is built using **Python 3.12 (Anaconda Environment)** with the following exact, stable package versions to prevent environment conflicts:
- **NumPy** `== 1.26.4`
- **OpenCV-Python** `== 4.9.0.80`
- **MediaPipe** `== 0.10.14`

## 📦 Installation & Setup
Since Windows AppLocker/SmartScreen policies may block execution within virtual environments (`venv`), it is highly recommended to run this project in a global or Anaconda environment using the `--no-cache-dir` flag.



Bash
pip install "numpy==1.26.4" "opencv-python==4.9.0.80" "mediapipe==0.10.14" --no-cache-dir
Run the application:

Bash
python finger_counter.py
💡 Algorithmic Logic
For Four Fingers (Index, Middle, Ring, Pinky): The algorithm checks if the Y-coordinate of the finger tip (e.g., landmark 8 for index) is higher (lower numerical value in image space) than its respective joint (landmark 6).

For the Thumb: Since the thumb moves horizontally, the X-coordinate of the tip (landmark 4) is compared against landmark 2
