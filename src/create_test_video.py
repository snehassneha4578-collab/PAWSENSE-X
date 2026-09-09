import cv2
import numpy as np

width, height = 640, 480
fps = 20
frames = 100

writer = cv2.VideoWriter(
    r".\data\test_motion.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (width, height)
)

for i in range(frames):
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    x = 50 + i * 4
    y = 220

    cv2.rectangle(
        frame,
        (x, y),
        (x + 100, y + 80),
        (255, 255, 255),
        -1
    )

    cv2.putText(
        frame,
        "TEST ANIMAL",
        (x, y - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    writer.write(frame)

writer.release()

print("Created: data/test_motion.avi")
print("Frames:", frames)
print("FPS:", fps)


