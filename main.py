from model import Model

model = Model()
model.fillServices("375447219365")

model.attack_service.perform_attack(model.services)