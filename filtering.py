from skimage.filters import sobel, gaussian
from skimage.data import cat
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Función para comparar las imágenes
def plot_comparison(original, 
                    filtered,
                    another,
                    title_filtered):

    fig, (ax1, ax2, ax3) = plt.subplots(ncols = 3, figsize = (8, 6), sharex = True, sharey = True)

    ax1.imshow(original, cmap = plt.cm.gray)
    ax1.set_title("Original")
    ax1.axis("off")
    ax2.imshow(filtered, cmap = plt.cm.gray)
    ax2.set_title(title_filtered)
    ax2.axis("off")
    ax3.imshow(another, cmap = plt.cm.gray)
    ax3.set_title(title_filtered)
    ax3.axis("off")
    plt.show()

# Un algoritmo para detectar border es Sobel

img_cat = cat()
gray_cat = rgb2gray(img_cat)

# Aplicando detección de borde
edge_sobel = sobel(gray_cat)

# plot_comparison(img_cat, edge_sobel, "Bordes de gato")


# Otra técnica de filtrado es suavizado(smoothing)
# esta alarga los bordes y reduce el contraste y el ruido.
# Algunas veces si la imagen tiene una alta resolución 
# no se ve el efecto del suavizado, sin embargo, 
# un poco más de cerca se puede ver el efecto.

gaussian_image = gaussian(img_cat)

# plot_comparison(img_cat, gaussian_image, "Blurred with Gaussian Filter")