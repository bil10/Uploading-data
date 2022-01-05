import json
import requests
from plyer import notification

headers = {"Authorization": "Bearer ##access token##"}
para = {
    "name": "File1.jpg",
    #"parents" : ["12pp_CUbl0srvKD6c3h8FCPeqMWex3Ivw"] # in order to upload the file to a folder
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./nat2.jpg", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
notification.notify(
    title = "Message from PC",
    message = "File sensed",
    timeout = 10 
)

print(r.text)