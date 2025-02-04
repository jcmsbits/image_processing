from skimage import color
from data_rgb_gray import show_image
import matplotlib.pyplot as plt



# Thresholding es un simple método de segmentación de imágenes
# Solo para imagenes en escala de grises
# Este enfoque funciona bien en imágenes con alto
# contraste entre los objetos y el fondo, lo que 
# permite una delimitación clara de los objetos. 
# Al simplificar la imagen, el umbral facilita un 
# análisis más detallado, mejorando varios métodos 
# de segmentación y convirtiéndolo en un paso de 
# preprocesamiento fundamental en la visión por computadora.

img = plt.imread("./campeones.jpg")
img_gray = color.rgb2gray(img)
print("Shape: ", img_gray.shape)

# Obtain the optimal threshold value
thresh = 127

# Apply thresholding to the image
binary = img_gray > thresh

# Show the original and thresholded
# show_image(img_gray, "Grayscale")
# show_image(binary, "Binary")

# Categories or histogram bases: good for uniform backgrouds
# Local or adaptive: for uneven background illumination

# Si quieres probar otros algoritmos puedes usar try_all_threshold
from skimage.filters import try_all_threshold
# Obtienes todas las imagenes resultantes
fig, ax = try_all_threshold(img_gray, verbose = False)

# Cuando el fondo es uniforme o tiene alto constraste, umbral global funciona mejor

# Anteriormente pusimos un umbral arbitrario pero podemos encontrar el mejor umbral
from skimage.filters import threshold_otsu

thresh = threshold_otsu(img_gray)

# Si la imagen no tiene alto contraste o tiene un desigual o irregular fondo
# podemos usar un umbral local
from skimage.filters import threshold_local

# Tamaño impar del vecindario de píxeles
# que se utiliza para calcular el valor umbral (p. ej., 3, 5, 7, ..., 21, ...).
block_size = 35

# offset Constante restada de la media ponderada del vecindario para calcular
# el valor del umbral local. El desplazamiento predeterminado es 0.
local_thresh = threshold_local(img_gray, block_size, offset = 10)