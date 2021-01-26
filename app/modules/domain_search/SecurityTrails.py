import requests
from bs4 import BeautifulSoup
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class SecurityTrails:
    __WEB_SITE__ = None

    def __init__(self, website):
        self.__WEB_SITE__ = website

    @staticmethod
    def __extract_payload__(html_content):
        payload = {
            '_csrf_token': None
        }
        content = html_content.decode('utf8').split('\n')
        for line in content:
            if 'window.csrf_token' in line:
                _csrf_token = line.split('"')[1]
                payload = {
                    '_csrf_token': _csrf_token
                }
        return payload

    def __download_html_content__(self, session):
        url = "https://securitytrails.com/domain/" + self.__WEB_SITE__ + "/dns"
        response = session.get(url, verify=False)
        return response.content

    def __download_dns_information__(self, session, payload):
        r = session.post(url="https://securitytrails.com/app/api/v1/domain/" + self.__WEB_SITE__, data=payload)
        print(json.dumps(r.json(), indent=2))

    def __download_sub_domain_list__(self, session):
        page = session.get(url="https://securitytrails.com/list/apex_domain/" + self.__WEB_SITE__)
        soup = BeautifulSoup(page.text, 'html.parser')
        root_div = soup.find("div", {"id": "root"})
        table = root_div.find("table", {'class': 'table table-hover'})
        com = []
        for row in table.find_all("tr")[1:]:
            index = 0
            subdomain_data = {}
            for column in row.find_all('td'):
                data = column.text
                if index == 0 and data:
                    subdomain_data["domain"] = data
                elif index == 1 and data:
                    subdomain_data["rank"] = data
                elif index == 2 and data:
                    subdomain_data["hosting_provider"] = data
                elif index == 3 and data:
                    subdomain_data["main_provider"] = data
                index += 1
            com.append(subdomain_data)
        print(com)

    def __security_trails_info__(self):
        with requests.Session() as session:
            html_content = self.__download_html_content__(session)
            payload = self.__extract_payload__(html_content)

            # Function to get information about dns
            self.__download_dns_information__(session, payload)

            # List of sub domain from server
            self.__download_sub_domain_list__(session)

    def get(self):
        self.__security_trails_info__()
