from PIL import Image

im=Image.open("foto.jpg")

print("format file :",im.format)
print("Ukura file :",str(im.size))
print("mode file :",im.mode)

im.show()

import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9])