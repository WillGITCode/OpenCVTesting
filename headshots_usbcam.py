import cv2

name = 'William' #replace with your name

cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 304)
# cam.set(cv2.CAP_PROP_FPS, 10)
    
img_counter = 0

while True:
    ret, image = cam.read()
    cv2.imshow("Press Space to take a photo", image)
    
    k = cv2.waitKey(1)
    if k%256 == 27: # ESC pressed
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, image)
        print("{} written!".format(img_name))
        img_counter += 1
            
if k%256 == 27:
    print("Escape hit, closing...")


cv2.destroyAllWindows()

