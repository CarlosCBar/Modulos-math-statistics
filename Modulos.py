import math
import statistics as stats

print(f"The value of pi is: {math.pi}")

print(f"Square root of 1908 is: {math.sqrt(1908)}")

print(math.e)

#para redondear un número se usa ----- math.ceil(XXX) ----
x = 586
RAIZ = math.sqrt(x)
REDONDEA = math.ceil(RAIZ)
redondea_abajo = math.floor(RAIZ)

# import pygal dice que es un modulo en linea
# para conseguir info de un modulo usamos 'help()' -->  help(math)
# Podemos importar solamente un elemento de un modulo ---- from math import pi  -----
# Podemos modificar el nombre de un modulo importando usando ----- import statistics as stats-----


# MODULO statistics

valores = [5,2,3,6,9,2,1,4,7,8,5,2,1,4,6,5,4,7]
#mean = statistics.mean(valores)
mean = stats.mean(valores)
median = stats.median(valores)


