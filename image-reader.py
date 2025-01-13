import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('zadanie-python.jpg')

image = image.resize((image.width * 3, image.height * 3))

gray_image = image.convert('L')

enhancer = ImageEnhance.Contrast(gray_image)
contrast_image = enhancer.enhance(2)

blurred_image = contrast_image.filter(ImageFilter.GaussianBlur(0.5))

bw_image = blurred_image.point(lambda x: 0 if x < 120 else 255, '1')

bw_image.save('processed_image_contrast.png')

custom_config = r'--oem 3 --psm 13'
text = pytesseract.image_to_string(bw_image, config=custom_config)

print(text)