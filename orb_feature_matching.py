import cv2
import numpy as np

# Load two images in grayscale
img1 = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the images are loaded properly
if img1 is None or img2 is None:
    print("Error: One or both images not found.")
    exit()

# Initialize the ORB detector
orb = cv2.ORB_create(nfeatures=1000)

# Detect keypoints and compute descriptors for both images
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

# Create BFMatcher object (Brute Force with Hamming distance)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(descriptors1, descriptors2)

# Sort matches by distance (best matches first)
matches = sorted(matches, key=lambda x: x.distance)

# Draw the top N matches
N_MATCHES = 50  # number of matches to draw
matched_image = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:N_MATCHES], None, flags=2)

# Resize image for display (optional)
matched_image = cv2.resize(matched_image, (1200, 600))

# Display the matching result
cv2.imshow("ORB Feature Matching", matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
