# Linux Log Analysis — Investigación

**Laboratorio:** SOC-Labs / 01-Log-Analysis  
**Plataforma:** Kali Linux  
**Entorno:** Máquina virtual  
**Período de análisis:** Últimos 7 días  
**Fuente principal de registros:** `systemd-journald`

---

# Investigación — Análisis de registros de Linux

## 1. Objetivo

Analizar los registros del sistema Linux para identificar y clasificar:

- Eventos de autenticación.
- Sesiones de usuario.
- Actividad relacionada con privilegios.
- Tareas programadas.
- Errores del sistema.
- Eventos que podrían requerir una investigación adicional.

El objetivo no es considerar automáticamente cualquier evento `failed` o `error` como actividad maliciosa, sino analizar cada evento dentro de su contexto.

---

## 2. Entorno de análisis

**Sistema operativo:** Kali Linux

**Entorno:** Máquina virtual

**Herramienta principal:**

```bash
journalctl
```

El sistema utiliza `systemd-journald` para centralizar diferentes eventos del sistema.

---

## 3. Identificación de eventos de autenticación

Se ejecutó el siguiente comando:

```bash
sudo journalctl --since "7 days ago" --no-pager | grep -Ei "login|logged|session|authentication|pam_unix|lightdm"
```

Posteriormente, se realizó una búsqueda más amplia:

```bash
sudo journalctl --since "7 days ago" --no-pager | grep -Ei "authentication|failed|failure|success|accepted|rejected"
```

Estas consultas permitieron localizar eventos relacionados con autenticación, sesiones y fallos.

---

## 4. Evento de autenticación fallida — LightDM

Se identificó el siguiente evento:

```text
Sep 27 17:59:43 kali lightdm[1128]: pam_unix(lightdm:auth): check pass; user unknown
Sep 27 17:59:43 kali lightdm[1128]: pam_unix(lightdm:auth): authentication failure; logname= uid=0 euid=0 tty=:0 ruser= rhost=
```

### Observación

El evento corresponde al proceso:

```text
lightdm
```

y al módulo PAM:

```text
pam_unix(lightdm:auth)
```

El registro indica:

```text
user unknown
authentication failure
```

Además, el campo:

```text
rhost=
```

no contiene una dirección de origen remota.

### Interpretación

Se produjo un intento de autenticación fallido en el sistema de inicio de sesión gráfico.

El registro no proporciona suficiente información para determinar quién realizó el intento ni permite atribuirlo a un origen remoto.

Por lo tanto, el evento debe clasificarse como:

**Evento de autenticación fallida que requiere contexto adicional.**

No existe evidencia suficiente en este evento aislado para clasificarlo como un ataque.

---

## 5. Sesión gráfica exitosa

Posteriormente, se observaron eventos relacionados con la apertura de