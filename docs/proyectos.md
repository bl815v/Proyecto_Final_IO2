# Ejercicio 2: Selección de proyectos de inversión

## 1. Enunciado

Seleccionar proyectos (Alpha, Beta, Gamma, Delta) y determinar la inversión en cada uno bajo restricciones de presupuesto global (200,000), exclusión mutua y límites mínimos/máximos de capital por proyecto. El objetivo es maximizar el ROI neto.

- Alpha: Fijo 10k, Inv (20k a 80k), ROI 15%
- Beta: Fijo 15k, Inv (30k a 100k), ROI 18%
- Gamma: Fijo 8k, Inv (15k a 60k), ROI 12%
- Delta: Fijo 20k, Inv (50k a 120k), ROI 20%. Excluyente con Alpha.

## 2. Planteamiento Matemático

Variables:

$$
z_a,z_b,z_g,z_d \in \{0,1\}
$$

$$
inv_a,inv_b,inv_g,inv_d \geq 0
$$

### Función Objetivo

$$
\max Z=
0.15inv_a
+0.18inv_b
+0.12inv_g
+0.20inv_d
-10000z_a
-15000z_b
-8000z_g
-20000z_d
$$

### Restricciones principales

#### Presupuesto global

$$
\sum CostosFijos+\sum Inversiones \leq 200000
$$

#### Exclusión Delta-Alpha

$$
z_a+z_d\leq1
$$
