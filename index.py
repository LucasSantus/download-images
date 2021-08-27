import cv2
import requests
import numpy as np
from io import BytesIO
from PIL import Image

# Lista de imagens a baixar
list_links = [
    "https://source.unsplash.com/pWkk7iiCoDM/800x600",
    "https://source.unsplash.com/aob0ukAYfuI/800x600",
    "https://source.unsplash.com/EUfxH-pze7s/800x600",
    "https://source.unsplash.com/M185_qYH8vg/800x600",
    "https://source.unsplash.com/sesveuG_rNo/800x600",
    "https://source.unsplash.com/AvhMzHwiE_0/800x600",
    "https://source.unsplash.com/2gYsZUmockw/800x600",
    "https://source.unsplash.com/EMSDtjVHdQ8/800x600",
    "https://source.unsplash.com/8mUEy0ABdNE/800x600",
    "https://source.unsplash.com/G9Rfc1qccH4/800x600",
    "https://source.unsplash.com/aJeH0KcFkuc/800x600",
    "https://source.unsplash.com/p2TQ-3Bh3Oo/800x600", 
]

# Função para recuperar imagem
def get_image(url, save_image=''):
    image = Image.open(BytesIO(requests.get(url).content))
    if save_image: 
        image.save(save_image)
    return np.array(image)

# Percorrendo lista de links
for link in list_links:
    name = f"images/image-{ list_links.index(link) }"
    dir = f"{name}.jpg"
    image = get_image(link, dir)
    cv2.imwrite(dir, image)