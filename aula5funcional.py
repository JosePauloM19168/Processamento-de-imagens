import cv2
import numpy
import matplotlib.pyplot as plt


input= "predio.jpg"
img = cv2.imread(input)

img_BP =  numpy.zeros((img.shape[0], img.shape[1]), dtype = numpy.uint8)
img_equalizada = numpy.zeros((img.shape[0], img.shape[1]), dtype = numpy.uint8)
#img_modificada = numpy.zeros((img.shape[0],img.shape[1]),dtype= numpy.uint8)
histoBP = [0]*256
histo_normal= [0]*256
histoBP_acumulado=[0]*256

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_BP[i][j] = (img[i][j].sum()//3)
        histoBP[img_BP[i][j]]+=1
  

#Histograma BP

pixel1 = [0]*256
for i in range(256):
    pixel1[i] = i

#Título do gráfico
plt.xlabel('Pixel')
plt.ylabel('Quantidade') 
plt.title('Histograma Preto e Branco')
plt.bar(pixel1, histoBP, color='grey');  
plt.show()  



#Calculo Histograma Normalizado
numero_pixel = img.shape[1]*img.shape[0]

for i in range (256):
    histo_normal[i]=histoBP[i]/numero_pixel    


plt.xlabel('Pixel')
plt.ylabel('Quantidade') 
plt.title('Histograma normalizado')
plt.bar(pixel1, histo_normal, color='blue');  
plt.show() 


#Calculo do Histograma Normalizado Acumulado
aux =0
for i in range(256):
    aux+=histo_normal[i]
    histoBP_acumulado[i]=aux
    

plt.xlabel('Pixel')
plt.ylabel('Quantidade') 
plt.title('Histograma Acumulado')
plt.bar(pixel1, histoBP_acumulado, color='red');  
plt.show()  
 

#Histograma Equalizado
histoBP_mapeado = [0]*256
for i in range(256):
    histoBP_mapeado[i]=round(histoBP_acumulado[i]*255)
    

pixel = [0]*256
for i in range(256):
     pixel[i] = i


#Imagem Equalizada com o seu Histograma
histoBP_equalizado=[0]*256
for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        img_equalizada[i][j] = histoBP_mapeado[img_BP[i][j]]
        histoBP_equalizado[img_equalizada[i][j]]+=1


pixel2 =[0]*256
for i in range (256):
    pixel2[i]=i
    
plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma Equalizado')    
plt.bar(pixel2,histoBP_equalizado, color='green')      
plt.show()

cv2.imshow('foto', img_BP)
cv2.imwrite("Equalizado.jpg", img_BP)
cv2.imshow('Equalizado',img_equalizada)
cv2.imwrite("Equalizado.jpg", img_equalizada)
cv2.waitKey(0)

