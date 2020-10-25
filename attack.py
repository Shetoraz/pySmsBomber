import requests
from person import Person

class Attack:

    def perform_attack(self, serviceList):
        for service in serviceList:
            req = requests.post(
                url=service.url, data=service.data, headers=service.headers)
            print(req)
            print(req.text)

    def genPerson(self):
        return Person()

attacker = Attack()
