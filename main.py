import cv2
import mediapipe as mp
import json

image = cv2.imread("tom-hanks-niece.jpg")

# Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Facial landmarks
result = face_mesh.process(rgb_image)

height, width, _ = image.shape

landmarks = []

if result.multi_face_landmarks:
    for facial_landmarks in result.multi_face_landmarks:
        face_landmarks = []
        for i in range(0, 468):
            pt1 = facial_landmarks.landmark[i]
            x = int(pt1.x * width)
            y = int(pt1.y * height)
            face_landmarks.append({"x": x, "y": y})
            cv2.circle(image, (x, y), 5, (100, 100, 0), -1)
        landmarks.append(face_landmarks)

# Save landmarks as JSON
with open("landmarks.json", "w") as json_file:
    json.dump(landmarks, json_file, indent=4)

cv2.imshow("Image", image)
cv2.imwrite("output_image.png", image) # Save the image
cv2.waitKey(0)
cv2.destroyAllWindows()