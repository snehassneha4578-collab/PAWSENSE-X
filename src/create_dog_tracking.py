import cv2
import numpy as np

image = cv2.imread(r".\data\dog.png")

if image is None:
    raise FileNotFoundError("dog.png not found")

image = cv2.resize(image, (640, 480))

writer = cv2.VideoWriter(
    r".\data\dog_tracking.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    10,
    (640, 480)
)

for i in range(60):
    frame = image.copy()

    shift = i * 2
    matrix = np.float32([[1, 0, shift], [0, 1, 0]])
    frame = cv2.warpAffine(frame, matrix, (640, 480))

    writer.write(frame)

writer.release()

print("Created: data/dog_tracking.avi")
print("Frames: 60")
print("FPS: 10")
print("Simulated animal: Dog")
