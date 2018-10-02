##### live webcam screenshot
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import cv2
import time
import datetime
import os

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

j_cam = "https://www.youtube.com/watch?v=nKMuBisZsZI" # japanese crosswalk
b_cam ="https://www.youtube.com/watch?v=2UIA8xOVcOs" # bear creek
t_cam = "https://www.youtube.com/watch?v=ydZBBAPE_mw" # thailand cafe cam

if __name__ == "__main__":

    driver.get(j_cam)
    time.sleep(2) #time to wait for buffering logo to leave image
    driver.save_screenshot("[placeholder]_cam_{0}_{1}_{2}.png".format(str(datetime.datetime.now().month),
                                                                    str(datetime.datetime.now().day),
                                                                    str(datetime.datetime.now().year)))
    driver.close()

    # resize images in folder
    filelist = os.listdir(".")
    for file in filelist:
        if file.endswith(".png"):
            im = cv2.imread(file)
            crop_im = im[80:520,50:880] # hard crops for window frame
            cv2.imwrite(file[:-4]+"_cropped.png",crop_im)
            os.remove(file)
