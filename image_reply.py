# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import cv2
import boto3

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
AWS_REGION_NAME = os.getenv('AWS_REGION_NAME', None)
AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME', None)

# s3 enviroment setting
session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                region_name=AWS_REGION_NAME)
s3 = session.resource('s3')
bucket = s3.Bucket(AWS_S3_BUCKET_NAME)
s3_url = "https://s3-{}.amazonaws.com/{}/".format(AWS_REGION_NAME, AWS_S3_BUCKET_NAME)

# face mask app setting
CASCADE_PATH = "haarcascade_frontalface_default.xml"
mask = cv2.imread("sampleimage/shirotan.jpg")


def createReply(img_f_name, id):
    img = cv2.imread(img_f_name)
    masked_img = faceMask(img.copy())
    org_url, prev_url = saveImage(img, masked_img, id)
    return org_url, prev_url


def saveImage(raw_img, reply_img, id):
    raw_name = "images/" + str(id) + "_raw.jpg"
    org_name = "images/" + str(id) + "_org.jpg"
    prev_name = "images/" + str(id) + "_prev.jpg"

    prev_img = cv2.resize(reply_img, (100, 100))

    tmp = "temp.jpg"
    cv2.imwrite(tmp, raw_img)
    bucket.upload_file(tmp, Key=raw_name)

    cv2.imwrite(tmp, reply_img)
    bucket.upload_file(tmp, Key=org_name)

    cv2.imwrite(tmp, prev_img)
    bucket.upload_file(tmp, Key=prev_name)

    org_url = s3_url + org_name
    prev_url = s3_url + prev_name

    return org_url, prev_url


def faceMask(img):
    cascade = cv2.CascadeClassifier(CASCADE_PATH)
    facerect = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, minSize=(10, 10))
    if len(facerect) > 0:
        for rect in facerect:
            resize_mask = cv2.resize(mask, tuple(rect[2:4]))
            img[rect[1]:(rect[1]+rect[3]), rect[0]:(rect[0]+rect[2])] = resize_mask
    return img


def test():
    print(createReply('sampleimage/face_sample.jpg', "123456789"))


if __name__ == "__main__":
    test()
