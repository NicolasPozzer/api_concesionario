from fastapi import APIRouter, Query, Path #Query y Path para validaciones.
from config.DataBase import lista_autos, lista_motos
from models.Moto import Moto
from models.Vehiculo import Vehiculo
from fastapi import APIRouter, Query, Path
from typing import List, Optional

router = APIRouter()

#List Vehiculos
@router.get("/vehiculos", response_model=List[Vehiculo])#
def get_Vehiculos():
    lista_vehiculos = lista_autos + lista_motos
    return  lista_vehiculos

#List Motos
@router.get("/vehiculos/motos", response_model=List[Moto])#
def get_Motos():
    return  lista_motos


# Crear Motos
@router.post("/vehiculos/motos/crear", response_model=Moto)
def create_Moto(moto: Moto):
    lista_motos.append(moto)
    return moto

# Crear Autos

#Limitar Velocidad de todos los vehiculos
@router.post("/vehiculos/limitar/{velocidad}")
def limitar_velocidad(velocidad: float):
    listaVehiculos = lista_autos + lista_motos

    for vehiculo in listaVehiculos:
        vehiculo.velocidad = velocidad


#Vehiculos con precio menor a..
@router.get("/vehiculos/limitprice/{price}", response_model=List[Vehiculo])
def precio_menor(price: float):
    listaVehiculos = get_Vehiculos()
    listaMenores = []

    for vehiculo in listaVehiculos:
        if vehiculo.price < price:
            listaMenores.append(vehiculo)

    return listaMenores


"""
@router.get("/Vehiculoos/{id}", response_model=Optional[Vehiculo])
def find_Vehiculo(id: int = Path(gt=0)):
    Vehiculoo = next((item for item in lista_Vehiculoos if item.id == id), None)
    if Vehiculoo:
        return Vehiculoo
    return {"error": "Vehiculoo no encontrado"}

@router.put("/Vehiculoos/{id}", response_model=Optional[Vehiculo])
def edit_Vehiculo(id: int, Vehiculo: Vehiculo): #Necesitamos el id y el objeto con sus datos.
    for index, item in enumerate(lista_Vehiculoos): #Con esta linea tenemos acceso al item actual del Vehiculoo y a su posicion.
        if item.id == id:
            lista_Vehiculoos[index] = Vehiculo #Busca el indice y lo mete al nuevo obj. editado.
            return Vehiculo #Retornamos el obj. actualizado
    return {"error": "Vehiculoo no encontrado"}

@router.delete("/Vehiculoos/{id}", response_model=Optional[dict])
def delete_Vehiculo(id: int):
    for item in lista_Vehiculoos: #Usamos for comun ya que necesito acceder al valor del item no a la posicion.
        if item.id == id: #Encontramos el item con el id que sea igual al id ingresado por el Usuario.
            lista_Vehiculoos.remove(item) #Una vez que borramos retornamos un mensaje.
            return {"message": "Vehiculoo eliminado"}
    return {"error": "Vehiculoo no encontrado"}


#End-Points Externos de CRUD con Parametros Query
# Ej. Vehiculoos/?price=10&stock=20
@router.get("/Vehiculoos/stockigual", response_model=List[Vehiculo])
#La forma de declarar los parametros query es por medio de los parametros de la funcion
# ya que no son parametros de ruta de una url sino de un body de un obj. hay que declaralos
# de esta manera para que FastApi los detecte. Ej. stock: int como esta abajo...
def get_Vehiculoos_by_stock(stock: int, price: float = Query(gt=0)):#Query para validar parametros tipo RequestParam
    return [item for item in lista_Vehiculoos if item.stock == stock and item.price == price]

"""