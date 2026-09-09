import cv2
import onnxruntime as ort
import numpy as np

MODEL_PATH = r".\models\yolov8n.onnx"
VIDEO_SOURCE = r".\data\dog_tracking.avi"

session = ort.InferenceSession(
    MODEL_PATH,
    providers=["CPUExecutionProvider"]
)

cap = cv2.VideoCapture(VIDEO_SOURCE)

if not cap.isOpened():
    raise RuntimeError("Could not open webcam.")

print("PAWSENSE-X Live Animal Tracking")
print("=" * 35)
print("Press Q to quit.")

next_animal_id = 1

while True:
    ret, frame = cap.read()

    if not ret:
        print('Could not read video frame.')
        continue

    h, w = frame.shape[:2]

    input_image = cv2.resize(frame, (640, 640))
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

    scale_x = w / 640
    scale_y = h / 640

    for i in range(len(confidence_scores)):
        confidence = float(confidence_scores[i])
        class_id = int(class_ids[i])

        if confidence < 0.40 or class_id != 16:
            continue

        cx, cy, bw, bh = output[:4, i]

        x = int((cx - bw / 2) * scale_x)
        y = int((cy - bh / 2) * scale_y)
        box_w = int(bw * scale_x)
        box_h = int(bh * scale_y)

        boxes.append([x, y, box_w, box_h])
        scores.append(confidence)

    indices = cv2.dnn.NMSBoxes(
        boxes,
        scores,
        score_threshold=0.40,
        nms_threshold=0.45
    )

    for animal_number, index in enumerate(indices, start=1):
        index = int(index)

        x, y, box_w, box_h = boxes[index]

        cv2.rectangle(
            frame,
            (x, y),
            (x + box_w, y + box_h),
            (0, 255, 0),
            3
        )

        cv2.putText(
            frame,
            f"Animal #{animal_number} | Dog | {scores[index] * 100:.1f}%",
            (x, max(30, y - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Animals detected: {len(indices)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow("PAWSENSE-X Animal Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Tracking stopped.")





