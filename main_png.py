import cv2
import json
import textract
import pdf2image
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

#Português
#Pegando o arquivo PDF e convertendo para PNG 
#
#English
#Picking the PDF file and converting it to PNG
#

from pdf2image import convert_from_path
pages = convert_from_path('pdf_file.pdf', 500)

#Português
#Salvando páginas em PNG
#
#English
#Saving pages in PNG format
#

for page in pages:
    page.save('convert_file.png', 'PNG')

#Português
#Utilizando Pytesseract para salvar a ler a imagem e o CV2 para corta-la
#
#English
#Using Pytesseract to save reading the image and CV2 to cut it
#

print(pytesseract.image_to_string(Image.open('convert_file.png'), lang='por'))
img = cv2.imread("convert_file.png")

#Português
#Área selecionada para corte e salvando a imagem cortada.
#
#English
#Selected area for cropping and saving the cropped image.
#

crop_img = img[325:500, 15:1350]
h, w, _= img.shape
print(h, w)
cv2.imwrite("cut_file.png", crop_img,)

#Português
#Extraindo o texto da imagem e salvando em Json.
#
#English
#Extracting the image text and saving on Json.
#

data = pytesseract.image_to_string(Image.open('cut_file.png'),config="11")

with open("file_json.json", "w") as out:
    json.dump(data, out)

