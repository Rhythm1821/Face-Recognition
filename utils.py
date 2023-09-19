import cv2
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk

# Function to start capturing webcam feed
def start_camera():
    cap = cv2.VideoCapture(0)
    return cap

# Function to update the camera feed
def update_camera(cap, camera_label):
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        camera_label.config(image=photo)
        camera_label.photo = photo

# Function to stop capturing webcam feed
def stop_camera(cap):
    cap.release()

# Create the main Tkinter window
def create_gui():
    root = tk.Tk()
    root.title("Webcam GUI")

    # Create a label to display the camera feed
    camera_label = tk.Label(root)
    camera_label.pack()

    # Create buttons with styles
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 14))
    signup_button = ttk.Button(root, text="Sign Up", command=lambda: print("Sign Up clicked"))
    login_button = ttk.Button(root, text="Login", command=lambda: print("Login clicked"))

    signup_button.pack(pady=10)
    login_button.pack()

    return root, camera_label

# Main function
# def main():
#     cap = start_camera()
#     root, camera_label = create_gui()

#     def update():
#         update_camera(cap, camera_label)
#         root.after(10, update)

#     update()
#     root.mainloop()


# Load the jpg files into numpy arrays
# rhythm_image = face_recognition.load_image_file("/home/rhythm/Pictures/Profile Photo.jpg")


# try:
#     rhythm_face_encoding = face_recognition.face_encodings(rhythm_image)[0]
# except IndexError:
#     print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
#     quit()

# known_face_encodings = [
#     rhythm_face_encoding,
# ]

# known_face_names = [
#     "Rhythm",
# ]

# cap=cv2.VideoCapture(0)

# while cap.isOpened():
#     ret,frame=cap.read()


#     # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#     rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

#     # Find all the faces and face encodings in the frame of video
#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


#     # Loop through each face in this frame of video
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # See if the face is a match for the known face(s)
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

#         name = "Unknown"

#         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#         best_match_index = np.argmin(face_distances)
#         if matches[best_match_index]:
#             name = known_face_names[best_match_index]

#         # Draw a box around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Draw a label with a name below the face
#         cv2.rectangle(frame, (left, bottom+25), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left+6, bottom+21), font, 1.0, (255, 255, 255), 1)

#     cv2.imshow("frame",frame)

#     if cv2.waitKey(10) & 0xFF==ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


