[English version](README_EN.md)

# 03 | SOC LABS — LABORATORIOS SOC

**Laboratorios prácticos de investigación, análisis y detección de amenazas**

## Descripción general

Esta sección reúne laboratorios prácticos orientados al desarrollo de habilidades técnicas y analíticas relacionadas con las operaciones de un Centro de Operaciones de Seguridad (SOC).

El objetivo es aprender a identificar actividades sospechosas, analizar registros de seguridad, investigar posibles amenazas, reconocer indicadores de compromiso (IOC) y comprender los procesos de respuesta ante incidentes.

Cada laboratorio documenta el objetivo, el entorno utilizado, las herramientas, el procedimiento de investigación, las evidencias recopiladas y los resultados obtenidos.

Los ejercicios se desarrollan en entornos controlados y con fines educativos.

---

## Estado de los laboratorios

| Estado | Significado |
|---|---|
| 🟢 **Terminada** | Laboratorio completado y documentado |
| 🔵 **En proceso** | Laboratorio actualmente en desarrollo |
| ⚪ **Planeada** | Laboratorio pendiente de comenzar |

---

## Laboratorios

| Laboratorio | Objetivo | Estado |
|---|---|---|
| [01 - Log Analysis](./01-Log-Analysis/) | Identificar fuentes de registros y analizar eventos de Linux. | 🟢 Terminada |
| [02 - Brute Force Detection](./02-Brute-Force-Detection/) | Investigar intentos de autenticación SSH y detectar patrones de fuerza bruta. | 🟢 Terminada |
| [03 - Phishing Analysis](./03-Phishing-Analysis/) | Analizar correos sospechosos, encabezados, URL e indicadores de phishing. | 🟢 Terminada |
| [04 - Malware Analysis](./04-Malware-Analysis/) | Investigar archivos sospechosos y analizar comportamientos potencialmente maliciosos. | 🟢 Terminada  |
| [05 - Incident Response](./05-Incident-Response/) | Practicar procesos de investigación, contención y respuesta ante incidentes. | 🟢 Terminada  |
| [06 - SIEM Fundamentals](./06-SIEM-Fundamentals/) | Comprender los fundamentos SIEM, el monitoreo y el análisis de eventos de seguridad. | 🔵 En proceso |

---

## Objetivos de aprendizaje

A través de estos laboratorios busco desarrollar las siguientes habilidades:

- **Análisis de registros:** interpretar eventos de autenticación, actividad del sistema y registros de seguridad.
- **Detección de amenazas:** identificar patrones sospechosos y posibles indicadores de compromiso.
- **Investigación de incidentes:** recopilar, analizar y correlacionar evidencias.
- **Análisis de phishing:** reconocer técnicas de ingeniería social y correos fraudulentos.
- **Análisis de malware:** comprender comportamientos sospechosos y posibles mecanismos de ejecución.
- **Monitoreo de seguridad:** conocer el funcionamiento de las plataformas SIEM.
- **Respuesta a incidentes:** comprender las etapas de identificación, análisis, contención y recuperación.
- **Documentación técnica:** elaborar informes estructurados con hallazgos y conclusiones.

---

## Herramientas y tecnologías

Las herramientas utilizadas o contempladas dentro de esta ruta de aprendizaje incluyen:

| Categoría | Herramientas |
|---|---|
| Sistemas operativos | Kali Linux, Linux y Windows |
| Análisis de registros | journalctl, grep, awk |
| Redes | Wireshark |
| Programación | Python, Bash y PowerShell |
| SIEM | Wazuh, Splunk y Elastic Security |
| Detección | Sigma y YARA |
| Inteligencia de amenazas | Fuentes de análisis de IP, dominios, URL y hashes |
| Frameworks | MITRE ATT&CK |
| Documentación | Git y GitHub |

*Cada laboratorio especifica las herramientas que realmente fueron utilizadas.*

---

## Metodología de investigación

Los laboratorios siguen un flujo de trabajo basado en actividades habituales de investigación SOC:

1. **Definición del objetivo:** identificar qué actividad o problema de seguridad se investigará.
2. **Preparación del entorno:** configurar los sistemas y herramientas necesarios.
3. **Recolección de evidencias:** obtener registros, eventos, archivos e indicadores relevantes.
4. **Análisis:** examinar la información e identificar comportamientos sospechosos.
5. **Correlación:** relacionar eventos y evidencias para comprender lo ocurrido.
6. **Clasificación:** determinar los hallazgos y su posible impacto.
7. **Documentación:** registrar procedimientos, evidencias y resultados.
8. **Conclusión:** presentar los resultados y posibles acciones recomendadas.

---

## Estructura de los laboratorios

Cada laboratorio contará, según las necesidades del ejercicio, con una organización similar a la siguiente:

```text
XX-Lab-Name/
│
├── README.md
│
├── evidence/
│   ├── evidence-files.txt
│   └── analysis-results.txt
│
├── investigation.md
│
└── screenshots/
```

**Descripción de los archivos:**

- `README.md`: presenta el laboratorio, sus objetivos y herramientas.
- `evidence/`: almacena los archivos y resultados obtenidos durante la investigación.
- `investigation.md`: documenta el procedimiento, análisis, hallazgos y conclusiones.
- `screenshots/`: contiene capturas de pantalla que respaldan las actividades realizadas.

La estructura puede variar según el tipo de laboratorio.

---

## Resultados y progreso

Este apartado se actualizará conforme se completen nuevos laboratorios, investigaciones y ejercicios prácticos.

El propósito es mantener un registro transparente de mi aprendizaje y demostrar progresivamente mis habilidades en ciberseguridad defensiva y operaciones SOC.

---

## Aviso legal

Todos los ejercicios documentados en esta sección se realizan exclusivamente con fines educativos y en entornos controlados.

Las actividades de simulación, análisis de amenazas y pruebas de seguridad no se realizan sobre sistemas sin autorización.

**Aprender. Investigar. Detectar. Defender.**