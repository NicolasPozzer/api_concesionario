# Base de datos lógica como una lista de instancias de Product
from models.Auto import Auto
from models.Moto import Moto

lista_autos = [
    Auto(id=1,marca="Ferrari",modelo="Enzo",price=200000,velocidad=270.00,id_auto=1,puertas=4),
    Auto(id=2,marca="MacLaren",modelo="P1",price=400000,velocidad=330.00,id_auto=2,puertas=4),
    Auto(id=3,marca="Ferrari",modelo="sena",price=8700000,velocidad=420.00,id_auto=3,puertas=4)
]

lista_motos = [
    Moto(id=1,marca="Honda",modelo="t4",price=500000,velocidad=220.00,id_moto=1,electrica=True),
    Moto(id=2,marca="Yamaha",modelo="R1",price=87500000,velocidad=440.00,id_moto=2,electrica=False),
    Moto(id=3,marca="Kawasaki",modelo="Gletter",price=6600000,velocidad=360.00,id_moto=3,electrica=False)
]