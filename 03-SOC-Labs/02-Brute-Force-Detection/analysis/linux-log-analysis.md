# Análisis de registros de seguridad mediante la línea de comandos

## 1. Objetivo

El objetivo de este ejercicio fue desarrollar habilidades fundamentales en el uso de la línea de comandos para el análisis de registros de seguridad.

La investigación se centró en filtrar eventos de autenticación, extraer campos relevantes, contar valores repetidos, identificar patrones y aplicar un umbral básico de detección.

El ejercicio se realizó utilizando registros SSH de autenticación simulados.

---

## 2. Entorno

- **Sistema operativo:** Terminal de Linux.
- **Formato de registros:** Registros de autenticación SSH.
- **Fuente de datos:** Eventos de seguridad simulados.
- **Tipo de análisis:** Análisis de registros mediante la línea de comandos.
- **Herramientas principales:** `grep`, `awk`, `sort`, `uniq`, `wc`, `head`, `tail`.

---

## 3. Comandos aprendidos

### `wc -l`

Se utiliza para contar el número de líneas de un archivo de registros.

```bash
wc -l logs/ssh-auth.log
```

Resultado de ejemplo:

```text
6 logs/ssh-auth.log
```

### `grep`

Se utiliza para buscar patrones específicos dentro de los registros.

```bash
grep "Failed password" logs/ssh-auth.log
```

Esto permite identificar los intentos de autenticación fallidos y separarlos del resto de los registros.

### `grep -c`

Se utiliza para contar las líneas que coinciden con un patrón de búsqueda.

```bash
grep -c "Failed password" logs/ssh-auth.log
```

Resultado de ejemplo:

```text
5
```

### `awk`

Se utiliza para extraer campos específicos y aplicar condiciones.

Ejemplo:

```bash
awk '{print $11}' logs/ssh-auth.log
```

En el formato de registro SSH simulado utilizado en este ejercicio, el campo `$11` contiene la dirección IP de origen.

Otro ejemplo:

```bash
awk '$3 > "10:01:35"' logs/ssh-auth.log
```

Este comando filtra los eventos que ocurrieron después de una hora específica.

### `sort`

Se utiliza para ordenar los valores extraídos.

```bash
sort
```

También puede combinarse con otros comandos:

```bash
sort | uniq
```

### `uniq`

Se utiliza para eliminar valores repetidos consecutivos.

```bash
sort | uniq
```

Para contar los valores repetidos:

```bash
sort | uniq -c
```

### Tuberías (`|`)

Las tuberías permiten utilizar la salida de un comando como entrada de otro.

Ejemplo:

```bash
grep "Failed password" logs/ssh-auth.log | wc -l
```

Este comando realiza dos acciones:

1. Busca los eventos de autenticación fallidos.
2. Cuenta las líneas obtenidas.

---

## 4. Investigación de registros

El primer registro simulado contenía seis eventos de autenticación SSH.

**Resultados observados:**

| Indicador | Resultado |
|---|---:|
| Eventos totales | 6 |
| Autenticaciones fallidas | 5 |
| Autenticaciones exitosas | 1 |
| Usuario | `admin` |
| Dirección IP de origen | `192.0.2.50` |
| Intervalo de tiempo | 19 segundos |

La secuencia de eventos mostró cinco intentos de autenticación fallidos, seguidos de un inicio de sesión exitoso desde la misma dirección IP de origen.

---

## 5. Investigación de múltiples fuentes

Se analizó un segundo registro simulado para practicar el trabajo con múltiples direcciones IP de origen y cuentas de usuario.

El registro contenía:

- 13 eventos de autenticación en total.
- 11 intentos de autenticación fallidos.
- 2 intentos de autenticación exitosos.
- 4 direcciones IP de origen.
- 3 cuentas de usuario.

**Cantidad de intentos de autenticación fallidos por dirección IP:**

| Dirección IP de origen | Intentos fallidos |
|---|---:|
| `192.0.2.50` | 5 |
| `192.0.2.51` | 3 |
| `192.0.2.52` | 1 |
| `192.0.2.53` | 2 |
| **Total** | **11** |

La dirección IP `192.0.2.50` registró la mayor cantidad de eventos de autenticación fallidos, con cinco intentos.

---

## 6. Detección de patrones

Se creó una condición básica de detección:

```bash
grep "Failed password" logs/multi-source-ssh.log | \
awk '{print $11}' | \
sort | \
uniq -c | \
sort -nr | \
awk '$1 >= 5'
```

El objetivo de este comando fue identificar las direcciones IP de origen que registraron cinco o más intentos de autenticación fallidos.

Resultado de ejemplo:

```text
5 192.0.2.50
```

Este resultado debe considerarse un candidato para detección e investigación adicional, no una prueba de actividad maliciosa.

---

## 7. Metodología de investigación

El ejercicio siguió un flujo de trabajo básico de investigación SOC:

```text
Registros sin procesar
       ↓
Filtrar eventos relevantes
       ↓
Extraer campos
       ↓
Contar y agrupar valores
       ↓
Identificar patrones
       ↓
Aplicar una condición de detección
       ↓
Investigar la evidencia
       ↓
Formular una conclusión prudente
```

Este enfoque reduce la cantidad de información que debe revisarse manualmente y ayuda a concentrar la investigación en los eventos relevantes.

---

## 8. Interpretación de seguridad

La presencia de múltiples intentos de autenticación fallidos desde una misma dirección IP puede representar un patrón potencialmente sospechoso.

Sin embargo, los registros por sí solos no permiten establecer que la actividad haya sido maliciosa.

Algunas explicaciones posibles son:

- Un usuario legítimo que introduce una contraseña incorrecta varias veces.
- Un usuario que ha olvidado parte de su contraseña.
- Una aplicación que utiliza credenciales incorrectas.
- Un administrador que realiza una prueba.
- Un intento de adivinación de contraseñas o un ataque de fuerza bruta.

Se necesitaría evidencia adicional para distinguir entre estas posibilidades.

---

## 9. Limitaciones

Esta investigación presenta varias limitaciones:

- Los registros utilizados son simulados.
- El conjunto de datos es muy pequeño.
- No se disponía de actividad histórica.
- No se analizó telemetría de red.
- No se disponía de actividad de los endpoints.
- No había información sobre la titularidad de las direcciones IP de origen.
- El umbral de cinco intentos de autenticación fallidos se seleccionó con fines de aprendizaje.

Por lo tanto, esta condición de detección no debe considerarse una regla SOC lista para producción.

---

## 10. Habilidades practicadas

- Herramientas de línea de comandos en entornos similares a Unix.
- Análisis de registros de autenticación SSH.
- `grep`.
- `awk`.
- `sort`.
- `uniq`.
- `uniq -c`.
- `wc`.
- `head`.
- `tail`.
- Uso de tuberías.
- Extracción de campos.
- Conteo de eventos.
- Identificación de patrones.
- Lógica básica de detección.
- Análisis de líneas de tiempo.
- Investigación basada en evidencias.

---

## 11. Conclusión

Este ejercicio demostró cómo las herramientas de línea de comandos pueden transformar registros de autenticación sin procesar en información estructurada para el análisis de seguridad.

En lugar de revisar manualmente cada línea, se utilizaron comandos para filtrar eventos, extraer direcciones IP y nombres de usuario, contar valores repetidos, analizar líneas de tiempo e identificar patrones de autenticación potencialmente sospechosos.

La investigación también reforzó un principio importante del trabajo SOC: un patrón sospechoso es un indicador que requiere investigación adicional, no necesariamente la confirmación de un ataque.

El siguiente paso consiste en aplicar estos conceptos a conjuntos de datos más grandes y, posteriormente, reproducir análisis similares mediante tecnologías SIEM.
