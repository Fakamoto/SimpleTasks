# -*- coding: utf-8 -*-


# Ejercicio clase 6
import json
path = "./pedidos.json"
tamaños = [{"pequeño" : 100}, {"mediano" : 200}, {"grande" : 300}]
toppings = [{"ajo" : 10}, {"cebolla" : 10}, {"sardina" : 10}, {"jamon" : 10}]

try:
  if pedidos_totales:
    pass
except:
  pedidos_totales = []


# Def Functions..
def tomar_pedido():
  print("hola, que tamaño de pizza desea? ")
  tamaño = input("Pequeña por un precio de 100, presione (1)\nMediana por un precio de 200, presione (2)\nGrande por un precio de 300, presione (3)\n")
  pedido_tamaño = {}
  pedido_toppings = {}
  pedido = [pedido_tamaño, pedido_toppings]
  if tamaño == "1":
    pedido_tamaño["tamaño"] = tamaños[0]
  elif tamaño == "2":
    pedido_tamaño["tamaño"] = tamaños[1]
  elif tamaño == "3":
    pedido_tamaño["tamaño"] = tamaños[2]
  
  print("\nQue toppins de pizza desea? ")
  ajo = input("\nDesea agregar Ajo por un precio de 10?\nPresione 1 en caso de querer agregar el ingrediente a la pizza, de lo contrario oprima cualquier tecla.")
  cebolla = input("\nDesea agregar Cebolla por un precio de 10?\nPresione 1 en caso de querer agregar el ingrediente a la pizza, de lo contrario oprima cualquier tecla.") 
  sardina = input("\nDesea agregar Sardina por un precio de 10?\nPresione 1 en caso de querer agregar el ingrediente a la pizza, de lo contrario oprima cualquier tecla.")
  jamon = input("\nDesea agregar Jamon por un precio de 10?\nPresione 1 en caso de querer agregar el ingrediente a la pizza, de lo contrario oprima cualquier tecla.")
  if ajo == "1":
    pedido_toppings["topping_1"] = toppings[0]
  if cebolla == "1":
    pedido_toppings["topping_2"] = toppings[1]
  if sardina == "1":
    pedido_toppings["topping_3"] = toppings[2]
  if jamon == "1":
    pedido_toppings["topping_4"] = toppings[3]
  pedidos_totales.append(pedido)

def guardar_pedido(pedido):
  with open(path, "a") as f:
    print(pedido)
    json.dump(pedido, f)
    
def cargar_pedidos():
  with open(path, "r") as f:
    content = json.load(f)
  return content

def calcular_precio(pedidos_totales):

  ganancia = 0
  for i in pedidos_totales:
    for f in i:
      for x in f.values():
        for v in x.values():
          ganancia += v
  print("\n\nlas ganancias del dia son:", ganancia)
def encender_programa():  
  while True:
    tomar_pedido()
    interruptor = input("\nSi desea pedir otra pizza presione (1), de lo contrario presione cualquier tecla.")
    if interruptor != "1":
      break

# Ejecucion
encender_programa()
guardar_pedido(pedidos_totales)
calcular_precio(cargar_pedidos())


# Reiniciar
pedidos_totales = []
with open(path, "w") as f:
  del f
