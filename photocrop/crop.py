# Crop.py by Stephen Wu
# Uses Croppola API to batch square crop pictures
# Thanks to Thomas Lochmatter from Croppola for assistance
# http://croppola.com/

import os, requests, json, urllib

# Set vars
path_in = 'photos'
path_out = 'photos_out' 
params = 'aspectRatio=1.0&algorithm=croppola' # Initial croppola settings
backup_params = 'aspectRatio=1.0&width=2300&height=2300&algorithm=croppola' # Used when no face is found
scale = 2.35 # Multiplier for face pic

# Reset folder if exists, otherwise make
if not os.path.exists(path_out):
    os.makedirs(path_out)

base = 'http://new.croppola.com/croppola/'
url = base + 'image.json?' + params

i = 0
# Batch crop
for photo in os.listdir(path_in):
    print("--------------- " + photo + " ---------------")
    if i < 100: # Limit at 100 just in case
        dataFile = open(path_in + '/' + photo, 'rb')
        res = requests.post(url, data=dataFile, headers={'User-Agent' : 'py'})
        if res.status_code == 200:
            print(res.content)
            d = json.loads(res.content)
            token = d["token"]
            if (len(d["faces"]) > 0):
                for face in range(0,len(d["faces"])): # Loop through all faces found
                    # Create new coordinates based on face
                    head_height = d["faces"][face]["height"] * scale
                    head_width = d["faces"][face]["width"] * scale
                    head_x = d["faces"][face]["x"] + (d["faces"][face]["width"] - head_width) * 0.5
                    head_y = d["faces"][face]["y"] + (d["faces"][face]["height"] - head_height) * 0.5
                    # Establish url with new coordinates
                    url2 = base + str(token) + '/image.jpg?x=' + str(head_x) + '&y=' + str(head_y) + '&width=' + str(head_width) + '&height=' + str(head_height)
                    print(url2)
                    # Add number for additional faces
                    split = os.path.splitext(os.path.basename(photo))
                    add = '' if face == 0 else '.' + str(face)
                    photo_out = split[0] + add + split[1]
                    # Write to file
                    with open(path_out + "/" + photo_out, 'wb') as f:
                        urllib.urlretrieve(url2, path_out + '/' + photo_out)
            else: # No faces found, resort to default params
                url2 = base + str(token) + '/image.jpg?' + backup_params
                urllib.urlretrieve(url2, path_out + '/' + photo)
        else: # Print error
            print ('Error: ' + res.status_code)
    i = i + 1
