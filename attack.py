import requests
from person import Person


class Attack:

    def perform_attack(self, serviceList):
        for service in serviceList:
            req = requests.post(
                url=service.url, data=service.data, headers=service.headers)
            if req.status_code == 200:
                print(service.url + " SUCCESS!")
            else:
                print(req.text)

    def genPerson(self):
        return Person()

    def formatPhoneNumber(self, phone: str, mask: str, mask_symbol: str = '*'):
        if len(phone) == mask.count(mask_symbol):
            formatted_phone = ''
            for symbol in mask:
                if symbol == mask_symbol:
                    formatted_phone += phone[0]
                    phone = phone[(len(phone) - 1) * -1:]
                else:
                    formatted_phone += symbol
        else:
            formatted_phone = phone
        return formatted_phone
