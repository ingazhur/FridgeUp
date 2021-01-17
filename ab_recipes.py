from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests

class Recipes(ABC):

    def __init__(self, url):
        self.url = url
        self.link = requests.get(url)
        self.soup = BeautifulSoup(self.link.text, 'lxml')
        super().__init__()

    def find_url(self):
        return self.url

    @abstractmethod
    def find_name(self):
        pass

    @abstractmethod
    def find_ingredients(self):
        pass

    # @abstractmethod
    # def find_image(self):
    #     pass
    #
    # @abstractmethod
    # def find_preptime(self):
    #     pass
