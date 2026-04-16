import cv2

img = cv2.imread('thragg1.jpg') # pegando imagem thragg1
# imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) <= imagem cinza
edt = cv2.selectROI('Selecione a area de recorte', img, False) 
cv2.destroyWindow('Selecione a area de recorte') # Fechando a janela do recorte
print(edt) # mostrar os dados do edt

v1 = int(edt[0]) # selecionando o quadrado de recorte
v2 = int(edt[1]) # selecionando o quadrado de recorte
v3 = int(edt[2]) # selecionando o quadrado de recorte
v4 = int(edt[3]) # selecionando o quadrado de recorte


recorte = img[v2:v2+v4, v1:v1+v3] # aplicando o recorte
caminho = 'imagens/' # caminho pra salvar imagem
nome_arquivo = input('Digite o nome do arquivo: ') # para salvar o arquivo

cv2.imwrite(f'{caminho}{nome_arquivo}.jpg', recorte) # Salvando a imagem.jpg
print('Imagem salva com sucesso.')
cv2.imshow('imagem', recorte) # Mostrando o recorte 
cv2.waitKey(0) # fechar o recorte