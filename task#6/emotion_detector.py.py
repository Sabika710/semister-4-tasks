import cv2
import numpy as np

# Load pre-trained Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

def analyze_personality(eyes, smiles):
    """
    Determines a personality trait based on detected facial features.
    """
    if len(smiles) > 0:
        return "Friendly and Approachable 😀"
    elif len(eyes) > 1:
        return "Curious and Alert 🤔"
    elif len(eyes) == 1:
        return "Focused or Determined 😐"
    else:
        return "Calm and Reserved 😶"

def detect_personality(image_path):
    """
    Detects personality traits from an input image.
    """
    image = cv2.imread('sample1.jpg')
    if image is None:
        print("Error: Could not read image. Check the file path.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Detect smiles
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(30, 30))
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 255), 2)

        # Determine personality based on detected features
        personality_trait = analyze_personality(eyes, smiles)
        cv2.putText(image, personality_trait, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Show the result
    cv2.imshow("Personality Detector", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
image_path = "your_image.jpg"  # Change this to the path of your input image
detect_personality(image_path)
