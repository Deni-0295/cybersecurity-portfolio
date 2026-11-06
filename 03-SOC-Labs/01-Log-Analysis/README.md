[🇲🇽 Español](README.md) | [🇺🇸 English](README.en.md)
# Análisis de Registros de Linux

## Descripción general

Este laboratorio se centra en el análisis de los registros del sistema Linux de una máquina virtual con Kali Linux.

El objetivo es practicar la identificación de eventos de autenticación, actividades privilegiadas, tareas programadas, actividad SSH y errores del sistema utilizando los mecanismos de registro de Linux y herramientas de línea de comandos.

La investigación sigue un enfoque orientado a un SOC (Centro de Operaciones de Seguridad), mediante la recopilación de evidencias, la clasificación de eventos y la diferenciación entre la actividad normal del sistema y aquellos eventos que podrían requerir una investigación adicional.

---

## Objetivos

- Identificar las fuentes de registros relevantes de Linux.
- Analizar eventos relacionados con la autenticación.
- Investigar la actividad SSH.
- Revisar la actividad privilegiada realizada mediante `sudo`.
- Identificar tareas programadas ejecutadas por CRON.
- Revisar errores del sistema reportados por `systemd` y otros servicios.
- Correlacionar eventos de diferentes fuentes de registros.
- Documentar los hallazgos utilizando evidencias reproducibles.

---

## Entorno

| Elemento | Detalles |
| ------------------ | ------------------ |
| Sistema operativo | Kali Linux |
| Entorno | Máquina virtual |
| Usuario | `kali` |
| Shell | Bash |
| Sistema de registros | Journal de systemd |
| Tipo de investigación | Análisis de registros de Linux |

---

## Herramientas y comandos

Durante la investigación se utilizaron los siguientes comandos de Linux:

```bash
journalctl
grep
awk
sort
uniq
wc
last
ss
ps
systemctl
sudo
```

---

## Áreas de investigación

### 1. Fuentes de registros

Identificación de los archivos y fuentes del journal relevantes disponibles en el sistema.

**Evidencia:**

`evidence/log-sources.txt`

### 2. Eventos SSH

Análisis de la actividad de autenticación relacionada con SSH.

La investigación no encontró registros de `sshd` en el journal durante el período revisado y el servicio SSH se encontraba inactivo.

**Evidencia:**

`evidence/ssh-events.txt`

### 3. Actividad de sudo

Revisión de los comandos privilegiados y las sesiones de sudo generadas durante la investigación.

**Evidencia:**

`evidence/sudo-activity.txt`

### 4. Actividad de CRON

Revisión de las tareas programadas y las sesiones PAM generadas por CRON.

**Evidencia:**

`evidence/cron-activity.txt`

### 5. Errores del sistema

Revisión y clasificación de los errores del sistema operativo y del entorno de escritorio y virtualización.

**Evidencia:**

`evidence/system-errors.txt`

---

## Hallazgos principales

La investigación identificó varios eventos relacionados con la autenticación asociados al entorno gráfico local.

Se observó un fallo de autenticación de LightDM en el que el usuario fue identificado como desconocido y no se registró ningún host remoto.

También se identificó un fallo de autenticación del protector de pantalla de Xfce para la cuenta local `kali`.

No se identificaron eventos de autenticación SSH durante el período revisado.

Se observaron varias sesiones de CRON ejecutándose como `root`, lo cual es consistente con la actividad programada del sistema.

También se identificaron errores del sistema relacionados con componentes de virtualización y del entorno de escritorio.

Estas observaciones se documentaron por separado para evitar clasificar la actividad normal del sistema como actividad maliciosa confirmada.

---

## Estructura de evidencias

```text
evidence/
├── log-sources.txt
├── ssh-events.txt
├── sudo-activity.txt
├── cron-activity.txt
└── system-errors.txt
```

---

## Metodología de investigación

La investigación siguió los siguientes pasos:

1. Identificar las fuentes de registros disponibles.
2. Revisar los eventos relacionados con la autenticación.
3. Buscar específicamente actividad de autenticación SSH.
4. Revisar la actividad privilegiada.
5. Revisar las sesiones programadas de CRON.
6. Identificar los errores del sistema.
7. Correlacionar eventos mediante marcas de tiempo y servicios.
8. Clasificar los eventos según las evidencias disponibles.
9. Documentar los hallazgos y las limitaciones de la investigación.

---

## Resultado

Este laboratorio demuestra el flujo de trabajo básico de un analista SOC al investigar registros de Linux:

**Recopilar → Filtrar → Correlacionar → Clasificar → Documentar**

Las evidencias recopiladas durante este laboratorio pueden utilizarse como base para investigaciones más avanzadas relacionadas con la detección de ataques de fuerza bruta, plataformas SIEM, reglas de detección y respuesta a incidentes.