##### live webcam screenshot
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import cv2
import time
import os

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

j_cam = "https://www.youtube.com/watch?v=nKMuBisZsZI" # japanese crosswalk
b_cam ="https://www.youtube.com/watch?v=2UIA8xOVcOs" # bear creek

if __name__ == "__main__":

    driver.get(j_cam)
    time.sleep(1) #time to wait for buffering logo to leave image
    driver.save_screenshot("j_cam.png")
    driver.close()

    im = cv2.imread("j_cam.png")
    crop_im = im[80:520,50:880] # hard crops for window frame
    cv2.imwrite("j_cam_cropped.png",crop_im)

    os.remove("j_cam.png")
