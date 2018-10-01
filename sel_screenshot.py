from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import cv2
import time


if __name__ == "__main__":

    j_cam = "https://www.youtube.com/watch?v=nKMuBisZsZI"
    driver = webdriver.Firefox()
    driver.get("https://www.youtube.com/watch?v=nKMuBisZsZI")
    time.sleep(2) #time to wait for buffering logo to leave image
    driver.save_screenshot("j_cam.png")
    driver.close()

    im = cv2.imread("j_cam.png")

    # hard crops for window frame
    crop_im = im[100:460,30:780]
    cv2.imwrite("j_cam_cropped.png",crop_im)
