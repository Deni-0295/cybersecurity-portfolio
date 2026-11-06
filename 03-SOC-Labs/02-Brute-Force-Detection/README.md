[English version](README_EN.md)

# Detección de Fuerza Bruta SSH

## 1. Objetivo

El objetivo de este laboratorio es analizar eventos de autenticación SSH e identificar patrones potencialmente sospechosos en los intentos de inicio de sesión.

La investigación se enfoca en la dirección IP de origen, la cuenta de usuario involucrada, los resultados de autenticación y el intervalo de tiempo entre los eventos.

El laboratorio también demuestra cómo Python puede utilizarse para automatizar el análisis de logs de seguridad.

---

## 2. Escenario

El log simulado `ssh-auth.log` contiene eventos de autenticación SSH relacionados con el usuario `admin` y la dirección IP de origen `192.0.2.50`.

Los eventos observados fueron:

- 5 intentos de autenticación fallidos.
- 1 intento de autenticación exitoso.
- Todos los eventos se originaron desde la misma dirección IP.
- Los eventos ocurrieron durante un periodo corto de tiempo.
- El primer evento ocurrió a las `10:01:21`.
- El último evento ocurrió a las `10:01:40`.
- El intervalo total fue de 19 segundos.

La autenticación exitosa ocurrió en el sexto intento.

---

## 3. Investigación manual

La investigación inicial identificó un patrón de múltiples intentos fallidos de autenticación SSH, seguidos de una autenticación exitosa desde la misma dirección IP y para la misma cuenta de usuario.

Este patrón puede ser compatible con una actividad de adivinación de contraseñas o un ataque de fuerza bruta. Sin embargo, los datos disponibles no son suficientes para determinar si la actividad fue maliciosa o legítima.

Una posible hipótesis legítima es que el usuario haya introducido una contraseña incorrecta varias veces antes de autenticarse correctamente.

Sería necesario realizar una investigación adicional para determinar la naturaleza de la actividad.

---

## 4. Automatización con Python

El script `analyze_logs.py` automatiza el análisis inicial del log de autenticación SSH.

El script realiza las siguientes operaciones:

1. Localiza el archivo de logs.
2. Lee el log línea por línea.
3. Identifica eventos de autenticación `Failed` y `Accepted`.
4. Extrae el nombre de usuario.
5. Extrae la dirección IP de origen.
6. Cuenta los intentos de autenticación fallidos y exitosos por dirección IP.
7. Calcula el intervalo entre el primer y el último evento.
8. Genera una alerta cuando una dirección IP registra 5 o más intentos fallidos.

---

## 5. Lógica de detección

Para este laboratorio se estableció la siguiente regla:

```text
5 o más intentos de autenticación fallidos
desde la misma dirección IP.
```

Cuando se cumple esta condición, el script genera una alerta para realizar una investigación adicional.

Este umbral se utiliza como ejercicio de aprendizaje y por sí mismo **no confirma que exista un ataque de fuerza bruta**.

---

## 6. Resultados

El análisis automatizado de `ssh-auth.log` identificó:

| Campo | Resultado |
|---|---|
| Servicio | SSH / sshd |
| Usuario | `admin` |
| IP de origen | `192.0.2.50` |
| Intentos fallidos | 5 |
| Intentos exitosos | 1 |
| Primer evento | `10:01:21` |
| Último evento | `10:01:40` |
| Intervalo total | 19 segundos |
| Alerta | 5 intentos fallidos detectados |

### Análisis adicional: múltiples fuentes

El archivo `multi-source-ssh.log` se utilizó para ampliar el análisis a diferentes direcciones IP y usuarios.

Resultados:

- 13 eventos de autenticación.
- 11 intentos fallidos.
- 2 autenticaciones exitosas.
- 4 direcciones IP de origen.
- 3 cuentas de usuario.

La dirección `192.0.2.50` registró el mayor número de intentos fallidos, con 5.

---

## 7. Limitaciones

Este laboratorio utiliza logs simulados de autenticación SSH.

El análisis es intencionalmente sencillo y está diseñado para demostrar los fundamentos del procesamiento de logs y la creación de una lógica básica de detección.

Una investigación real en un SOC requeriría información adicional, por ejemplo:

- Más eventos de autenticación.
- Información del equipo de origen.
- Actividad asociada al usuario.
- Métodos de autenticación utilizados.
- Otros logs del sistema.
- Telemetría de red.
- Historial de actividad de la dirección IP de origen.
- Evidencia adicional para determinar si la actividad fue maliciosa o legítima.

---

## 8. Habilidades desarrolladas

Este laboratorio permitió desarrollar conocimientos prácticos iniciales en:

- Análisis de logs de autenticación SSH.
- Correlación de eventos.
- Identificación de direcciones IP y usuarios.
- Clasificación de eventos de autenticación.
- Análisis básico de líneas de tiempo.
- Procesamiento de logs con Python.
- Expresiones regulares.
- Conteo y filtrado de eventos.
- Creación de lógica básica de detección.
- Documentación de investigaciones de seguridad.

---

## 9. Estructura del laboratorio

```text
02-Brute-Force-Detection/
├── analysis/
│   ├── investigation_EN.md
│   ├── investigation.md
│   └── linux-log-analysis.md
├── logs/
│   ├── multi-source-ssh.log
│   └── ssh-auth.log
├── scripts/
│   └── analyze_logs.py
├── README_.md
└── README_EN.md
```

---

## 10. Conclusión

Este laboratorio demuestra cómo los logs de seguridad pueden analizarse manualmente y posteriormente procesarse de forma automatizada utilizando Python.

El objetivo no es clasificar automáticamente el evento como un ataque, sino identificar un patrón de autenticación potencialmente sospechoso y generar una alerta que pueda ser investigada posteriormente por un analista de seguridad.