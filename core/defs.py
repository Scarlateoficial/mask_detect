from requests import post
import cv2
import numpy as np


def alerta_user(roi):
    cv2.imwrite("core/temp/x.png", roi)
    payload = {"image": open("core/temp/x.png", "rb")}
    header = {"Authorization": "Token aed2507e817bcf63b1a8e40239eded74a849ae1c"}
    post(
        "http://127.0.0.1:8080/face_detection/alert_user/",
        files=payload,
        headers=header,
    ).json()
