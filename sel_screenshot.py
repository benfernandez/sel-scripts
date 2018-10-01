##### live webcam screenshot

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import cv2
import time
import os

j_cam = "https://www.youtube.com/watch?v=nKMuBisZsZI"
driver = webdriver.Firefox()

if __name__ == "__main__":

    driver.get(j_cam)
    time.sleep(2) #time to wait for buffering logo to leave image
    driver.save_screenshot("j_cam.png")
    driver.close()

    im = cv2.imread("j_cam.png")
    crop_im = im[100:460,30:780] # hard crops for window frame
    cv2.imwrite("j_cam_cropped.png",crop_im)

    os.remove("j_cam.png")
