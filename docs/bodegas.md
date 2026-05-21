# Ejercicio 1: Expansión de bodegas logísticas

## 1. Enunciado

Una empresa logística debe decidir en cuáles ciudades (Bogotá, Medellín, Cali) abrir nuevas instalaciones y qué cantidad de carga almacenar en cada una. Abrir una bodega tiene un costo fijo elevado, pero permite obtener ganancias por cada tonelada almacenada. Se cuenta con un presupuesto máximo de 100,000 y se debe cumplir con una demanda mínima de 180 toneladas. Solo se pueden abrir un máximo de 2 bodegas.

- Bogotá: Capacidad 200t, Costo Fijo 50,000, Ganancia/t 300
- Medellín: Capacidad 150t, Costo Fijo 40,000, Ganancia/t 350
- Cali: Capacidad 100t, Costo Fijo 35,000, Ganancia/t 280

# 2. Planteamiento Matemático

Variables:

$$
y_{bog}, y_{med}, y_{cal} \in \{0,1\}
$$

$$
x_{bog}, x_{med}, x_{cal} \geq 0
$$

## Función Objetivo

$$
\max Z =
300x_{bog}
+350x_{med}
+280x_{cal}
-50000y_{bog}
-40000y_{med}
-35000y_{cal}
$$

## Restricciones

### Presupuesto

$$
50000y_{bog}
+40000y_{med}
+35000y_{cal}
\leq 100000
$$

### Máximo de aperturas

$$
y_{bog}+y_{med}+y_{cal}\leq 2
$$

### Demanda mínima

$$
x_{bog}+x_{med}+x_{cal}\geq 180
$$

### Capacidad

$$
x_{bog}\leq 200y_{bog}
$$

$$
x_{med}\leq 150y_{med}
$$

$$
x_{cal}\leq 100y_{cal}
$$
