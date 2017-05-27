import requests
from lxml.html import fromstring
from lxml import etree
from datetime import datetime 


def download_wallpaper(url):
    try:   
        r = requests.get(url)
        doc = fromstring(r.text)
        for meta in doc.cssselect('meta'):
            prop = meta.get('property')
            if prop == 'og:image':
                image_url = meta.get('content')
                r = requests.get(image_url, stream=True)
                now = datetime.now()
                fname = 'image-' + str(now) + ".jpg"
                if r.status_code == 200:
                    try:
                        with open(fname, 'wb') as f:
                            for chunk in r.iter_content(1024):
                                f.write(chunk)
                        return "Download Complete"
                        
                    except Exception as e:
                        return "Something went Wrong!"

    except:
        return "Something went Wrong!"




