# DOSSIER TÉCNICO-FUNCIONAL Y RESEÑA OPERATIVA DEL SISTEMA (VERSIÓN 2.0 AUDITADA)
## Documento Descriptivo de Arquitectura, Flujos, Invariantes y Controles Forenses
**Iniciativa:** Ecosistema Híbrido "Patrimonio Inteligente"  
**Titular y Autora Responsable:** Hilda Belem Ortiz Fuentes  
**Fecha de Emisión Oficial:** 25 de Noviembre de 2026 (Revisión v2.0 Subsanada)  
**Marco Normativo de Referencia:** LMV (Arts. 225 y 227 Bis 1), Ley Fintech (Arts. 2 y 11), LFPC (Art. 32), LFPDPPP, LFPPI (Arts. 163–169)  
**Destinatario:** Cuerpo Colegiado de Auditores Externos (Tecnología, Cumplimiento, Finanzas y Ciberseguridad)

---

## 1. PROPÓSITO DEL DOCUMENTO Y SUBSANACIONES FORENSES
El presente documento actualiza y eleva al estándar forense más exigente la descripción técnica, funcional y operativa de **Patrimonio Inteligente**, atendiendo puntualmente los dictámenes de auditoría externa.

Este dossier proporciona a los auditores una comprensión exhaustiva y rigurosa de las entradas, procesos, invariantes contables, salvaguardas de no-custodia y protocolos de continuidad de negocio, **sin divulgar código ejecutable propietario ni secretos industriales protegidos por la Ley Federal de Protección a la Propiedad Industrial (LFPPI)**.

---

## 2. DELIMITACIÓN JURÍDICA Y MARCO REGULATORIO MEXICANO (NO-CUSTODIA)

### 2.1. Cero Captación de Pasivos y Régimen de No-Custodia
La arquitectura técnica excluye por diseño la recepción, administración, depósito o custodia de moneda de curso legal o activos virtuales de terceros:
- **Ley Fintech (Arts. 2 y 11):** La plataforma no opera como Institución de Fondos de Pago Electrónico (IFPE) ni Institución de Financiamiento Colectivo (IFC).
- **Ley de Instituciones de Crédito (Art. 103 LIC):** No realiza captación bancaria de recursos del público.
- **Custodia Exclusiva en Intermediarios Regulados:** Los fondos monetarios y activos permanecen en cuentas individuales contratadas directamente por el usuario:
  * **Activos Virtuales:** Custodia individual en cuentas personales dentro del exchange regulado **Bitso México**.
  * **Valores Bursátiles y FIBRAs:** Custodia individual en cuentas de la casa de bolsa **Bursanet (Actinver)**, regulada por la Comisión Nacional Bancaria y de Valores (CNBV).

### 2.2. Fundamentación Conforme a la Ley del Mercado de Valores (Arts. 225 y 227 Bis 1)
En estricta subsanación de referencias previas, la actividad del copiloto se delimita formalmente conforme al marco bursátil vigente:
- **Artículo 225 de la LMV:** El sistema **no presta servicios de Asesoría en Inversiones profesional individualizada ni discrecional**. No determina perfiles de inversión privados, no emite recomendaciones forzosas ni dispone de carteras ajenas. Su función es la provisión de software de análisis técnico cuantitativo, seguimiento de cotizaciones públicas y educación financiera basada en reglas matemáticas objetivas, al amparo de las libertades de expresión y difusión consagradas en los **Artículos 6º y 7º Constitucionales**.
- **Artículo 227 Bis 1 de la LMV (Servicios Automatizados / Algorítmicos):** Se hace constar que los algoritmos operan como modelos cuantitativos fijos no discrecionales; toda orden de compra o venta en Bitso o Bursanet requiere **la decisión, parametrización y ejecución manual indispensable del usuario**.

---

## 3. ARQUITECTURA DEL FRONTEND WEB (EXPERIENCIA PÚBLICA AUDITABLE)
La plataforma web (`ariaeden.github.io/patrimonio-web` y `patrimonio-inteligente`) actúa como un entorno educativo estático del lado del cliente (*Client-Side Rendering*):

### 3.1. Aislamiento de Privacidad y Cero Telemetría
- No se implementan cookies analíticas de terceros, balizas (*pixels*), ni extracción de direcciones IP. Toda simulación se procesa localmente en la memoria del navegador.
- Interfaz moderna con 4 menús desplegables Glassmorphism (*Primeros Pasos*, *Estrategia & Herramientas*, *Educación & Guías*, *Legal & Recursos*), adaptabilidad móvil con *Drawer* y pie de página con titularidad formal atribuida a **Hilda Belem Ortiz Fuentes**.

### 3.2. Modelo Matemático de Interés Compuesto Geométrico
- **Tasa Geométrica Efectiva Mensual:** Aplica la conversión exacta $r_m = (1 + r_a)^{1/12} - 1$ para evitar el sesgo de sobreestimación del método aritmético lineal ($r_a / 12$).
- **Matriz de Estrés Cuantitativo:** Modela cuatro escenarios deterministas que incluyen inflación, depreciación de divisa y escenarios adversos severos con rendimientos reales netos negativos.
- **Deslinde LFPC (Art. 32):** Se eliminaron expresiones absolutas ("cero trampas", "garantías"); los resultados se declaran expresamente como simulaciones didácticas de largo plazo no garantizadas.

---

## 4. ARQUITECTURA DEL COPILOTO EN LA NUBE Y REGLAS DE TRADING

### 4.1. Separación de Máquinas de Estados: DCA vs Recompra Táctica (Gatekeeper)
Atendiendo la observación técnica de Ai-1, el copiloto desacopla dos lógicas operativas independientes:

```
[MÁQUINA 1: ACUMULACIÓN PROGRAMADA DCA]
   ├── Regla: Compras periódicas según calendario del usuario.
   ├── Condición de Mercado: RSI 4H < 65.0 (Mercado no sobrecalentado).
   └── Costo Promedio: Métrica meramente informativa, no bloquea el ahorro disciplinado.

[MÁQUINA 2: RECOMPRA TÁCTICA TRAS VENTA (GATEKEEPER)]
   ├── Estado del Usuario: EN_LIQUIDEZ (tras venta previa de toma de ganancias).
   ├── Condición de Recompra: Retroceso de mercado >= -2.5% vs precio de salida.
   └── Objetivo: Condicionar la entrada a un precio con descuento para optimizar unidades netas.
```

**Deslinde de Rendimiento:** Se suprime categóricamente la expresión "satoshis gratuitos garantizados". Se documenta con rigor que la ganancia de unidades es **condicional a que el mercado efectivamente retroceda al target, que las órdenes límites Maker se ejecuten al 100% y descontando las comisiones de exchange**.

### 4.2. Ingesta de Tipos de Cambio y Datos en Vivo
El sistema distingue con precisión técnica dos fuentes de datos:
1. **Cotizaciones Spot de Exchange en Tiempo Real:** Precios de ejecución viva en Bitso para pares `btc_usd` y `btc_mxn`, reflejando la liquidez y el spread directo del libro de órdenes.
2. **Tipo de Cambio de Referencia Oficial:** Tipo de cambio FIX / interbancario de Banco de México (DOF) utilizado exclusivamente para valuaciones de referencia contable y comparativas didácticas, documentando que no constituye un precio negociable de ejecución inmediata en fines de semana.

---

## 5. MODELO CONTABLE DE PARTIDA DOBLE Y CERTIFICACIÓN FORENSE
*(Subsanación integral del contraejemplo contable de Ai-1)*

### 5.1. Ecuaciones de Conservación y Balance Patrimonial Completo
Para resolver la debilidad de omitir el efectivo disponible y el PnL realizado al vender posiciones de Bitcoin, el sistema implementa un modelo contable de partida doble:

$$\text{Patrimonio Total Estimado} = \text{Efectivo Disponible (Fiat Cash)} + \left( \frac{\text{Satoshis Acumulados} \times P_{\text{spot}}}{10^8} \right)$$

$$\text{Resultado Neto Histórico} = \text{Patrimonio Total Estimado} - \text{Capital Real Aportado de Bolsillo}$$

Donde se rastrean formalmente cuatro magnitudes independientes:
- **`total_fiat_deposited_usd` / `total_fiat_deposited_mxn`:** Capital externo neto inyectado de bolsillo por el usuario (depósitos bancarios acumulados).
- **`total_satoshis` (y `total_btc`):** Unidades de Bitcoin en cartera no vendidas.
- **`fiat_cash_balance_usd` / `fiat_cash_balance_mxn`:** Efectivo líquido en cuenta disponible tras ventas de toma de ganancias o fondeo pendiente de ejecutar.
- **`realized_pnl_usd` / `realized_pnl_mxn`:** Utilidad o pérdida neta materializada por órdenes de venta concluidas sobre el costo promedio de adquisición.

*Resolución del Contraejemplo:* Si un usuario aporta $10,000 MXN y vende todo a $12,000 MXN, su balance de satoshis pasa a `0`, pero su `fiat_cash_balance` registra `$12,000 MXN`, su capital aportado registra `$10,000 MXN` y su `realized_pnl` acredita una ganancia realizada de `+$2,000 MXN (+20.0%)`, reflejando con exactitud su patrimonio total sin pérdidas de información.

### 5.2. Verificación de Integridad de Comprobantes con Huella SHA-256
- La huella SHA-256 generada a partir de los atributos invariantes de la orden en Bitso (precio, monto BTC, moneda, fecha/hora y total) opera como un **control estricto de idempotencia y antiduplicación lógica**. Si una captura se reenvía, el hash colisiona y se rechaza.
- Se documenta que el hash garantiza la unicidad del registro en el libro contable auxiliar, sin sustituir los estados de cuenta oficiales emitidos por Bitso México.

---

## 6. PRIVACIDAD DE DATOS, ARCO Y CRYPTO-SHREDDING EN EL WAL (LFPDPPP)

### 6.1. Conciliación entre Bitácora Inmutable (WAL) y Derecho de Cancelación
Para subsanar la tensión técnica entre un log *append-only* encadenado y el derecho a la eliminación definitiva de datos personales:
- **Mecanismo de Crypto-Shredding:** Al invocar `/borrar_datos confirmar`, el sistema **no rompe la cadena criptográfica SHA-256**. En su lugar, ejecuta una rutina de anonimización irreversible donde el `chat_id` y nombre del usuario se sustituyen en el histórico por un token disociado (`ANONYMIZED_USER_<salt_hash>`), y se anexa un evento formal de cancelación con folio legal ARCO.
- **Purga de Base Activa:** El usuario se suprime de inmediato de `registered_users.json` y de los estados de memoria en caliente.
- **Cumplimiento:** Satisface plenamente el Artículo 16 de la LFPDPPP y el periodo de bloqueo de conservación disociada contemplado en el Artículo 24 de la misma ley.

---

## 7. GOBERNANZA, RESILIENCIA Y PLAN DE CONTINUIDAD (DISASTER RECOVERY)

### 7.1. Persistencia Real en Render Cloud y Almacenamiento Efímero
Reconociendo la naturaleza efímera de los contenedores estándar de Render:
- El sistema implementa la escritura atómica (`.tmp` + `fsync()` + `os.replace()`) y snapshots locales como primera barrera contra fallos de proceso.
- Para neutralizar la pérdida de datos ante reinicios o recreaciones de contenedor en Render, la plataforma cuenta con un canal de replicación externa automática.

### 7.2. Bóveda Soberana de Rescate Cifrada (ZIP con Contraseña)
En cumplimiento de las observaciones de ciberseguridad sobre el envío de datos en texto plano:
- El comando `/respaldo` genera un contenedor comprimido **ZIP protegido criptográficamente con contraseña** (`boveda_rescate_cifrada_*.zip`).
- Los archivos sensibles (directorio de usuarios CSV con contactos y balances, base JSON y libro contable) viajan cifrados, impidiendo que terceros puedan acceder al padrón aun en caso de compromiso de sesión en Telegram.
- **Objetivos de Continuidad Operativa (Métricas RPO/RTO):**
  * **RPO (Punto Objetivo de Recuperación):** $\le 15$ minutos (mediante snapshots y bitácora transaccional WAL).
  * **RTO (Tiempo Objetivo de Recuperación):** $\le 60$ minutos (reconstrucción determinista en servidor alternativo a partir del paquete de rescate cifrado). Se eliminan afirmaciones comerciales no medidas como "recuperación en 10 segundos".

---

## 8. MATRIZ DE CONFORMIDAD FORENSE INTEGRAL (CHECKLIST FINAL)

| Criterio Forense | Evaluación Ai-1 / Ai-2 | Subsanación Técnica Implementada |
| :--- | :---: | :--- |
| **Fundamentación Bursátil** | Observación Crítica (P0) | Corrección a **Artículos 225 y 227 Bis 1 de la LMV** (software no discrecional). |
| **Integridad Contable** | Debilidad Matemática (P0) | **Partida Doble:** Incorporación de `fiat_cash_balance` y `realized_pnl` en el libro mayor. |
| **Seguridad de Respaldos** | Riesgo de Privacidad (P0) | **Cifrado ZIP con Contraseña:** Empaquetado protegido de directorio CSV y bases JSON. |
| **Persistencia en Nube** | Almacenamiento Efímero (P0) | Documentación de RPO/RTO y replicación externa fuera del contenedor efímero. |
| **Privacidad vs WAL** | Tensión Legal (P1) | **Crypto-Shredding:** Anonimización irreversible en WAL sin fracturar la cadena SHA-256. |
| **Lenguaje y Deslindes** | Promesas Excesivas (P1) | Erradicación de términos absolutos ("garantías", "satoshis gratis") conforme a LFPC Art. 32. |
| **Lógica Gatekeeper** | Conflicto con DCA (P1) | Desacoplamiento de máquinas de estado: DCA programado independiente de recompra táctica. |

---

## 9. DECLARACIÓN DE TITULARIDAD Y AUTORÍA
Se ratifica formalmente que la totalidad del diseño metodológico, arquitectura de resiliencia y documentación técnica pertenecen con carácter exclusivo a **Hilda Belem Ortiz Fuentes**, con derechos morales y patrimoniales reservados ante el **INDAUTOR** y bajo la **Ley Federal de Protección a la Propiedad Industrial**.

**Hilda Belem Ortiz Fuentes**  
Titular y Desarrolladora de Patrimonio Inteligente  
Ciudad de México, Noviembre de 2026.
