import face_recognition
from PIL import Image,ImageFilter

def anonymizephoto(originalphoto,outputphoto):
	originalimage = Image.open(originalphoto)
	width, height = originalimage.size
	image = face_recognition.load_image_file(originalphoto)
	face_locations = face_recognition.face_locations(image)


	for face_location in face_locations:
		top, fwidth, fheigth, left = face_location
		cropped_image = originalimage.crop((left,top,fwidth,fheigth ))
		blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=3))
		originalimage.paste(blurred_image,(left,top,fwidth,fheigth))
	
	originalimage.save(outputphoto)
