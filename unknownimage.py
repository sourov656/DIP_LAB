import cv2
import numpy as np

def classify_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        return f"Error: Cannot load {image_path}"

    # Check channels
    if len(img.shape) == 2 or img.shape[2] == 1:
        unique_pixels = np.unique(img)
        if len(unique_pixels) == 2:
            return f"Binary Image: Detected {len(unique_pixels)} unique pixel values ({unique_pixels})."
        else:
            return f"Grayscale Image: Single-channel intensity values with {len(unique_pixels)} unique values."
    else:
        b, g, r = cv2.split(img[:, :, :3])
        if np.array_equal(b, g) and np.array_equal(g, r):
            unique_pixels = np.unique(b)
            if len(unique_pixels) == 2:
                return f"Binary Image: 3-channel layout containing 2 unique values ({unique_pixels})."
            return f"Grayscale Image: Single intensity replicated across 3 channels."
        return f"Full-Color Image: Multiple color channels detected."

# Test with images
print(classify_image('glavo-field-5932123_1920.jpg'))
print(classify_image('images.jpg'))