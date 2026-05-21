# Ejercicio 3: Programación de producción en planta manufacturera

## 1. Enunciado

Decidir qué líneas de producción (L1, L2) encender y cuántos productos (A, B, C) asignar a cada una. Se busca maximizar la ganancia neta respetando la capacidad de consumo de materia prima por línea y los topes de demanda.

- Precios: A(120), B(150), C(90)
- Demandas máximas: A(80), B(60), C(100)

### Línea 1

- CF: 5000
- Cap: 300
- Consumo unitario:
  - A(2)
  - B(3)
  - C(1)

### Línea 2

- CF: 6000
- Cap: 250
- Consumo unitario:
  - A(1.5)
  - B(2)
  - C(2.5)


# 2. Planteamiento Matemático

Variables:

$$
w_1,w_2 \in \{0,1\}
$$

$$
p_{ij}\geq0
$$

## Función Objetivo

$$
\max Z=
120(p_{a1}+p_{a2})
+150(p_{b1}+p_{b2})
+90(p_{c1}+p_{c2})
-5000w_1
-6000w_2
$$

## Restricciones principales

### Línea 1

$$
2p_{a1}
+3p_{b1}
+1p_{c1}
\leq300w_1
$$

### Línea 2

$$
1.5p_{a2}
+2p_{b2}
+2.5p_{c2}
\leq250w_2
$$

### Límite de ventas por producto

$$
p_{a1}+p_{a2}\leq80
$$

$$
p_{b1}+p_{b2}\leq60
$$

$$
p_{c1}+p_{c2}\leq100
$$
