import requests
import json


class WhoIsXml:
    __WEBSITE__ = None

    def __init__(self, website):
        self.__WEBSITE__ = website

    def __download_information__(self):
        url = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_rTccrYYeLZfhfEJUOLmJIqe6VURc2&" \
              "domainName=" + self.__WEBSITE__ + "&outputFormat=json"
        response = requests.get(url)
        print(json.dumps(response.json(), indent=2))

    def get(self):
        self.__download_information__()
