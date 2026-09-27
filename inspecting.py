import cv2
import matplotlib.pyplot as plt

def inspect_image(image_path, is_color=True):
    # Load image based on flag
    if is_color:
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    else:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was successfully loaded
    if img is None:
        print(f"Error: '{image_path}' Not found file\n")
        return

    # Convert BGR to RGB for correct color display in Matplotlib
    if is_color:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    else:
        img_rgb = img

    # Shape and properties
    shape = img.shape
    height = shape[0]
    width = shape[1]
    channels = shape[2] if len(shape) == 3 else 1
    dtype = img.dtype

    print(f"File: {image_path}")
    print(f"Width: {width}, Height: {height}, Channels: {channels}, Data Type: {dtype}\n")

    plt.imshow(img_rgb, cmap='gray' if channels == 1 else None)
    plt.title(f"{'Color' if is_color else 'Grayscale'} Image")
    plt.axis('off')
    plt.show()

# Run for both images
inspect_image('glavo-field-5932123_1920.jpg', is_color=True)
inspect_image('images.jpg', is_color=False)