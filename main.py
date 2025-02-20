import cv2
import mediapipe as mp
import json

image = cv2.imread("input_image.jpg")

# Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Facial landmarks
result = face_mesh.process(rgb_image)

height, width, _ = image.shape

landmarks = {
    "eyes": [],
    "lips": [],
    "eyebrows": [],
    "nose": [],
    "face_outline": []
}

# Define landmark indices for different facial features
eyes_indices = list(range(33, 133)) + list(range(362, 463))
lips_indices = list(range(78, 88)) + list(range(308, 318))
eyebrows_indices = list(range(46, 67)) + list(range(276, 297))
nose_indices = list(range(1, 9)) + list(range(195, 197))
face_outline_indices = list(range(10, 34)) + list(range(297, 338))

if result.multi_face_landmarks:
    for facial_landmarks in result.multi_face_landmarks:
        for i in range(0, 468):
            pt1 = facial_landmarks.landmark[i]
            x = int(pt1.x * width)
            y = int(pt1.y * height)
            landmark = {"x": x, "y": y}

            if i in eyes_indices:
                landmarks["eyes"].append(landmark)
            elif i in lips_indices:
                landmarks["lips"].append(landmark)
            elif i in eyebrows_indices:
                landmarks["eyebrows"].append(landmark)
            elif i in nose_indices:
                landmarks["nose"].append(landmark)
            elif i in face_outline_indices:
                landmarks["face_outline"].append(landmark)

            cv2.circle(image, (x, y), 5, (100, 100, 0), -1)

# Save landmarks as JSON
with open("landmarks.json", "w") as json_file:
    json.dump(landmarks, json_file, indent=4)

cv2.imshow("Image", image)
cv2.imwrite("output_image.png", image) # Save the image
cv2.waitKey(0)
cv2.destroyAllWindows()