# Crop.py by Stephen Wu
# Uses Croppola API to batch square crop pictures
# Thanks to Thomas Lochmatter from Croppola for assistance
# http://croppola.com/

import os, requests, shutil, json, urllib

# Set vars
path_in = 'photos'
path_out = 'photos_out' 
params = 'aspectRatio=1.0&algorithm=croppola'

# Reset folder if exists, otherwise make
if not os.path.exists(path_out):
    os.makedirs(path_out)

base = 'http://new.croppola.com/croppola/'
url = base + 'image.json?' + params

i = 0
# Batch crop
for photo in os.listdir(path_in):
    print("--------------- " + photo + " ---------------")
    if i < 100: 
        dataFile = open(path_in + '/' + photo, 'rb')
        res = requests.post(url, data=dataFile, headers={'User-Agent' : 'py'})
        if res.status_code == 200:
            print(res.content)
            d = json.loads(res.content)
            token = d["token"]
            if (len(d["faces"]) > 0) :
                head_height = d["faces"][0]["height"] * 2.35
                head_width = d["faces"][0]["width"] * 2.35
                head_x = d["faces"][0]["x"] + (d["faces"][0]["width"] - head_width) * 0.5
                head_y = d["faces"][0]["y"] + (d["faces"][0]["height"] - head_height) * 0.5
                with open(path_out + "/" + photo, 'wb') as f:
                    url2 = base + str(token) + '/image.jpg?x=' + str(head_x) + '&y=' + str(head_y) + '&width=' + str(head_width) + '&height=' + str(head_height)
                    print(url2)
                    urllib.urlretrieve(url2, path_out + "/" + photo)
            else:
                url2 = base + str(token) + '/image.jpg?' + params
                urllib.urlretrieve(url2, path_out + '/' + photo)
        else:
            print ('Error: ' + res.status_code)
    i = i + 1
