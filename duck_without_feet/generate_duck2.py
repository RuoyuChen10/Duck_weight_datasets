import cv2

pic_num = [i for i in range(10,169,2)]

for i in range(1,51):
    for j in pic_num:
        pic = cv2.imread('./'+str(i)+'/'+str(j)+'.bmp')
        cv2.imwrite('../duck2/'+str(i)+'/'+str(j)+'.jpg',pic)
    print('finish '+str(i)+'/50!')