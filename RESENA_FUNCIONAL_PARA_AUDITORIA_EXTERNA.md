# DOSSIER TÉCNICO-FUNCIONAL Y RESEÑA OPERATIVA DEL SISTEMA
## Documento Descriptivo de Arquitectura, Flujos y Controles para Auditoría Externa
**Iniciativa:** Ecosistema Híbrido "Patrimonio Inteligente"  
**Titular y Autora Responsable:** Hilda Belem Ortiz Fuentes  
**Fecha de Emisión:** 25 de Noviembre de 2026  
**Clasificación:** Documento Institucional de Auditoría de Sistemas y Cumplimiento  
**Régimen Jurídico:** Secreto Industrial (LFPPI Arts. 163–169) y Reserva de Derechos (LFDA)

---

## 1. PROPÓSITO DEL DOCUMENTO Y ALCANCE DE AUDITORÍA
El presente documento ha sido elaborado a solicitud de la titular para proporcionar al equipo de **auditores externos** una comprensión exhaustiva, transparente y estructurada del funcionamiento operativo, flujos de datos, modelos matemáticos y mecanismos de control de la plataforma **Patrimonio Inteligente**.

Dado que el código fuente, los modelos algorítmicos específicos y los pesos ponderados constituyen **Secretos Industriales protegidos por ley**, este documento detalla con máxima precisión **qué hace el sistema, cómo procesa la información, cuáles son sus invariantes cuantitativos y qué salvaguardas operativas posee**, permitiendo una auditoría forense, funcional y de seguridad sin requerir la revelación de código ejecutable sensible ni comprometer la propiedad industrial.

---

## 2. NATURALEZA JURÍDICA Y DELIMITACIÓN REGULATORIA (NO-CUSTODIA)
Para efectos de evaluación de riesgo regulatorio en México (CNBV, Banco de México y CONDUSEF), el auditor debe constatar que el sistema opera bajo una estricta **arquitectura no custodial y de soporte didáctico-decisional**:

1. **Cero Captación de Recursos:** La plataforma no recibe, no intermedia, no administra ni capta fondos monetarios ni activos virtuales de terceros (no encuadra en los supuestos del Art. 2º ni Art. 11 de la Ley de Instituciones de Tecnología Financiara - Ley Fintech).
2. **Cero Custodia:** En ningún momento el sistema genera, almacena ni interactúa con llaves privadas criptográficas, contraseñas bancarias, tokens transaccionales o credenciales de retiro. Los usuarios conservan el control absoluto y exclusivo de su dinero en instituciones formalmente reguladas:
   - **Activos Virtuales:** Custodia individual en cuentas personales dentro de exchanges regulados (Bitso México).
   - **Renta Variable y FIBRAs:** Custodia individual en casas de bolsa autorizadas y supervisadas por la CNBV (Bursanet / Actinver).
3. **Ausencia de Asesoría Financiera Reservada:** El sistema no emite recomendaciones discrecionales personalizadas (Art. 210 de la Ley del Mercado de Valores - LMV). Su actividad se limita a la provisión de software educativo, visualización analítica de datos públicos de mercado y cálculo de indicadores técnicos matemáticos estandarizados al amparo de las libertades de expresión e imprenta consagradas en los **Artículos 6º y 7º Constitucionales**.

---

## 3. ARQUITECTURA DEL FRONTEND WEB (EXPERIENCIA PÚBLICA AUDITABLE)
La interfaz web (`ariaeden.github.io/patrimonio-web`) es el primer punto de contacto y opera como un entorno 100% de lado del cliente (*Client-Side Static Application*):

### 3.1. Procesamiento Local sin Telemetría Oculta
- **Aislamiento de Datos:** Todo cálculo matemático realizado en los simuladores se procesa localmente en la memoria del navegador del usuario. No existen cookies de rastreo, píxeles de telemetría de terceros ni captura de direcciones IP.
- **Navegación Ergonómica y Responsiva:** Header institucional con 4 módulos desplegables (*Primeros Pasos*, *Estrategia & Herramientas*, *Educación & Guías*, *Legal & Recursos*) y menú lateral tipo drawer para dispositivos móviles, garantizando lectura en cualquier resolución.

### 3.2. Modelo Matemático de Interés Compuesto Geométrico
Los auditores podrán verificar que la calculadora no incurre en errores de acumulación aritmética o lineal:
- **Capitalización Compuesta Mensual:** Modela aportaciones periódicas disciplinadas aplicando la tasa geométrica mensual exacta para evitar distorsiones de retorno:
  $$\text{Tasa Mensual} = (1 + r_a)^{1/12} - 1$$
- **Matriz de Estrés Macroeconómico:** Los rendimientos se proyectan a través de cuatro escenarios deterministas que incluyen variables de inflación, depreciación cambiaria y escenarios recesivos severos (incluyendo rendimientos reales netos negativos).
- **Contraste Didáctico:** Permite comparar el efecto del interés compuesto bursátil regulado (S&P 500 y dividendos por FIBRAs) con la apreciación histórica de Bitcoin, desglosando siempre el *Capital Aportado de Bolsillo* frente a la *Utilidad Generada*.

### 3.3. Evaluador de Activos con Oscilador Técnico Diario
- Presenta fichas analíticas didácticas de instrumentos clave del Sistema Internacional de Cotizaciones (SIC) y Bolsa Mexicana de Valores (BMV), tales como `FIBRAMQ12`, `FMTY14`, `IVVPESO` y `QQQM`.
- Cada activo modela su perfil de dividendos, costo de gestión anual (TER) y el nivel del oscilador de fuerza relativa RSI Wilder (14 días), educando al usuario en zonas de sobreventa y sobrecompra.

---

## 4. ARQUITECTURA DEL COPILOTO EN LA NUBE (LO QUE OCURRE TRAS BAMBALINAS)
El componente asíncrono opera mediante un microservicio en la nube (contenedor Docker en Render Cloud) conectado a la red de Telegram (`@dabel_btc_copiloto_bot`). Sus funciones clave comprenden:

### 4.1. Monitoreo Técnico 24/7 y Blindaje Anti-Alertas Prematuras (*Gatekeeper*)
- **Ingesta de Mercado en Tiempo Real:** El copiloto sondea continuamente el libro de órdenes público y los precios en vivo de Bitcoin en pares `BTC/USD` y `BTC/MXN`, así como el tipo de cambio interbancario de Banco de México / DOF.
- **Filtro Preventivo de Alertas (*Gatekeeper*):** A diferencia de bots convencionales que disparan notificaciones con cualquier oscilación menor, nuestro motor incorpora un filtro lógico estricto:
  * Si el usuario se encuentra en estado de liquidez fiat tras una venta previa, el sistema **bloquea cualquier alerta de compra** hasta que el mercado haya retrocedido al menos un **-2.5%** frente al precio de salida. Esto garantiza matemáticamente que el usuario capture satoshis gratuitos en la recompra y no malgaste su efectivo en micro-rebotes falsos.
  * Si el usuario ya posee satoshis en cartera, el sistema suprime alertas de compra si el precio cotiza por encima de su costo promedio de entrada, protegiendo su precio de equilibrio (*break-even*).

### 4.2. El Algoritmo de Doble Finalidad de Bitcoin
El sistema opera bajo dos modalidades que el usuario puede elegir según sus objetivos financieros:
1. **Modalidad A: Acumulación Intergeneracional (Modo Satoshis):**  
   Prioriza el volumen neto de satoshis acumulados. Ante lecturas de sobreventa técnica en temporalidad de 4 horas (RSI 4H &le; 30-35), el bot asiste al usuario para colocar órdenes de compra límite tipo **Maker** en Bitso (aprovechando tarifas mínimas de 0.10% a 0.60% y evitando el spread de mercado). El usuario adopta una filosofía de reserva de valor a largo plazo.
2. **Modalidad B: Cosecha de Capital y Rentas Inmobiliarias (Modo Flujo Fiat):**  
   Bitcoin opera como acelerador asimétrico de capital. Al dispararse condiciones de ciclo macro ($1,800,000+ MXN / $95,000+ USD) o zonas de sobrecompra extrema (RSI 4H &ge; 65-70), el sistema alerta para monetizar plusvalías en pesos/dólares y canalizarlas a casas de bolsa mexicanas para adquirir FIBRAs, amarrando flujos de efectivo en dividendos trimestrales regulados.

---

## 5. MOTOR DE AUDITORÍA CONTABLE Y CERTIFICACIÓN FORENSE
Uno de los componentes de mayor valor institucional del sistema es su motor de conciliación contable de órdenes ejecutadas:

### 5.1. Procesamiento de Comprobantes con Huella Criptográfica SHA-256
- Cuando un usuario envía una captura de pantalla de una orden ejecutada en Bitso, el sistema extrae los datos estructurales: fecha, tipo de orden, precio de entrada, volumen en BTC y total pagado/recibido.
- **Garantía Antiduplicación:** Cada transacción genera una firma criptográfica única mediante algoritmo **SHA-256** calculada a partir de los datos invariantes de la orden. Si un usuario intenta enviar dos veces la misma captura o si se genera un reenvío por error de red, el sistema detecta la colisión del hash y rechaza el registro duplicado, garantizando que el saldo nunca se infle artificialmente.

### 5.2. Invariante Contable: Segregación de Capital de Bolsillo vs Valuación
- El motor contable mantiene dos variables completamente desacopladas en el perfil de cada miembro:
  * `total_fiat_deposited_usd` y `total_fiat_deposited_mxn`: Reflejan estrictamente el dinero real aportado por el usuario de su bolsillo (depósitos netos).
  * `total_satoshis`: Refleja el balance acumulado de unidades Bitcoin.
- La valuación actual se calcula en tiempo real multiplicando los satoshis acumulados por el precio vivo del mercado. Esto erradica inconsistencias contables y permite calcular con exactitud la ganancia o pérdida patrimonial flotante y realizada.

### 5.3. Principio de Lectura Dual Obligatoria
Cada notificación, reporte contable o estado de cuenta emitido por el sistema presenta simultáneamente:
- **Cripto:** Monto exacto en Satoshis enteros (para disciplina de ahorro) y en fracción decimal de BTC (para coincidencia con la pantalla de Bitso).
- **Fiat:** Importe en Dólares Estadounidenses (USD) y su equivalente en Pesos Mexicanos (MXN).

---

## 6. PRIVACIDAD DE DATOS Y CUMPLIMIENTO LFPDPPP
El auditor puede certificar el estricto cumplimiento con la **Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP)**:

1. **Principio de Minimización de Datos:** El sistema no solicita RFC, CURP, comprobantes de domicilio ni estados de cuenta bancarios. El único identificador operativo es el `chat_id` numérico emitido por los servidores de Telegram y el nombre público voluntario provisto por el usuario.
2. **Tratamiento Efímero de Imágenes:** Las capturas de comprobantes se procesan exclusivamente para validar la transacción contable. No se comparten con servidores de publicidad ni con brokers externos.
3. **Mecanismo Automatizado de Derechos ARCO:** Mediante el comando nativo `/borrar_datos`, cualquier usuario puede solicitar en cualquier instante la cancelación y purga inmediata de su historial, eliminando sus registros de la base de datos de manera definitiva e irrevocable.
4. **Domicilio Legal de Contacto:** La plataforma cuenta con canal formal de representación jurídica y atención de solicitudes ARCO en la Ciudad de México.

---

## 7. GOBERNANZA, RESILIENCIA Y RECUPERACIÓN ANTE DESASTRES (*DISASTER RECOVERY*)
El sistema ha sido blindado ante caídas de infraestructura en la nube, suspensiones de servicio o fallas de hardware mediante una arquitectura de cuatro capas:

### 7.1. Segregación Estricta de Privilegios (Super-Admin)
El código diferencia categóricamente los comandos de consulta pública de los comandos de gobierno. Las instrucciones críticas (`/aprobar`, `/renovar`, `/suspender`, `/respaldo`, `/auditoria`) solo responden si el remitente coincide de forma exacta e invariable con el identificador criptográfico del **Super-Admin ID** (Hilda Belem Ortiz Fuentes).

### 7.2. Escritura Atómica y Auto-Sanación (*Self-Healing*)
- **Escritura Atómica:** Ninguna modificación a la base de datos se realiza sobre el archivo en caliente. El sistema escribe en un archivo temporal (`.tmp`), fuerza la sincronización física al disco duro (`fsync`) y renombra de manera atómica, previniendo que un corte de energía dañe el archivo.
- **Rotación de Snapshots:** Cada cambio genera copias de seguridad fechadas rotativas en el directorio seguro de backups.
- **Auto-Sanación:** Si por una anomalía de servidor el archivo principal de usuarios se ausentara o corrompiera, la subrutina de carga detecta el fallo en el arranque, acude automáticamente a la bóveda de respaldos, valida el último snapshot íntegro y restaura el padrón en milisegundos sin requerir intervención humana.

### 7.3. Bitácora Inmutable Write-Ahead Log (WAL)
Cada alta, renovación, depósito o acreditación se asienta en `user_rescue_audit_log.jsonl`. Este archivo funciona bajo el principio *append-only* (solo adición) donde cada línea contiene un sello de tiempo UTC-6, identificador de evento único y firma criptográfica SHA-256 encadenada. Permite a cualquier auditor reconstruir la historia contable completa del sistema paso a paso.

### 7.4. Respaldo Soberano Offline e Inmortalidad de Datos
Mediante el comando `/respaldo`, la administradora recibe periódicamente en su canal privado de Telegram:
1. `respaldo_usuarios_patrimonio_*.json`: Serialización completa de la base de datos de usuarios.
2. `bitso_libro_contable_*.json`: Libro mayor de transacciones certificadas.
3. `directorio_usuarios_rescate_*.csv`: Directorio soberano compatible con **Microsoft Excel** con nombres, contactos y balances.

**Garantía de Recuperación:** Con estos 3 archivos en posesión de la titular, el sistema completo puede recrearse de manera idéntica en cualquier servidor nuevo o computadora en menos de 10 segundos, asegurando la continuidad del negocio y la protección irrestricta de los usuarios ante cualquier eventualidad con proveedores de nube.

---

## 8. GUÍA Y CHECKLIST DE VERIFICACIÓN PARA AUDITORES EXTERNOS
Se sugiere al equipo auditor utilizar la siguiente matriz para validar la conformidad del sistema:

| Dimensión de Auditoría | Criterio de Evaluación | Evidencia Funcional Verificable |
| :--- | :--- | :--- |
| **No-Custodia Financiera** | Cero captación de depósitos y cero posesión de claves privadas. | Operativa orientada a Bitso y Bursanet; órdenes ejecutadas directamente por el usuario. |
| **Rigor Matemático** | Ausencia de sesgos lineales en interés compuesto; tasas geométricas continuas. | Calculadora web con capitalización mensual exacta y 4 escenarios de estrés macroeconómico. |
| **Protección al Consumidor** | Deslinde explícito de no-asesoría y transparencia en comisiones. | Deslinde de Arts. 6º y 7º Constitucionales; comparador didáctico de tarifas Maker vs Taker. |
| **Integridad Contable** | Prevención de registros duplicados e invariantes de capital. | Huellas criptográficas SHA-256 por orden; segregación de capital aportado vs valuación. |
| **Seguridad de la Información** | Privacidad de datos, minimización y ejercicio de derechos ARCO. | Registro exclusivo de `chat_id`; comando `/borrar_datos` funcional de purga inmediata. |
| **Resiliencia Operativa** | Capacidad de recuperación ante desastres y auto-sanación. | Escritura atómica `.tmp` + `fsync`; auto-reparación desde snapshots; exportación soberana CSV/JSON. |

---

## 9. DECLARACIÓN DE AUTORÍA Y TITULARIDAD
Se hace constar formalmente que el concepto, desarrollo, arquitectura de sistemas y documentación técnica han sido concebidos y materializados de forma íntegra y exclusiva por **Hilda Belem Ortiz Fuentes**, titular de la totalidad de los derechos morales y patrimoniales conforme al marco jurídico mexicano e internacional.

**Hilda Belem Ortiz Fuentes**  
Titular y Creadora de Patrimonio Inteligente  
Ciudad de México, Noviembre de 2026.
