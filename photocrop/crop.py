# Crop.py by Stephen Wu
# Uses Croppola API to batch square crop pictures
# Thanks to Thomas Lochmatter from Croppola for assistance
# http://croppola.com/

import os, requests, shutil

# Set vars
path_in = 'photos'
path_out = 'photos_out' 
params = 'aspectRatio=1.0&width=2300&height=2300&algorithm=croppola'

# Reset folder if exists, otherwise make
if os.path.exists(path_out):
    shutil.rmtree(path_out)
    os.makedirs(path_out)
else:
    os.makedirs(path_out)

url = 'http://croppola.com/croppola/image.jpg?' + params

i = 0
# Batch crop
for photo in os.listdir(path_in):
    print(photo)
    if i < 0: # Limit # of requests for now
        dataFile = open(path_in + '/' + photo, 'rb')
        res = requests.post(url, data=dataFile, headers={'User-Agent' : 'py'})
        if res.status_code == 200:
            with open(path_out + '/' + photo, 'wb') as f:
               f.write(res.content)
        else:
            print ('Error: ' + res.status_code)
    i = i + 1
