from skimage import data, color
import matplotlib.pyplot as plt

# carga de imagen
rocket_image = data.rocket()

def show_image(image, title = "Image", cmap_type = "gray"):
    plt.imshow(image, cmap = cmap_type )
    plt.title(title)
    plt.axis("off")
    plt.show()

# show_image(rocket_image)

# Cambiar imagen de color a escala de grises
gray_scale = color.rgb2gray(rocket_image)

# show_image(gray_scale, title = "Grayscale")