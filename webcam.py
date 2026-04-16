import cv2

camera = cv2.VideoCapture(0)

while True:
    check,img = camera.read() # Mostar a webcam

    cv2.imshow("Webcam", img) # Mostrar a janela 
    if cv2.waitKey(1) & 0xFF == ord('q'): # se o usuario apertar a tecla "q", e ele ira fechar em 1 milissegundo
        break 