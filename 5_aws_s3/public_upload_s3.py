import os
import boto3

session = boto3.Session(profile_name="default")
s3 = session.client("s3")

bucket_name = "jihyun-2024-bigdata-practice"
folder_name = "2024/"
key = "marie.jpeg"
target_key = "marie.png"

# os.getcwd() -> 현재 폴더
local_file_path = os.getcwd() + "/" + key

# 올릴 파일, 버켓명, 저장할 객체명
s3.upload_file(
    local_file_path,
    bucket_name, 
    folder_name + target_key
)