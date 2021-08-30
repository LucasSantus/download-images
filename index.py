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
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtT_Okoy-bdhjWA9QPv1tXdtoRQd7P6rOXEg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3X7iiJcDpD-QP6ln5kJmUzRbJH3Tgn5zWhg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ34iEOaXace3VrMFdmWGZlPt_tA45DhQgVUA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4-2xeXvpasKZAw31lKDmXlwDHS6IRYJmOsg&usqp=CAU",
    "https://www.hypeness.com.br/1/2018/12/imagens-surreais7.jpg",
    "https://img.cancaonova.com/cnimages/canais/uploads/sites/6/2019/11/formacao_1600x1200-imagens-e-sons-de-cada-dia.jpg",
    "https://marketingcomcafe.com.br/wp-content/uploads/2018/01/banco_de_imagens_menino.jpg",
    "https://static5.depositphotos.com/1003371/521/i/950/depositphotos_5214674-stock-photo-tropical-sea-sunset.jpg",
    "https://marketingcomcafe.com.br/wp-content/uploads/2018/01/ladi-storing-music-2-1.jpg",
    "https://marketingcomcafe.com.br/wp-content/uploads/2018/01/banco_de_imagens_free.jpeg",
    "https://marketingcomcafe.com.br/wp-content/uploads/2017/12/banco-de-imagens-morguefile.png",
]

# Função para recuperar imagem
def get_image(url, save_image=''):
    image = Image.open(BytesIO(requests.get(url).content))
    if save_image: 
        image.save(save_image)
    return np.array(image)

# Percorrendo lista de links
for link in list_links:
    try:
        name = f"images/image-{ list_links.index(link) }"
        dir = f"{name}.jpg"
        image = get_image(link, dir)
        cv2.imwrite(dir, image)
        print(f'"{link}",')
    except:
        pass