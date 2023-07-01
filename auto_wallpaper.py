#automated wallpaper settings in python

import requests
import json

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Get the JSON
response = requests.get(api_url)
content = response.content.decode('UTF-8')

# Convert string to JSON
dict_content = json.loads(content)

# Get the image URL
image_url = dict_content['url']

#download the image
res= requests.get(image_url)

#save the image
with open('apod.png','wb') as image:
    image.write(res.content)
