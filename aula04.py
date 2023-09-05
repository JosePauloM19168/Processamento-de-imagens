import cv2
import numpy as np
import numpy
import matplotlib.pyplot as plt



input = "teste.jpeg"
imagem = cv2.imread(input)

# Carregar a imagem em escala de cinza
canalPretoBranco =  numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        canalPretoBranco[i][j] = (imagem[i][j].sum()//3) #tirar a media aritmética dos 3 canais rgb
       

# Encontrar os valores mínimo e máximo de intensidade na imagem
min_intensity = np.min(imagem)  
max_intensity = np.max(imagem)  

# Definir os novos valores mínimo e máximo desejados após a expansão de 0 a 255
new_min = 155
new_max = 250

# Aplicando a expansão de histograma 
expanded_image = ((canalPretoBranco - min_intensity) / (max_intensity - min_intensity)) * (new_max - new_min) + new_min
expanded_image = expanded_image.astype(np.uint8)

# Calcular o histograma da imagem expandida
histogram = cv2.calcHist([expanded_image], [0], None, [256], [0, 256])


plt.figure(figsize=(8, 6))
plt.title('Histograma Expandido')
plt.xlabel('Intensidade de Pixel')
plt.ylabel('Frequência')
plt.xlim([0, 256])
plt.plot(histogram)
plt.grid(True)
plt.show()


cv2.imshow('Imagem de Entrada', canalPretoBranco)
cv2.imshow('Imagem com Expansao de Histograma', expanded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
