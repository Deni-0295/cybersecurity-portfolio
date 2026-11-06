[English version](README_EN.md)

# Laboratorio 05 — Respuesta a Incidentes

## Descripción

En este Laboratorio se realizó una investigación simulada de un incidente de seguridad relacionado con actividad sospechosa de PowerShell.

El incidente comenzó con una alerta en el equipo `PC-023`, donde se observó una relación sospechosa entre Microsoft Word y PowerShell:

```text
winword.exe → powershell.exe
```

La investigación posterior reveló la ejecución de scripts, comunicación de red y creación de un archivo ejecutable.

También se identificó el mismo documento sospechoso en varios equipos, lo que llevó a ampliar el alcance de la investigación.

---

## Objetivos

- Analizar una alerta de seguridad.
- Investigar relaciones entre procesos.
- Construir una línea de tiempo del incidente.
- Identificar indicadores de compromiso (IOC).
- Determinar el alcance de un incidente.
- Priorizar los equipos afectados.
- Formular una hipótesis sobre el vector de acceso inicial.
- Aplicar medidas de contención.
- Preservar evidencias.
- Realizar actividades de Threat Hunting.
- Diferenciar entre exposición y compromiso confirmado.

---

## Resumen de la alerta

| Campo | Valor |
|---|---|
| ID del caso | SOC-CASE-001 |
| Severidad | Alta |
| Equipo inicial | PC-023 |
| Usuario | employee |
| Proceso | powershell.exe |
| Proceso padre | winword.exe |
| Script | update.ps1 |
| IP de red | 198.51.100.25 |
| Archivo creado | invoice_update.exe |

---

## Cadena principal de procesos

```text
Correo de phishing
        ↓
invoice.docm
        ↓
winword.exe
        ↓
powershell.exe
        ↓
update.ps1
        ↓
Conexión de red
        ↓
invoice_update.exe
```

---

## Hallazgos principales

### PC-023

La evidencia más significativa se observó en el equipo `PC-023`.

Actividades identificadas:

- `winword.exe → powershell.exe`
- `ExecutionPolicy Bypass`
- Ejecución de `update.ps1`
- Conexión de red a `198.51.100.25`
- Creación de `invoice_update.exe`

**Evaluación:** Riesgo alto / posible compromiso.

### PC-017

Se observó la siguiente relación entre procesos:

```text
winword.exe → powershell.exe
```

También se identificaron el mismo archivo sospechoso `invoice.docm` y su hash.

**Evaluación:** Actividad sospechosa / requiere investigación adicional.

### PC-041

Se observó la siguiente relación entre procesos:

```text
winword.exe → powershell.exe
```

También se identificaron el mismo archivo sospechoso `invoice.docm` y su hash.

**Evaluación:** Actividad sospechosa / requiere investigación adicional.

### PC-078

El archivo sospechoso `invoice.docm` estaba presente en el equipo, pero no se detectó actividad de PowerShell.

**Evaluación:** Posible exposición / requiere monitoreo.

---

## Indicadores de compromiso (IOC)

```text
Archivo:
invoice.docm

Hash proporcionado:
9f86d081884c7d659a2feaa0c55ad015

Script de PowerShell:
update.ps1

Ejecutable creado:
invoice_update.exe

Dirección IP:
198.51.100.25

Relación entre procesos:
winword.exe → powershell.exe
```

---

## Hipótesis de acceso inicial

La hipótesis principal es que el incidente se originó a través de un correo electrónico de phishing que contenía el archivo `invoice.docm`.

Es posible que el correo utilizara técnicas de ingeniería social y mensajes de urgencia para convencer a los usuarios de abrir el documento.

```text
Phishing
    ↓
Ingeniería social
    ↓
invoice.docm
    ↓
Microsoft Word
    ↓
PowerShell
    ↓
Payload (carga útil)
```

El mismo hash del documento fue identificado en varios sistemas, lo que sugiere que el archivo pudo haberse distribuido a diferentes usuarios.

---

## Respuesta al incidente

Las principales acciones de respuesta consideradas durante la investigación fueron:

1. **Contención**
   - Aislar de la red los equipos sospechosos.

2. **Preservación de evidencias**
   - Conservar archivos sospechosos, registros, información del correo electrónico y evidencias de red.

3. **Threat Hunting**
   - Buscar en el entorno hashes, nombres de archivos, direcciones IP y relaciones entre procesos previamente identificados.

4. **Contención del correo electrónico**
   - Identificar y eliminar el correo de phishing de los buzones afectados.

5. **Erradicación**
   - Poner en cuarentena y eliminar los artefactos maliciosos confirmados después de preservar las evidencias necesarias.

6. **Recuperación**
   - Restaurar los sistemas a un estado confiable y monitorearlos después de su recuperación.

7. **Monitoreo posterior al incidente**
   - Restaurar los sistemas a un estado confiable y monitorearlos después de su recuperación.

---

## Evidencias

```text
evidence/
├── alert.txt
├── timeline.txt
├── process-tree.txt
├── indicators.txt
├── affected-hosts.txt
└── response-actions.txt
```

Investigación detallada:

```text
investigation.md
```

---

## Habilidades practicadas

- Respuesta a incidentes (Incident Response)
- Clasificación y análisis de alertas (Alert Triage)
- Análisis de árboles de procesos (Process Tree Analysis)
- Investigación de PowerShell
- Identificación de indicadores de compromiso (IOC)
- Búsqueda de amenazas (Threat Hunting)
- Reconstrucción de líneas de tiempo
- Determinación del alcance de incidentes
- Priorización de equipos
- Contención
- Preservación de evidencias
- Investigación de phishing
- Análisis de ingeniería social

---

## Resumen de la investigación

La investigación identificó un posible ataque basado en phishing que involucraba un documento de Microsoft Word habilitado para macros.

La cadena de ejecución sospechosa fue:

```text
Correo de phishing
        ↓
invoice.docm
        ↓
winword.exe
        ↓
powershell.exe
        ↓
update.ps1
        ↓
Conexión de red
        ↓
invoice_update.exe
```

La evidencia más significativa se encontró en `PC-023`, mientras que `PC-017` y `PC-041` requirieron una investigación adicional.

`PC-078` se consideró potencialmente expuesto debido a la presencia del archivo sospechoso, aunque no se detectó su ejecución.


**Aprender. Investigar. Contener. Recuperar. Defender.**

Copyright (c) 2026 Irma (Deni-0295). Todos los derechos reservados.

Este repositorio y su contenido (reportes, documentos, imágenes y textos)
son propiedad de la autora. No se permite copiar, modificar, distribuir
ni utilizar este material, total o parcialmente, sin autorización
previa y por escrito.