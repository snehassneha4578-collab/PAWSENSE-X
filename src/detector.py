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
    raise FileNotFoundError(f"Could not read: {IMAGE_PATH}")

original_h, original_w = image.shape[:2]

input_image = cv2.resize(image, (640, 640))
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
input_image = input_image.astype(np.float32) / 255.0
input_image = np.transpose(input_image, (2, 0, 1))
input_image = input_image[None, :, :, :]

output = session.run(
    None,
    {session.get_inputs()[0].name: input_image}
)[0][0]

boxes = []
scores = []

class_ids = np.argmax(output[4:, :], axis=0)
confidence_scores = np.max(output[4:, :], axis=0)

scale_x = original_w / 640
scale_y = original_h / 640

for i in range(len(confidence_scores)):
    confidence = float(confidence_scores[i])
    class_id = int(class_ids[i])

    if confidence < 0.25 or class_id != 16:
        continue

    cx, cy, bw, bh = output[:4, i]

    x = int((cx - bw / 2) * scale_x)
    y = int((cy - bh / 2) * scale_y)
    width = int(bw * scale_x)
    height = int(bh * scale_y)

    boxes.append([x, y, width, height])
    scores.append(confidence)

indices = cv2.dnn.NMSBoxes(
    boxes,
    scores,
    score_threshold=0.25,
    nms_threshold=0.45
)

print("PAWSENSE-X Animal Detection")
print("=" * 35)

if len(indices) == 0:
    print("No dog detected.")
else:
    for animal_number, index in enumerate(indices, start=1):
        index = int(index)
        print(f"Animal #{animal_number}")
        print("Type: Dog")
        print(f"Confidence: {scores[index] * 100:.2f}%")
        print(f"Bounding Box: {boxes[index]}")
        print()

cv2.imwrite(r".\outputs\dog_detection.jpg", image)
print("Saved: outputs/dog_detection.jpg")


