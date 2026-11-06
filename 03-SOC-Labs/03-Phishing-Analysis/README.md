# Misión 3 — Análisis de Phishing

[English version](README_EN.md)

## Descripción

Laboratorio práctico de ciberseguridad enfocado en el análisis de correos electrónicos sospechosos, la identificación de indicadores de phishing y la documentación de una investigación siguiendo un enfoque de analista SOC.

El escenario simula un correo electrónico que suplanta a Microsoft Security e intenta presionar al destinatario para que verifique su cuenta mediante un enlace de inicio de sesión.

**Importante:** Todos los datos del escenario son ficticios. Esta actividad tiene fines exclusivamente educativos.

## Objetivos

- Identificar técnicas de ingeniería social.
- Analizar el remitente y los encabezados disponibles del correo.
- Interpretar los resultados de autenticación SPF, DKIM y DMARC.
- Descomponer una URL e identificar su dominio registrable.
- Registrar indicadores técnicos y señales de phishing.
- Evaluar los posibles riesgos de robo de credenciales.
- Documentar hallazgos y recomendaciones de respuesta ante incidentes.

## Estructura del laboratorio

```text
03-Phishing-Analysis/
├── README.md
├── README_EN.md
├── evidence/
│   ├── email-header.txt
│   ├── indicators.txt
│   ├── urls.txt
│   └── analysis-notes.txt
├── investigation.md
├── investigation_EN.md
└── screenshots/
```

## Evidencias

| Archivo | Descripción |
|---|---|
| `email-header.txt` | Encabezados simulados del correo y resultados de autenticación. |
| `indicators.txt` | Indicadores técnicos y señales de phishing identificadas. |
| `urls.txt` | Análisis de la estructura y el dominio de la URL. |
| `analysis-notes.txt` | Notas técnicas, riesgos potenciales y conclusiones preliminares. |
| `investigation.md` | Informe completo de investigación en español. |
| `investigation_EN.md` | Informe completo de investigación en inglés. |

## Hallazgos principales

- Dominio del remitente diferente de `microsoft.com`.
- Lenguaje de urgencia y amenaza de suspensión de cuenta.
- URL con un subdominio que aparenta estar relacionado con Microsoft.
- Dominio registrable identificado como `example.com`.
- Fallos de SPF y DMARC en los datos simulados.
- Posible riesgo de captura de credenciales.

## Herramientas y conceptos

- Análisis manual de correo electrónico.
- Análisis de encabezados de correo.
- Análisis de URL.
- Identificación de IOC (Indicadores de Compromiso).
- SPF, DKIM y DMARC.
- Ingeniería social.
- Investigación y documentación de incidentes.

## Conclusión

El escenario simulado presenta múltiples características compatibles con phishing. Los hallazgos permiten clasificar el correo como sospechoso dentro del entorno del laboratorio, pero no demuestran que haya ocurrido un ataque o compromiso de seguridad real.

## Aviso legal y limitaciones

Este laboratorio utiliza exclusivamente datos simulados. No se abrió ningún enlace sospechoso, no se estableció comunicación con sistemas externos y no se intentó atribuir la actividad a ningún actor de amenazas.