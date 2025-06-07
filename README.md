# ORB Feature Matching with OpenCV

A simple Python project demonstrating how to detect and match keypoints between two images using the ORB (Oriented FAST and Rotated BRIEF) algorithm. This project is ideal for beginners in computer vision who want hands-on experience with feature detection and matching.

---

## 🔍 Overview

This project performs the following steps:

- Load two input images  
- Detect keypoints using the ORB detector  
- Compute descriptors for each keypoint  
- Match descriptors using Brute-Force Matcher with Hamming distance  
- Visualize the top matches with lines connecting keypoints across the images

---

## ✨ Features

- Fast and efficient keypoint detection with ORB
- Simple and clean code using OpenCV
- Visual output for matched keypoints
- Easily extendable for more advanced feature-matching tasks

---

## ✅ Requirements

- Python 3.6 or later  
- OpenCV (`opencv-python`)

Install dependencies using pip:

```bash
pip install opencv-python
