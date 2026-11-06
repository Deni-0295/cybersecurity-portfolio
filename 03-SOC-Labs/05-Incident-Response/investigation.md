# Laboratorio 05 — Incident Response Investigation

### 1. Información del incidente

**Case ID:** SOC-CASE-001
**Severity:** High
**Host inicial:** PC-023
**Usuario:** employee
**Actividad detectada:** Suspicious PowerShell Activity

El incidente comenzó con una alerta relacionada con actividad sospechosa de PowerShell.

El proceso observado fue:

```text
winword.exe → powershell.exe
```

El comando ejecutado fue:

```text
powershell.exe -ExecutionPolicy Bypass -File C:\Users\employee\AppData\Temp\update.ps1
```

---

### 2. Análisis inicial

Se identificaron varios elementos relevantes:

* Microsoft Word inició PowerShell.
* PowerShell utilizó `-ExecutionPolicy Bypass`.
* Se ejecutó el script `update.ps1`.
* El script se encontraba dentro de `AppData\Temp`.
* PowerShell realizó una conexión de red.
* Posteriormente se creó `invoice_update.exe`.

La combinación de estos eventos aumentó significativamente el nivel de sospecha.

---

### 3. Process Tree

La cadena principal observada fue:

```text
winword.exe
    │
    └── powershell.exe
            │
            ├── update.ps1
            │
            ├── Network Connection
            │       └── 198.51.100.25
            │
            └── invoice_update.exe
```

La relación `winword.exe → powershell.exe` fue considerada sospechosa porque un documento de Word normalmente no necesita iniciar PowerShell durante un uso normal.

---

### 4. Timeline

```text
10:13:58  employee opened invoice.docm
10:14:01  winword.exe started
10:14:31  winword.exe spawned powershell.exe
10:14:32  powershell.exe executed update.ps1
10:14:35  powershell.exe connected to 198.51.100.25
10:14:37  powershell.exe created invoice_update.exe
```

---

### 5. Scope Investigation

Durante la investigación se encontraron otros equipos con el mismo documento:

```text
PC-023 → invoice.docm
PC-017 → invoice.docm
PC-041 → invoice.docm
PC-078 → invoice.docm
```

Todos presentaron el mismo hash:

```text
9f86d081884c7d659a2feaa0c55ad015
```

Esto indica que el mismo contenido del archivo estaba presente en varios equipos.

PC-017 y PC-041 también presentaron:

```text
winword.exe → powershell.exe
```

PC-078 tenía el archivo, pero no se observó ejecución de PowerShell.

Por esta razón, PC-078 fue considerado potencialmente expuesto y no directamente comprometido.

---

### 6. Host Prioritization

Los equipos fueron priorizados de acuerdo con la evidencia disponible:

```text
1. PC-023 → HIGH RISK / POTENTIAL COMPROMISE
2. PC-009 → HIGH PRIORITY INVESTIGATION
3. PC-017 → SUSPICIOUS / REQUIRES INVESTIGATION
4. PC-041 → SUSPICIOUS / REQUIRES INVESTIGATION
5. PC-078 → EXPOSED / MONITOR
```

PC-023 presentó la mayor cantidad de evidencia.

PC-009 recibió alta prioridad debido al uso de una cuenta administrativa y a la relación:

```text
chrome.exe → powershell.exe
```

PC-017 y PC-041 presentaron el mismo patrón Word → PowerShell.

PC-078 solamente presentó el archivo sospechoso sin evidencia de ejecución.

---

### 7. Initial Access Hypothesis

La hipótesis principal es que el incidente comenzó mediante un correo de phishing.

El mensaje utilizaba ingeniería social para generar urgencia:

```text
Subject: Urgent Invoice 2026
Attachment: invoice.docm
```

El nombre del archivo podía hacer que el documento pareciera legítimo.

La extensión `.docm` indica que se trata de un documento de Microsoft Word habilitado para macros.

La hipótesis de ataque es:

```text
Phishing Email
      ↓
invoice.docm
      ↓
User opens document
      ↓
winword.exe
      ↓
powershell.exe
      ↓
update.ps1
      ↓
Network Connection
      ↓
invoice_update.exe
```

Esta hipótesis debe ser validada mediante análisis adicional del correo, documento, script y artefactos del sistema.

---

### 8. Incident Response

Las acciones de respuesta propuestas fueron:

#### Containment

* Aislar PC-023, PC-017 y PC-041 de la red.
* Evitar comunicaciones adicionales con infraestructura sospechosa.
* Reducir el riesgo de propagación o movimiento lateral.

#### Evidence Preservation

Preservar:

* `invoice.docm`
* `update.ps1`
* `invoice_update.exe`
* PowerShell logs
* Process creation logs
* Network logs
* Email headers
* Original phishing email

No se recomienda eliminar inmediatamente los archivos antes de preservar la evidencia.

#### Threat Hunting

Buscar en el entorno:

```text
SHA-256:
9f86d081884c7d659a2feaa0c55ad015

IP:
198.51.100.25

Files:
invoice.docm
update.ps1
invoice_update.exe
```

También buscar la relación:

```text
winword.exe → powershell.exe
```

#### Eradication

Después de preservar y analizar la evidencia:

* Poner en cuarentena los archivos maliciosos.
* Eliminar artefactos confirmados.
* Revisar mecanismos de persistencia.
* Validar que no existan componentes adicionales.

#### Recovery

* Restaurar los equipos a un estado confiable.
* Validar los sistemas antes de reconectarlos.
* Mantener monitoreo posterior al incidente.

---

### 9. Incident Assessment

El incidente presenta características compatibles con un posible ataque de phishing seguido de ejecución de PowerShell.

Los principales factores de riesgo fueron:

* Documento `.docm`.
* Distribución a múltiples usuarios.
* Mismo hash en varios equipos.
* `winword.exe → powershell.exe`.
* `ExecutionPolicy Bypass`.
* Script ejecutado desde `AppData\Temp`.
* Conexión de red.
* Creación de un ejecutable.

La evidencia disponible permite establecer una **alta sospecha de compromiso en PC-023** y requiere investigación adicional en PC-017 y PC-041.

PC-078 se considera potencialmente expuesto, pero no comprometido con la evidencia actualmente disponible.
