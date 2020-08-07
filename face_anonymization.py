import cv2

# Detecting Faces
face_cascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')  # change with loaction of xml file


def detect_face(img):
    print('.', end='')
    face_img = img
    face_rect = face_cascade.detectMultiScale(face_img, minNeighbors=5)  # params are extra

    if len(face_rect) > 0:
        for (x, y, w, h) in face_rect:
            face_img[y:y+h, x:x+w] = cv2.blur(face_img[y:y+h, x:x+w], ksize=(30, 30))

    return face_img

##############################################################
#  CHANGE THE INPUT VIDEO NAME BELOW #
video = cv2.VideoCapture('vid_input.mp4')  # change with location of input video
print('Loading Video...')
##############################################################

if not video.isOpened():
    print("Error reading video file")
else:
    print('Video File Loaded Successfully')

width = int(video.get(3))
height = int(video.get(4))

size = (width, height)

##############################################################
# CHANGE THE OUTPUT VIDEO NAME BELOW #
result = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, size)
##############################################################

print('Working on Video', end=' ')

while True:
    ret, frame = video.read(0)

    if ret:
        frame = detect_face(frame)

        result.write(frame)

        cv2.imshow('frame', frame)
    else:
        break

print('\nVideo Editing has been Completed')

result.release()
video.release()
