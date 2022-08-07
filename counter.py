import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = cv2.imread(input("ENTER THE NAME: ")+".jpg")

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    image = cv2.imread('coins.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # plt.imshow(gray, cmap='gray')
    # plt.show()

    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    canny = cv2.Canny(blur, 4, 4, 90)
    # plt.imshow(canny, cmap='gray')
    # plt.show()

    kernel = np.ones((2, 2))
    dilated = cv2.dilate(canny, kernel, iterations = 1)
    # plt.imshow(dilated, cmap='gray')
    # plt.show()

    cnt, heirarchy = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # area = cv2.arcLength(cnt,True)
    # print(type(area))
    count = 0
    for c in cnt:
        if cv2.contourArea(c)>90:
            count += 1
            cv2.drawContours(rgb, c, -1, (0,255,0), 2)
            # plt.imshow(rgb, cmap='gray')
            # plt.show()
            # print(count)
    cv2.putText(rgb, f'Coins: {count}' , (20, 35), font, 0.75, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow("Stack", rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
