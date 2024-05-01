import os
import boto3
import time

session = boto3.Session(profile_name="default")
s3 = session.client("s3")

bucket_name = "jihyun-2024-bigdata-practice"
folder_name = "2024/"
key = "marie.jpeg"

# 버켓명, 다운받을 객체, 저장 될 위치
s3.download_file(
                    bucket_name, 
                    folder_name + os.path.basename(key),
                    "./"+os.path.basename(key)
                )