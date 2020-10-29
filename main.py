from model import Model

model = Model()
model.fillServices('79998252348')

model.attack_service.perform_attack(model.services)