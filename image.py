# Example posting a local image file:

import requests
r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('C:\\Users\\renan\\OneDrive\\Imagens\\01.jpg','rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())
