import cv2
import pyttsx3
import threading
import time


# ==========================================
# VOICE FUNCTION
# ==========================================

def speak(text):

    def voice():

        engine = pyttsx3.init()

        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()

    threading.Thread(
        target=voice,
        daemon=True
    ).start()


# ==========================================
# FACE DETECTION
# ==========================================

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)


if face_cascade.empty():

    print("ERROR: Face detector not loaded.")

    exit()


# ==========================================
# CAMERA
# ==========================================

cap = cv2.VideoCapture(0)


if not cap.isOpened():

    print("ERROR: Camera could not be opened.")

    exit()


print("================================")
print("AI VISION ASSISTANT STARTED")
print("================================")
print("Camera: ON")
print("Face Detection: ON")
print("Voice Assistant: ON")
print("Press Q to quit.")
print()


# ==========================================
# GREETING SETTINGS
# ==========================================

last_greeting_time = 0

COOLDOWN = 8


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    ret, frame = cap.read()

    if not ret:

        print("ERROR: Could not read camera.")

        break


    # Convert image to grayscale

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    # Detect faces

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60, 60)
    )


    current_time = time.time()


    # ======================================
    # FACE FOUND
    # ======================================

    if len(faces) > 0:

        # Greeting cooldown

        if current_time - last_greeting_time > COOLDOWN:

            print("Face detected!")
            print("AI: Hello sir, how can I help you today?")

            speak(
                "Hello sir, how can I help you today?"
            )

            last_greeting_time = current_time


        # Draw face boxes

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "User Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )


    # ======================================
    # STATUS
    # ======================================

    if len(faces) > 0:

        status = "Face Detected"
        color = (0, 255, 0)

    else:

        status = "Searching for face..."
        color = (0, 0, 255)


    cv2.putText(
        frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )


    # ======================================
    # SHOW CAMERA
    # ======================================

    cv2.imshow(
        "AI Vision Assistant",
        frame
    )


    # ======================================
    # QUIT
    # ======================================

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break



cap.release()

cv2.destroyAllWindows()

print("AI Vision Assistant stopped.")