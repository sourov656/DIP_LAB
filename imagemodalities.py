import cv2
import matplotlib.pyplot as plt

modalities = {
    "X-Ray": ("images.jpg", "Detecting structural bone fractures and thoracic diseases."),
    "Satellite": ("glavo-field-5932123_1920.jpg", "Monitoring agricultural crop growth and deforestation."),
    "Microscopy": ("images.jpg", "Examining cell structures and pathological tissue samples."),
    "Ultrasound": ("images.jpg", "Safe real-time monitoring of fetal growth in obstetric care."),
    "Infrared": ("glavo-field-5932123_1920.jpg", "Identifying building heat loss and night-time security surveillance.")
}

fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for idx, (modality, (path, app)) in enumerate(modalities.items()):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        axes[idx].imshow(img, cmap='gray')
    axes[idx].set_title(modality)
    axes[idx].axis('off')
    print(f"[{modality}] Application: {app}")

plt.tight_layout()
plt.show()