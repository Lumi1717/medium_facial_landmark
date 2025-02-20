# Facial Landmark Detection with MediaPipe

This project demonstrates how to use MediaPipe for facial landmark detection. The script processes an image to detect facial landmarks and visualize them on the image.  The landmark data is also saved for further analysis.

## Files

*   `facial_landmark_detection.py`: The main script that performs facial landmark detection. See [Usage](#usage) for instructions on running this script.
*   `input_image.jpg`: The input image used for facial landmark detection. Feel free to replace this with your own image.
*   `output_with_landmarks.png`: The output image with facial landmarks marked. This file is generated when you run `facial_landmark_detection.py`.
*   `landmark_data.json`: The JSON file containing the mathematical output of the facial landmarks. This file is generated when you run `facial_landmark_detection.py`.
*   `README.md`: This file, providing instructions and information about the project.

## Usage <a name="usage"></a>

1.  **Install Dependencies:** Ensure you have the required dependencies installed:

    ```bash
    pip install opencv-python mediapipe
    ```

2.  **Run the Script:** Execute the following command in your terminal:

    ```bash
    python facial_landmark_detection.py
    ```

3.  **View Results:** The script will:
    *   Display the image with facial landmarks marked.
    *   Save the image with landmarks as `output_with_landmarks.png`.
    *   Save the facial landmark data as `landmark_data.json`.

## Description

This project serves as a practical example for demonstrating how facial landmark data is collected using MediaPipe.  The `facial_landmark_detection.py` script reads an image (`input_image.jpg`), processes it using MediaPipe to detect facial landmarks, and visualizes these landmarks on the image. The detected landmarks are also saved in a JSON file (`landmark_data.json`), which contains the numerical coordinates of the landmarks.

## Get Started with Your Own Project

Feel free to fork this repository to use as a starting point for your own facial landmark detection project.  You can modify the script, use different input images, and extend the functionality to suit your specific needs.

## Task List

1.  **Install Dependencies:** Install the necessary libraries (`opencv-python` and `mediapipe`) using `pip`.
2.  **Run the Script:** Execute the `facial_landmark_detection.py` script.
3.  **Examine Output:** Open `output_with_landmarks.png` to see the visualized facial landmarks.
4.  **Inspect Landmark Data:** Open `landmark_data.json` to examine the numerical data representing the facial landmarks. Try to correlate the data points with the landmarks you see in the image.
5.  **Experiment (Optional):** Replace `input_image.jpg` with your own image and re-run the script. Observe how the landmark detection changes.
6.  **Fork and Customize (Optional):** Fork this repository and modify the code to create your own unique facial landmark detection project.