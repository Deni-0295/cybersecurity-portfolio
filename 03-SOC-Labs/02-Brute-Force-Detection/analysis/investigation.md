# Investigación Manual — Detección de Fuerza Bruta SSH

## 1. Servicio analizado

El servicio involucrado en los eventos es:

```text
SSH / sshd
```

---

## 2. Cuenta de usuario involucrada

La cuenta de usuario observada en los eventos es:

```text
admin
```

---

## 3. Dirección IP de origen

Todos los intentos de autenticación analizados provienen de:

```text
192.0.2.50
```

Esta dirección pertenece a un rango reservado para documentación y ejemplos, por lo que se utiliza únicamente como parte de este laboratorio simulado.

---

## 4. Intentos de autenticación

Se identificaron:

```text
5 intentos fallidos
1 intento exitoso
```

Los cinco intentos fallidos fueron seguidos por una autenticación exitosa.

---

## 5. Secuencia temporal

Los eventos observados fueron:

| Hora | Resultado |
|---|---|
| 10:01:21 | Failed |
| 10:01:24 | Failed |
| 10:01:28 | Failed |
| 10:01:32 | Failed |
| 10:01:36 | Failed |
| 10:01:40 | Accepted |

El primer evento ocurrió a las `10:01:21` y el último a las `10:01:40`.

El intervalo total fue de:

```text
19 segundos
```

Los intervalos entre eventos fueron:

```text
3 segundos
4 segundos
4 segundos
4 segundos
4 segundos
```

---

## 6. Patrón observado

Se identifica el siguiente patrón:

```text
5 intentos fallidos
       ↓
Misma dirección IP
       ↓
Misma cuenta de usuario
       ↓
Periodo corto de tiempo
       ↓
1 autenticación exitosa
```

Este comportamiento representa un patrón que merece investigación debido a la repetición de intentos fallidos y a la posterior autenticación exitosa.

---

## 7. Evaluación inicial

Una posible explicación legítima es que el usuario haya olvidado o introducido incorrectamente su contraseña varias veces hasta conseguir autenticarse correctamente.

Otra posibilidad es que los intentos sean compatibles con una actividad de adivinación de contraseñas o un ataque de fuerza bruta.

Con la información disponible en este log no es posible determinar cuál de estas hipótesis es correcta.

---

## 8. Evidencia disponible

La evidencia utilizada en esta investigación está limitada al archivo:

```text
logs/ssh-auth.log
```

Los principales indicadores observados son:

| Indicador | Valor |
|---|---|
| Servicio | SSH / sshd |
| Usuario | `admin` |
| IP de origen | `192.0.2.50` |
| Intentos fallidos | 5 |
| Intentos exitosos | 1 |
| Primer evento | `10:01:21` |
| Último evento | `10:01:40` |
| Duración observada | 19 segundos |

---

## 9. Información adicional necesaria

Para determinar si la actividad fue legítima o maliciosa sería necesario revisar información adicional, como:

- Otros eventos de autenticación.
- Historial de actividad de la cuenta `admin`.
- Información del sistema afectado.
- Registros adicionales del servidor SSH.
- Actividad de red relacionada con la dirección IP.
- Historial de conexiones desde la misma IP.
- Información sobre el usuario que utiliza la cuenta.
- Eventos posteriores a la autenticación exitosa.
- Posibles cambios realizados en la cuenta después de la autenticación.

---

## 10. Conclusión

El análisis manual identificó cinco intentos fallidos de autenticación SSH seguidos de una autenticación exitosa desde la misma dirección IP y utilizando la misma cuenta de usuario.

El patrón es potencialmente sospechoso y justifica una investigación adicional, pero la evidencia disponible no permite confirmar que se trate de un ataque de fuerza bruta.

La investigación demuestra la importancia de distinguir entre:

```text
Evento observado
       ↓
Patrón identificado
       ↓
Hipótesis
       ↓
Investigación adicional
       ↓
Conclusión basada en evidencia
```

Este enfoque evita asumir que todo comportamiento anómalo constituye automáticamente un incidente de seguridad.