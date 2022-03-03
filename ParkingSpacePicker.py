import cv2
import pickle


width,height=107,48  #157-50  240-192
try:
   with open('CarPArkPos', 'rb') as f:
    posList=pickle.load(f)
except:
    posList=[]

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:      #to create
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:      #to delete
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

    with open('CarPArkPos','wb') as f:
        pickle.dump(posList,f)

while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img,pos, (pos[0] + width,pos[1]+height), (255, 0, 255), 2)  #PurpleColor-One rectangle for one Parking Space

    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mouseClick)        #Detect Mouse Click
    cv2.waitKey(1)