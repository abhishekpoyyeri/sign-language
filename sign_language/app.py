import cv2
from ultralytics import YOLO
model = YOLO('best.pt')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame,(1024,720))

    results = model(frame)

    boxes = results[0].boxes
    for box in boxes:

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0]
        cls = int(box.cls[0])
        label = model.names[cls]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        text = f'{label} {conf:.2f}'
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2)

    cv2.imshow('cam', frame)

    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite('img.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()
