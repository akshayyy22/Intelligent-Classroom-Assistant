import cv2
import pytesseract

def extract_blackboard_images(video_file="recordings/lecture.avi", output_folder="blackboard_frames"):
    cap = cv2.VideoCapture(video_file)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        edges = cv2.Canny(gray, 50, 150)  

        if edges.mean() > 50:  
            cv2.imwrite(f"{output_folder}/frame_{frame_count}.jpg", frame)

        frame_count += 1

    cap.release()

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

if __name__ == "__main__":
    extract_blackboard_images()
    blackboard_text = extract_text_from_image("blackboard_frames/frame_10.jpg")
    print("Blackboard Extracted Text:\n", blackboard_text)
