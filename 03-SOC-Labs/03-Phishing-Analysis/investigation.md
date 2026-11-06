# SOC-CASE-003 — Análisis de Phishing

**Laboratorio:** 3 — Análisis de Phishing  
**Analista:** Laboratorio de Portafolio de Ciberseguridad  
**Estado:** Investigación documentada  
**Entorno:** Escenario simulado  
**Clasificación:** Sospecha de phishing  
**Fecha:** 3 de noviembre de 2026

---

## 1. Resumen ejecutivo

Se analizó un correo electrónico simulado que aparenta proceder de Microsoft Security. El mensaje advierte que la cuenta de Microsoft 365 del destinatario será suspendida en un plazo de 24 horas si no verifica su identidad.

El correo contiene un dominio de remitente sospechoso, lenguaje de urgencia y una URL que utiliza términos relacionados con Microsoft, aunque su dominio registrable es `example.com`.

Los resultados de autenticación proporcionados indican un fallo de SPF, ausencia de una firma DKIM reportada y un fallo de DMARC.

**Conclusión preliminar:** El correo presenta múltiples indicadores compatibles con phishing. Esta investigación se basa exclusivamente en datos simulados y no demuestra que haya ocurrido un compromiso real de seguridad.

## 2. Objetivos

- Identificar indicadores de phishing en el contenido del correo.
- Analizar el remitente y los encabezados disponibles.
- Descomponer la URL e identificar su dominio registrable.
- Registrar indicadores técnicos relevantes.
- Evaluar los posibles riesgos para el usuario.
- Documentar recomendaciones de respuesta ante un posible incidente.

## 3. Evidencia analizada

| Evidencia | Hallazgo |
|---|---|
| Remitente | `security@microsoft-support-alert.com` |
| Asunto | Advertencia urgente de suspensión de cuenta |
| URL | `https://microsoft-security-verification.example.com/login` |
| Dominio registrable | `example.com` |
| SPF | `fail` |
| DKIM | `none` |
| DMARC | `fail` |
| IP del encabezado | `203.0.113.25` |

La dirección IP pertenece a un rango reservado para documentación y ejemplos. No representa una dirección de un atacante verificado.

## 4. Análisis del correo electrónico

### 4.1 Análisis del remitente

La dirección visible del remitente utiliza el dominio `microsoft-support-alert.com`, que no coincide con el dominio oficial de Microsoft: `microsoft.com`.

El nombre del remitente y el dominio podrían estar diseñados para generar confianza en el destinatario.

### 4.2 Ingeniería social

El mensaje utiliza dos técnicas de presión:

- **Urgencia:** Se indica al destinatario que debe actuar en un plazo de 24 horas.
- **Amenaza:** Se advierte que la cuenta será suspendida.

Estas técnicas pueden presionar al destinatario para que actúe sin verificar la autenticidad del mensaje.

### 4.3 Análisis de la URL

**URL identificada:**

`https://microsoft-security-verification.example.com/login`

- **Protocolo:** HTTPS.
- **Subdominio:** `microsoft-security-verification`.
- **Dominio registrable:** `example.com`.
- **Ruta:** `/login`.

El subdominio utiliza términos relacionados con Microsoft, pero el dominio registrable no es `microsoft.com`.

HTTPS protege la comunicación durante el tránsito de los datos, pero no garantiza que un sitio web sea legítimo.

La ruta `/login` sugiere que el usuario podría ser dirigido a una página de inicio de sesión.

### 4.4 Análisis de encabezados y autenticación

Los resultados simulados indican:

- **SPF: fail.** La comprobación SPF no fue superada.
- **DKIM: none.** No se reporta una firma DKIM en los resultados proporcionados.
- **DMARC: fail.** La evaluación DMARC no fue superada.
- **Return-Path:** Utiliza un dominio diferente al del remitente visible.

La diferencia entre los campos `From` y `Return-Path` requiere contexto adicional y no demuestra por sí sola que exista phishing.

## 5. Indicadores registrados

- Dirección de remitente sospechosa.
- Dominio del remitente diferente de `microsoft.com`.
- URL diseñada para aparentar ser un servicio de seguridad de Microsoft.
- Dominio registrable `example.com`.
- Lenguaje de urgencia y amenaza de suspensión de cuenta.
- Fallos de SPF y DMARC en los datos simulados.

Estos hallazgos deben evaluarse en conjunto. No se ha confirmado una campaña de phishing real ni una víctima comprometida.

## 6. Evaluación de riesgos

Si un correo similar apareciera en un entorno real, los riesgos potenciales podrían incluir:

- Robo de credenciales.
- Acceso no autorizado a una cuenta.
- Uso de una cuenta comprometida para enviar nuevos mensajes de phishing.
- Acceso a recursos de una organización, dependiendo de los permisos de la cuenta.

No existe evidencia en este laboratorio de que alguno de estos impactos haya ocurrido realmente.

## 7. Recomendaciones de respuesta

1. No abrir el enlace ni introducir credenciales.
2. Verificar el mensaje mediante un canal oficial e independiente.
3. Reportar el correo al equipo de seguridad.
4. En un caso real, conservar el mensaje original y sus encabezados completos.
5. Si un usuario hubiera proporcionado sus credenciales, seguir el procedimiento de respuesta a incidentes: cambiar las credenciales mediante un canal legítimo, revocar las sesiones activas cuando corresponda y revisar los registros de autenticación.
6. En un entorno real, validar los indicadores mediante herramientas y fuentes autorizadas antes de bloquear dominios o direcciones IP.

## 8. Limitaciones

El escenario, el correo electrónico y los encabezados son simulados. La URL no fue visitada y no se estableció comunicación con sistemas externos.

La reputación de los dominios no fue verificada de manera independiente y no se intentó atribuir la actividad a ningún actor de amenazas.

## 9. Conclusión

El correo electrónico simulado presenta múltiples características compatibles con phishing, entre ellas la aparente suplantación de una marca, el uso de urgencia, una amenaza de suspensión de cuenta, una URL sospechosa y resultados de autenticación fallidos.

La evidencia disponible permite clasificar el mensaje como **sospechoso dentro del entorno del laboratorio**.

Una investigación real requeriría validar la información y correlacionarla con fuentes adicionales antes de establecer una conclusión definitiva.