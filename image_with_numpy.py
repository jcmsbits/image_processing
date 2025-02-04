from skimage import data
import matplotlib.pyplot as plt
from data_rgb_gray import show_image
import numpy as np

# Al cargar la imagen con matplotlib nos devuelve un objeto
# de tipo de array
campeones_image = plt.imread("./campeones.jpg")
print(type(campeones_image))

# obteniendo los colores de la imagen
red = campeones_image[ :, :, 0]
green = campeones_image[ :, :, 1]
blue = campeones_image[ :, :, 2]

# for img, name in [(red, "Red"), (green, "Green"), (blue, "Blue")]:
#     show_image(img, name )

# Shape nos da la cantidad de matrices y los canales
print("Shape of image: ", campeones_image.shape)

# Size es la cantidad de pixeles totales que hay en la imagen
print("Size: ", campeones_image.size)

# Girar la imagen con flip verticalmente
verically_flippped = np.flipud(campeones_image)
# show_image(verically_flippped)

# Girar la imagen horizontalmente
horizontally_flipped = np.fliplr(campeones_image)
# show_image(horizontally_flipped)

# Histograms in Matplotlib
# El método ravel aplana a una matriz
# Bins = 256 porque son 256 valores en la matriz de colores
plt.hist(red.ravel(), bins = 256)
plt.show()