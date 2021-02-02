# python_extraction

Code made using Python to convert PDF to Image (PNG or JPEG), crop the image if necessary and extract the image data in a Json format.

## Crop Image

Português
O primeiro valor representa o X0 que será iniciado o corte e o segundo valor representa o X1 (final) da foto.
A mesma coisa se repeta para o Y0 e Y1.

English
The first value represents the X0 that will start cutting and the second value represents the X1 (end) of the photo.
The same thing is repeated for Y0 and Y1.

~~~python
crop_img = img[1300:2425, 500:2000]
~~~
