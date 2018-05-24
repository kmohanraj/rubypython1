from PIL import Image
import face_recognition
import io

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("/home/iteron/Pictures/12.jpg")
# image = face_recognition.load_image_file("/home/iteron/Pictures/12.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)
print (face_locations)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

# with io.FileIO("foobar.txt", "w") as file:
#     file.write("Hello!")
for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    print (">>>>>>>>ddddddddddd>>>>>>>>>>>>>>>>>")
    print (pil_image)
    print (">>>>>>>>ddddddddddd>>>>>>>>>>>>>>>>>")
    pil_image.save('/home/iteron/rubypython/fcm/raj.jpg', 'JPEG')

    temp = pil_image.show()
