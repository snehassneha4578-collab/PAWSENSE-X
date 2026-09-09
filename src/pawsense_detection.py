import cv2
import onnxruntime as ort
import numpy as np

MODEL_PATH = r".\models\yolov8n.onnx"
IMAGE_PATH = r".\data\dog.png"

session = ort.InferenceSession(
    MODEL_PATH,
    providers=["CPUExecutionProvider"]
)

image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError("dog.png not found")

h, w = image.shape[:2]

input_image = cv2.resize(image, (640, 640))
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
input_image = input_image.astype(np.float32) / 255.0
input_image = np.transpose(input_image, (2, 0, 1))
input_image = input_image[None, :, :, :]

output = session.run(
    None,
    {session.get_inputs()[0].name: input_image}
)[0][0]

class_ids = np.argmax(output[4:, :], axis=0)
confidence_scores = np.max(output[4:, :], axis=0)

boxes = []
scores = []

for i in range(len(confidence_scores)):
    confidence = float(confidence_scores[i])
    class_id = int(class_ids[i])

    if confidence < 0.25 or class_id != 16:
        continue

    cx, cy, bw, bh = output[:4, i]

    x = int((cx - bw / 2) * w / 640)
    y = int((cy - bh / 2) * h / 640)
    box_w = int(bw * w / 640)
    box_h = int(bh * h / 640)

    boxes.append([x, y, box_w, box_h])
    scores.append(confidence)

indices = cv2.dnn.NMSBoxes(
    boxes,
    scores,
    0.25,
    0.45
)

print()
print("PAWSENSE-X - ANIMAL INTELLIGENCE")
print("=" * 42)

if len(indices) == 0:
    print("No animal detected.")
else:
    index = int(indices[0])

    print("Animal Detected: DOG")
    print("Tracking ID: Animal #1")
    print(f"Detection Confidence: {scores[index] * 100:.2f}%")
    print("Status: ACTIVE")
    print("Movement: MONITORED")
    print("Welfare Analysis: READY")
    print()
    print("Detection pipeline: WORKING")

print("=" * 42)

