from skimage import exposure, data, color
from data_rgb_gray import show_image
from filtering import plot_comparison


img_cat = data.cat()
gray_cat = color.rgb2gray(img_cat)

# Tipos de mejora de contraste
# Contrast stretching
# Histogram equalization el esparse 

# Obtain the equalize image 
image_eq = exposure.equalize_hist(gray_cat)

# Como alternativa al uso de histeq, puede 
# realizar una ecualización de histograma 
# adaptativa limitada por contraste (CLAHE) 
# mediante la función adapthisteq. Mientras 
# que histeq funciona en toda la imagen, 
# adapthisteq opera en pequeñas regiones de la imagen,
# llamadas mosaicos. adapthisteq mejora el contraste
# de cada mosaico, de modo que el histograma de la región
# de salida coincida aproximadamente con un histograma
# especificado. Después de realizar la ecualización, 
# adapthisteq combina los mosaicos vecinos mediante 
# interpolación bilineal para eliminar los límites 
# inducidos artificialmente.

# Para evitar amplificar cualquier ruido que pueda estar
# presente en la imagen, puede utilizar los parámetros
# opcionales de adapthisteq para limitar el contraste,
# especialmente en áreas homogéneas.
# Apply adaptive Equalization (La mejor)

# Clip_limit: Límite de mejora de contraste, especificado como
# un número en el rango [0, 1]. Los límites más altos dan como resultado un mayor contraste.

# ClipLimit es un factor de contraste que evita la 
# sobresaturación de la imagen específicamente en 
# áreas homogéneas. Estas áreas se caracterizan por un
# pico alto en el histograma del mosaico de imagen en 
# particular debido a que muchos píxeles se encuentran
# dentro del mismo rango de nivel de gris. Sin el límite
# de recorte, la técnica de ecualización de histograma 
# adaptativo podría producir resultados que, en algunos 
# casos, son peores que la imagen original.
image_adapteq = exposure.equalize_adapthist(img_cat, clip_limit = 0.03)



plot_comparison(gray_cat,image_adapteq, "Imagen ecualizada")