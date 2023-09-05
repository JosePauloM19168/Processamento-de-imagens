import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregar a imagem em escala de cinza
img = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)

# Calcular o histograma
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Normalizar o histograma
hist_norm = hist / hist.sum()

# Calcular o histograma acumulado
hist_accumulated = np.cumsum(hist_norm)

# Mapear as intensidades de pixel usando o histograma acumulado
equ_img = (hist_accumulated[img] * 255).astype(np.uint8)

# Plotar a imagem original e a imagem equalizada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagem Original')

plt.subplot(1, 2, 2)
plt.imshow(equ_img, cmap='gray')
plt.title('Imagem Equalizada (Usando Normalização Acumulada)')

plt.show()
