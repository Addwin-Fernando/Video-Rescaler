import cv2 as cv
print('** press "d" to exit out of the rescaled **')
percent = float(input("enter the Percentage the video should be resized: "))
url = input("enter the path of the video: ")


scales = percent/100

vid = cv.VideoCapture(url)

def rescaleFrame(frame, scale = scales):
    width = int(frame.shape[1] * scale)
    hieght = int(frame.shape[0] * scale)
    dimentions = (width,hieght)

    return cv.resize(frame,dimentions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = vid.read()
    frame_resized = rescaleFrame(frame)


    cv.imshow("frame_resized",frame_resized)


    if cv.waitKey(20) & 0xff==ord("d"):
        break




vid.release()
cv.destroyAllWindows()    
        




 