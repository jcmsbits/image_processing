from skimage.util import random_noise
from skimage import color, io
from filtering import plot_comparison
# El ruido digital es la variación aleatoria 
# (que no se corresponde con la realidad) del 
# brillo o el color en las imágenes digitales
# producido por el dispositivo de entrada 
# (la cámara digital en este caso).
# Es ese efecto “indeseable” 
# consistente en la aparición aleatoria de señales
# ajenas a la imagen original, especialmente apreciable
# en las zonas de sombra de la imagen.

image = io.imread("campeones.jpg")
gray_image = color.rgb2gray(image)
# Agregando ruido a la image
noisy_image = random_noise(gray_image)


# Tipos de algoritmos para quitar el ruido
# Total variations (TV)
# Bilateral (suaviza la imagen mientras que precerva los bordes)
# Wavelet denoising
# Non-local means denoising 

# Usando total variation
from skimage.restoration import denoise_tv_chambolle
# Mayor weight menor el ruido pero tambien hace la imagen mas suave
denoised_image = denoise_tv_chambolle(noisy_image, weight=0.1)

# Bilateral filter (no siempre es el mejor)
from skimage.restoration import denoise_bilateral
bf_denoised_image = denoise_bilateral(noisy_image)

plot_comparison(noisy_image,denoised_image, bf_denoised_image, "Bilateral")