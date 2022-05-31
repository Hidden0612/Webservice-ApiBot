import requests

URL_REGISTER = "https://Hidden0612.ir"
URL_SENDCODE = "https://Hidden0612.ir/SendCode"
URL_GETAPI = "https://Hidden0612.ir/GetApi"

class GetApi:
    def __init__(self, token) -> None:
        self.token = token

    def register(self) -> dict:
        data = {
            "key": self.token,
        }
        resp = requests.post(URL_REGISTER, json=data)
        return resp.json()

    def send_phone(self,phone) -> dict:
        data = {
            "key": self.token,
            "phone": phone
        }
        resp = requests.post(URL_SENDCODE, json=data)
        return resp.json()

    def send_code(self,phone,code,hash) -> dict:
        data = {
            "key": self.token,
            "phone": phone,
            "code":code,
            "hash":hash
        }
        resp = requests.post(URL_GETAPI, json=data)
        return resp.json()

