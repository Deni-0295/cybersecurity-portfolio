# 🔎 03 · SOC Labs

Laboratorios prácticos que simulan el trabajo diario de un **Analista SOC Junior (Nivel 1)**: revisar alertas, analizar logs, detectar ataques, investigar correos sospechosos, estudiar malware, documentar hallazgos y apoyar la respuesta a incidentes.

![Rol](https://img.shields.io/badge/rol-Analista%20SOC%20Junior-a78bfa?style=for-the-badge)
![Enfoque](https://img.shields.io/badge/enfoque-Blue%20Team-22d3ee?style=for-the-badge)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-ef4444?style=for-the-badge)

⬅️ [Volver al portafolio](../README.md)

---

## 📂 Laboratorios

| # | Carpeta | De qué trata | Estado |
|---|---|---|---|
| 01 | [`01-Log-Analysis`](./03-SOC-Labs/01-Log-Analysis) | Lectura, filtrado y correlación de logs para encontrar actividad sospechosa | 🛠️ En progreso |
| 02 | [`02-Brute-Force-Detection`](./03-SOC-Labs/02-Brute-Force-Detection) | Detección de intentos de fuerza bruta a partir de múltiples fallos de autenticación | 🛠️ En progreso |
| 03 | [`03-Phishing-Analysis`](./03-SOC-Labs/03-Phishing-Analysis) | Análisis de correos de phishing: encabezados, enlaces, adjuntos e indicadores de compromiso (IoC) | 🛠️ En progreso |
| 04 | [`04-Malware-Analysis`](./03-SOC-Labs/04-Malware-Analysis) | Análisis básico (estático y de comportamiento) de muestras en un entorno aislado | 🛠️ En progreso |
| 05 | [`05-Incident-Response`](./03-SOC-Labs/05-Incident-Response) | Respuesta a incidentes: identificación, contención, erradicación, recuperación y lecciones aprendidas | 🛠️ En progreso |

---

## 🗺️ Relación con MITRE ATT&CK

| Laboratorio | Técnica de referencia |
|---|---|
| Brute Force Detection | [T1110 · Brute Force](https://attack.mitre.org/techniques/T1110/) |
| Phishing Analysis | [T1566 · Phishing](https://attack.mitre.org/techniques/T1566/) |
| Malware Analysis | [TA0002 · Execution](https://attack.mitre.org/tactics/TA0002/) |
| Incident Response | Ciclo de vida de respuesta a incidentes (NIST SP 800-61) |

---

## 🔄 Flujo de trabajo en un SOC

```text
Logs  →  Detección  →  Triage  →  Análisis  →  Respuesta  →  Documentación
(01)      (02)         (03)       (04)         (05)          (en cada lab)
```

---

## 🧰 Habilidades que practico

- Análisis y correlación de logs
- Detección de patrones de ataque y creación de alertas
- Investigación de correos y extracción de IoC
- Análisis estático y de comportamiento de malware
- Documentación de incidentes y recomendaciones de mitigación

---

## 🧪 Estructura de cada laboratorio

```text
NN-Nombre-del-Lab/
├── README.md       # Objetivo, escenario, herramientas y conclusiones
├── evidencias/     # Capturas de pantalla y logs de ejemplo
├── analisis.md     # Hallazgos paso a paso
└── reporte.md      # Resumen tipo reporte de incidente
```

Plantilla del reporte:

1. **Resumen**: qué pasó, en pocas líneas
2. **Cronología**: eventos en orden
3. **Indicadores de compromiso (IoC)**: IP, dominios, hashes
4. **Técnicas MITRE ATT&CK** observadas
5. **Impacto y severidad**
6. **Acciones recomendadas**

---

> ⚠️ Todos los ejercicios usan datos de ejemplo, plataformas de entrenamiento o máquinas virtuales aisladas. Nunca se analiza malware ni se prueban ataques fuera de entornos controlados.
