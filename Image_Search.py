from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import Search_Tags
import base64


class Image:
    def __init__(self, link):
        self.link = link
        try:
            self.data = requests.get(self.link).content
            self.type = link.split(".")[-1]
        except requests.exceptions.InvalidSchema:
            self.data = base64.b64decode(self.link.split(",")[-1])
            self.type = self.link.split(",")[0].split("/")[-1].split(";")[0]

    def save(self, filename):
        with open(f"{filename}.{self.type}", "wb") as image_file:
            image_file.write(self.data)


def search_image(search_term: str, number_of_images: int, *tags):
    """Returns a list of images from the search results, no gif support"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    dr = webdriver.Chrome(
        executable_path='chromedriver.exe',
        options=options,
    )
    dr.get(f"http://www.google.com/search?q={search_term}&tbm=isch{''.join(tags)}")
    time.sleep(1)
    soup = BeautifulSoup(dr.page_source, "html.parser")
    dr.close()
    images = soup.find_all("img", class_="n3VNCb")
    for image in images:
        print(image.link)
    return_images = []
    for picture in images[:number_of_images]:
        return_images.append(Image(picture.get("src")))

    return return_images


images = search_image("rug", 10, Search_Tags.Gif)
for image in images:
    image.save(f"saves/{images.index(image)}")