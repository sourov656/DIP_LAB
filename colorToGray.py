import cv2
import os
import matplotlib.pyplot as plt

# Load a color image
color_path = 'glavo-field-5932123_1920.jpg'
img_bgr = cv2.imread(color_path, cv2.IMREAD_COLOR)

if img_bgr is None:
    print(f"Error: {color_path} not found.")
else:
    # Convert BGR to RGB for plotting and GRAY for grayscale conversion
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Save gray version temporarily to calculate byte size
    temp_gray_path = 'temp_grayscale.jpg'
    cv2.imwrite(temp_gray_path, img_gray)

    # Calculate memory and file sizes
    color_channels = img_bgr.shape[2]
    gray_channels = 1 if len(img_gray.shape) == 2 else img_gray.shape[2]

    color_bytes = os.path.getsize(color_path)
    gray_bytes = os.path.getsize(temp_gray_path)

    print("--- Channel & Size Report ---")
    print(f"Original Channels: {color_channels} | Grayscale Channels: {gray_channels}")
    print(f"Color File Size: {color_bytes} bytes | Grayscale File Size: {gray_bytes} bytes")

    # Clean up temporary file
    if os.path.exists(temp_gray_path):
        os.remove(temp_gray_path)

    # Display side by side
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original RGB Image")
    axes[0].axis('off')

    axes[1].imshow(img_gray, cmap='gray')
    axes[1].set_title("Converted Grayscale Image")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()